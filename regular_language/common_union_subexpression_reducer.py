#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph



class CommonUnionSubexpressionReducer():


    def __init__(self, forrest, min_num_subtrees = 2, min_num_terms = 2 ):

        self.forrest = forrest

        # @brief k: regex v: [ sseASNodes ]
        self.map_regex_to_node_set = {}

        # @brief list of union nodes
        self.unions           = []

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
        while self.reduce_best_common_subexpression():
            pass

    def reduce_best_common_subexpression( self ):

        self.map_regex_to_node_set = {}
        self.unions                = []

        self.forrest.prepare_for_reduction()

        self.find_unions()

        self.construct_map_union_pairs()

        self.augment_map_regex_pairs()

        regex = self.find_best_regex()

        if regex == '':
            return False

        nonterminal = self.forrest.allocate_nonterminal()

        node_list = list ( self.map_regex_to_node_set[regex] )

        node_whose_children_to_retain   = node_list[0]
        nodes_whose_children_to_discard = node_list[1:]

        self.move_children_to_new_tree( node_whose_children_to_retain, nonterminal, regex )

        for n in nodes_whose_children_to_discard:

            self.remove_children_and_replace_with_nonterminal( n, nonterminal, regex )

        return True


    def remove_children_and_replace_with_nonterminal( self, n, nonterminal, regex ):

        regex_terms = set( regex.split( '%' ) )    

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        children_to_retain  = []
        for c in children:
            if c.regex in regex_terms:
                self.forrest.remove_AST(c)
            else:
                children_to_retain.append(c)

        if len(children_to_retain) == 0:
            n.reset( nonterminal )

        else:
            c_new = self.forrest.create_initial_node( nonterminal )
            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            e.add_to_graph( self.forrest, n, c_new, "directed" )     

    def move_children_to_new_tree( self, n, nonterminal, regex ):

        regex_terms = set( regex.split( '%' ) )    
        
        children_edge = [ e for e in n.out_neighbors() ]
        children      = [ e.other_node_of( n ) for e in  children_edge ]
        children_to_move    = []
        children_to_retain  = []
        for i in range(0, len(children) ):
            c = children[i]
            if c.regex in regex_terms:
                children_to_move.append(c)                
                children_edge[i].remove_from_graph()

            else:
                children_to_retain.append(c)

        if len(children_to_retain) == 0:
            n.reset( nonterminal )

        else:
            c_new = self.forrest.create_initial_node( nonterminal )
            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            e.add_to_graph( self.forrest, n, c_new, "directed" )


        n_new = self.forrest.create_initial_node( 'u' )
        for c in children_to_move:
            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            e.add_to_graph( self.forrest, n_new, c, "directed" )

        e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
        e.add_to_graph( self.forrest, self.forrest.root, n_new, "directed" )
        self.forrest.root.children_map[nonterminal] = n_new

        

    def find_unions( self ):
        self.unions = []
        self.visit_and_find_unions(self.forrest.root  )


    def visit_and_find_unions( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            self.visit_and_find_unions( c )

        if n.ast_node_type == 'u':
            self.unions.append(n)


    def construct_map_union_pairs( self ):

        for i in range (0, len(self.unions) - 1 ):

            for j in range (i + 1, len(self.unions)):

                self.construct_map_union_pair( self.unions[i], self.unions[j] )


    def construct_map_union_pair( self, u1, u2 ):
        
        terms1 = set(u1.children_map.keys())
        terms2 = set(u2.children_map.keys())

        intsec_list = sorted ( list ( terms1.intersection( terms2 ) ) )

        if len( intsec_list ) >= 2:

            intsec_regex = '%'.join( intsec_list )

            if intsec_regex not in self.map_regex_to_node_set:
                self.map_regex_to_node_set[ intsec_regex ] = set()

            self.map_regex_to_node_set[ intsec_regex ].add(u1)
            self.map_regex_to_node_set[ intsec_regex ].add(u2)


    def augment_map_regex_pairs( self ):

        new_regex_found = True

        while new_regex_found:

            new_regex_found = False
            new_regexes_set = set()
            regexes = list( self.map_regex_to_node_set.keys() )
            for i in range (0, len(regexes) - 1 ):
                for j in range (i + 1, len(regexes)):

                    terms1 = set( regexes[i].split('%') )
                    terms2 = set( regexes[j].split('%') )

                    intsec =  terms1.intersection( terms2 )
                    intsec_list = sorted ( list ( intsec ) )
                    if len(intsec_list) >= 2:
                        if intsec == terms1:
                            for n in self.map_regex_to_node_set[ regexes[j] ]:
                                self.map_regex_to_node_set[ regexes[i] ].add(n)

                        elif intsec == terms2:
                            for n in self.map_regex_to_node_set[ regexes[i] ]:
                                self.map_regex_to_node_set[ regexes[j] ].add(n)

                        else:
                            intsec_regex = '%'.join( intsec_list )
                            if intsec_regex not in regexes:
                                print ('ckp1')
                                new_regexes_set.add( intsec_regex )
                                new_regex_found = True

            for regex in new_regexes_set:
                for n in self.unions:

                    if self.this_node_includes_regex(n, regex):
                        if regex not in self.map_regex_to_node_set:
                            self.map_regex_to_node_set[ regex ] = set()

                        self.map_regex_to_node_set[ regex ].add(n)


    def this_node_includes_regex( self, node, regex ):

        regex_list_tested  = set( regex.split( '%' ) )

        regex_list_in_node = set( node.children_map.keys() )

        regex_list_diff    = regex_list_tested - regex_list_in_node

        return len(regex_list_diff) == 0


    def find_best_regex( self ):

        best_regex        = ""
        best_num_subtrees = 0
        best_num_terms    = 0
        best_height       = 0

        for r in self.map_regex_to_node_set:

            if self.check_balanced_tokens( r ) == False:
                continue

            subtrees =  list ( self.map_regex_to_node_set[r] )
            cur_num_subtrees = len( subtrees )
            a_subtree = subtrees[0]
            subregexes = r.split( '%' )
            cur_num_terms    = 0
            cur_height       = a_subtree.height
            for subregex in subregexes:
                c = a_subtree.children_map[subregex]
                cur_num_terms  += c.num_terms

            cur_len_regex    = len(r)

            update           = False

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
