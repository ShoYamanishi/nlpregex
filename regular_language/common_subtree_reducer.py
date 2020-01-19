#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph
import nlpregex.regular_language.sse_forrest


# @brief finds common subtrees (regular subexpressions) in sseASForrest, 
#        and replace all the occurrences with a new nonterminal
#        the common subtree is added under 'r' node.
#
class CommonSubtreeReducer():


    # @param forrest          : sseASForrect with a single tree under root.
    # @param min_num_subtrees : minimum number of identical subtrees 
    #                           required to be considered for reduction
    # @param min_num_terms    : minimum number of terms under the subtree
    #                           required to be considered for reduction
    def __init__( self, forrest, min_num_subtrees = 2, min_num_terms = 2 ):

        super().__init__()
        self.forrest = forrest

        # @brief k: regex v: [ sseASNodes ]
        self.map_regex_to_node_list = {}

        # @brief minimum number of instances of a common subtree
        #        to be considered for reduction
        self.min_num_subtrees = min_num_subtrees

        # @brief minimum number of terminals in a common subtree
        self.min_num_terms    = min_num_terms

        self.balanced_tokens  = {}


    # @brief 
    # @param token_pairs: list of tuple of (first token, second token)
    def set_balanced_tokens( self, token_pairs ):
        for first_token, second_token in token_pairs:
            self.balanced_tokens[first_token] = second_token


    def check_balanced_tokens( self, regex_str ):

        pending_second_tokens = set()
        terms = regex_str.split('%')

        for term in terms:
            subterms = term.split(' ')
            for subterm in subterms:
                if subterm in self.balanced_tokens:
                    pending_second_tokens.add(self.balanced_tokens[subterm])
                elif subterm in pending_second_tokens:
                    pending_second_tokens.remove(subterm)

        return len( pending_second_tokens ) == 0


    # @brief main public function to find and reduce common subtrees
    #
    def reduce( self ):
        while self.reduce_best_common_subtree():
            pass


    # @brief second top-level function to find the current best 
    #        common subtree and to reduce it.
    #
    # @return True if a common subtree is found and reduced
    #         False otherwise
    def reduce_best_common_subtree( self ):

        # Regenerate regex, index all the nodes, and put them to the map
        self.map_regex_to_node_list = {}

        self.forrest.prepare_for_reduction()

        self.visit_and_find_common_subtrees( self.forrest.root )

        regex = self.find_best_common_subtree()
        if regex == '':
            return False

        # retain the first subtree, and discard the rest.
        # when discarding remove the entries in map_regex_to_node_list
        nonterminal      = self.forrest.allocate_nonterminal()

        tree_to_retain   = self.map_regex_to_node_list[regex][0]
        trees_to_discard = self.map_regex_to_node_list[regex][1:]

        for t in trees_to_discard:
            self.replace_subtree_with_nonterminal( t, nonterminal )

        self.replace_subtree_with_nonterminal_and_place_under_root( tree_to_retain, nonterminal )

        return True


    # @brief recursiverly construct self.map_regex_to_node_list
    def visit_and_find_common_subtrees( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            self.visit_and_find_common_subtrees( c )

        if n.ast_node_type != 'r' and n.ast_node_type[0] != 't' and n.ast_node_type[0] != 'n':

            if n.regex not in self.map_regex_to_node_list:
                self.map_regex_to_node_list[n.regex] = []

            self.map_regex_to_node_list[n.regex].append(n)


    # @criteria: - s.t. min_num_subtrees < len(map_regex_to_node_list[R])
    #            - s.t. min_num_terms    < map_regex_to_node_list[0].num_terms
    #            - max (map_regex_to_node_list[0].height)
    def find_best_common_subtree( self ):

        best_regex        = ""
        best_num_subtrees = 0
        best_num_terms    = 0
        best_height       = 0

        for r in self.map_regex_to_node_list:

            if self.check_balanced_tokens( r   ) == False:
                continue

            subtrees =  self.map_regex_to_node_list[r]

            cur_num_subtrees = len( subtrees )
            cur_num_terms    = subtrees[0].num_terms
            cur_height       = subtrees[0].height
            cur_len_regex    = len(r)

            update = False

            if cur_num_subtrees >= self.min_num_subtrees and cur_num_terms >= self.min_num_terms:

                if best_height < cur_height:
                    update = True

                elif  best_height == cur_height and best_num_subtrees < cur_num_subtrees:
                    update = True

                elif  best_height == cur_height and best_num_subtrees == cur_num_subtrees and best_num_terms < cur_num_terms:
                    update = True

                elif  best_height == cur_height and best_num_subtrees == cur_num_subtrees and best_num_terms == cur_num_terms and len(best_regex) < len(r):
                    update = True

            if update:
                best_height       = cur_height
                best_num_subtrees = cur_num_subtrees
                best_num_terms    = cur_num_terms
                best_regex        = r

        return best_regex


    def replace_subtree_with_nonterminal_and_place_under_root( self, t, nonterminal ):
        
        out_edges = [ e for e in  t.out_neighbors() ]
        children  = [ e.other_node_of( t ) for e in  out_edges ]

        for e in out_edges:
            e.remove_from_graph()

        n = self.forrest.create_initial_node( t.ast_node_type )

        for c in children:       

            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            e.add_to_graph( self.forrest , n, c, "directed" )

        e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
        e.add_to_graph( self.forrest, self.forrest.root, n, "directed" )            
        self.forrest.root.children_map[ nonterminal ] = n

        t.reset( nonterminal )
        

    def replace_subtree_with_nonterminal( self, t, nonterminal ):

        children = [ e.other_node_of( t ) for e in  t.out_neighbors() ]
        for c in children:
            self.forrest.remove_AST( c )

        t.reset( nonterminal )
