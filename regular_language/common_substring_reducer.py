#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph


class CommonSubstringReducer():


    def __init__(self, forrest, min_num_subtrees = 2, min_num_terms = 2 ):

        self.forrest = forrest

        # @brief k: regex v: { k: node v:[pos] }
        self.map_regex_to_node_set = {}

        self.series_nodes          = []

        # @brief minimum number of instances of a common subtree
        #        to be considered for reduction
        self.min_num_subtrees = min_num_subtrees

        # @brief minimum number of terminals in a common subtree
        self.min_num_terms    = min_num_terms

        self.balanced_tokens = {}


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
        while self.reduce_best_common_substring():
            pass


    def reduce_best_common_substring( self ):

        self.map_regex_to_node_set = {}
        self.series_nodes          = []

        self.forrest.prepare_for_reduction()

        self.find_series_nodes()

        self.map_regex_to_node_set = {}

        self.construct_map_series_pairs()

        regex = self.find_best_regex()

        if regex == '':
            return False

        num_terms = len(regex.split('%'))

        nonterminal = self.forrest.allocate_nonterminal()

        node_list = list ( self.map_regex_to_node_set[regex].keys() )

        node0      = node_list[0]
        nodes_rest = node_list[1:]

        pos_list0 = sorted ( list (self.map_regex_to_node_set[ regex ][ node0 ] ) )

        self.move_children_to_new_tree( node0,  nonterminal, num_terms, pos_list0 )

        for n in nodes_rest:
            pos_list = sorted ( list (self.map_regex_to_node_set[regex][n] ) )
            self.remove_children_and_replace_with_nonterminal( n, nonterminal, num_terms, pos_list )

        return True


    def move_children_to_new_tree( self, n, nonterminal, num_terms, pos_list ):

        edges    = [ e for e in  n.out_neighbors() ]
        children = [ e.other_node_of( n ) for e in  edges ]

        for e in edges:
            e.remove_from_graph()

        num_pos = len(pos_list)
        cur_pos_list_pos = 0;

        pos_list.append(-1) # sentinel

        new_children     = []
        children_to_move = []
        state            = 'adding' # 'discarding'/'moving'
        discard_until    = -1
        move_until       = -1
        first            = True

        for i in range ( 0, len( children ) ):

            c = children[ i ]

            if state == 'adding':

                if i == pos_list[cur_pos_list_pos]:

                    if first:
                        children_to_move.append( c )
                        c_new = self.forrest.create_initial_node( nonterminal )
                        new_children.append( c_new )
                        cur_pos_list_pos += 1
                        move_until = i + num_terms - 1
                        state      = 'moving'

                        first = False

                    else:
                        self.forrest.remove_AST( c )
                        c_new = self.forrest.create_initial_node( nonterminal )
                        new_children.append( c_new )
                        cur_pos_list_pos += 1

                        discard_until = i + num_terms - 1
                        state         = 'discarding'

                else:
                    new_children.append( c )

            elif state == 'moving':
                children_to_move.append( c )

                if i == move_until:
                    state = 'adding'

            elif state == 'discarding':
                self.forrest.remove_AST( c )

                if i == discard_until:
                    state = 'adding'

        for c in new_children:
            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            e.add_to_graph( self.forrest, n, c, "directed" )

        n.generate_regex()
        n.generate_children_map_for_union()

        if len(new_children) == 1:
            self.forrest.pull_up_only_child( n )

        n_new = self.forrest.create_initial_node( 's' )
        for c in children_to_move:
            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            e.add_to_graph( self.forrest, n_new, c, "directed" )
        n_new.generate_regex()
        n_new.generate_children_map_for_union()

        e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
        e.add_to_graph( self.forrest, self.forrest.root, n_new, "directed" )
        self.forrest.root.children_map[nonterminal] = n_new


    def remove_children_and_replace_with_nonterminal( self, n, nonterminal, num_terms, pos_list ):

        edges    = [ e for e in  n.out_neighbors() ]
        children = [ e.other_node_of( n ) for e in  edges ]

        for e in edges:
            e.remove_from_graph()

        num_pos = len(pos_list)
        cur_pos_list_pos = 0;

        pos_list.append(-1) # sentinel

        new_children  = []
        state         = 'adding' # 'discarding'
        discard_until = -1

        for i in range ( 0, len( children ) ):

            c = children[ i ]

            if state == 'adding':

                if i == pos_list[cur_pos_list_pos]:

                    self.forrest.remove_AST( c )
                    c_new = self.forrest.create_initial_node( nonterminal )
                    new_children.append( c_new )
                    cur_pos_list_pos += 1

                    discard_until = i + num_terms - 1
                    state         = 'discarding'

                else:
                    new_children.append( c )

            else:
                self.forrest.remove_AST( c )

                if i == discard_until:
                    state = 'adding'

        for c in new_children:
            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            e.add_to_graph( self.forrest, n, c, "directed" )

        if len(new_children) == 1:
            self.forrest.pull_up_only_child( n )

        n.generate_regex()
        n.generate_children_map_for_union()


    def find_series_nodes( self ):

        self.series_nodes = []

        self.visit_and_find_series_nodes(self.forrest.root  )


    def visit_and_find_series_nodes( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            self.visit_and_find_series_nodes( c )

        if n.ast_node_type == 's':
            self.series_nodes.append(n)


    def construct_map_series_pairs( self ):

        for i in range (0, len(self.series_nodes) ):

            # Includes self comparison.
            for j in range (i, len(self.series_nodes)):

                self.construct_map_series_pair( self.series_nodes[i], self.series_nodes[j] )


    def construct_map_series_pair( self, s1, s2 ):

        terms1 = [ e.other_node_of( s1 ).regex for e in  s1.out_neighbors() ]
        terms2 = [ e.other_node_of( s2 ).regex for e in  s2.out_neighbors() ]

        len_terms1 = len(terms1)
        len_terms2 = len(terms2)
        
        terms1aug = ([''] * len_terms2 ) + terms1 + ([''] * len_terms2 )

        s1_regex_to_pos_list= {}
        s2_regex_to_pos_list= {}

        for comp_base_1 in range (2, len_terms2 + len_terms1 - 1 ):

            tstack = []
            for comp_base_2 in range(0, len_terms2):
                t1 = terms1aug[ comp_base_1 + comp_base_2 ]
                t2 = terms2   [ comp_base_2 ]
                if t1 == t2 and t1 != '':
                    tstack.append(t1)
                    len_tstack = len(tstack)

                    for partial_len_tstack in range( 2, len_tstack + 1 ):
                        s1_pos = comp_base_1 + comp_base_2 - len_terms2 - partial_len_tstack + 1
                        s2_pos = comp_base_2 - partial_len_tstack + 1

                        cur_regex = '%'.join( tstack[ len_tstack - partial_len_tstack : len_tstack ] )

                        if s1 != s2 or abs(s1_pos - s2_pos) >= partial_len_tstack:

                            if cur_regex not in s1_regex_to_pos_list:
                                s1_regex_to_pos_list[cur_regex] = []

                            if not self.has_overlap(s1_pos, partial_len_tstack, s1_regex_to_pos_list[cur_regex]):
                                s1_regex_to_pos_list[cur_regex].append(s1_pos)

                            if cur_regex not in s2_regex_to_pos_list:
                                s2_regex_to_pos_list[cur_regex] = []

                            if not self.has_overlap(s2_pos, partial_len_tstack, s2_regex_to_pos_list[cur_regex]):
                                s2_regex_to_pos_list[cur_regex].append(s2_pos)

                else:
                    tstack = []


            len_tstack = len(tstack)
            comp_base_2 = len_terms2

            for partial_len_tstack in range( 2, len_tstack + 1 ):
                s1_pos = comp_base_1 + comp_base_2 - len_terms2 - partial_len_tstack
                s2_pos = comp_base_2 - partial_len_tstack

                cur_regex = '%'.join( tstack[ len_tstack - partial_len_tstack : len_tstack ] )

                if s1 != s2 or abs(s1_pos - s2_pos) >= partial_len_tstack:

                    if cur_regex not in s1_regex_to_pos_list:
                        s1_regex_to_pos_list[cur_regex] = []

                    if not self.has_overlap(s1_pos, partial_len_tstack, s1_regex_to_pos_list[cur_regex]):
                        s1_regex_to_pos_list[cur_regex].append(s1_pos)

                    if cur_regex not in s2_regex_to_pos_list:
                        s2_regex_to_pos_list[cur_regex] = []

                    if not self.has_overlap(s2_pos, partial_len_tstack, s2_regex_to_pos_list[cur_regex]):
                        s2_regex_to_pos_list[cur_regex].append(s2_pos)


        for regex in s1_regex_to_pos_list:

            if regex not in self.map_regex_to_node_set:
                self.map_regex_to_node_set[regex] = {}

            if s1 not in self.map_regex_to_node_set[regex]:
                self.map_regex_to_node_set[regex][s1] = set()

            for pos in s1_regex_to_pos_list[regex]:
                self.map_regex_to_node_set[regex][s1].add(pos)

        for regex in s2_regex_to_pos_list:

            if regex not in self.map_regex_to_node_set:
                self.map_regex_to_node_set[regex] = {}

            if s2 not in self.map_regex_to_node_set[regex]:
                self.map_regex_to_node_set[regex][s2] = set()

            for pos in s2_regex_to_pos_list[regex]:
                self.map_regex_to_node_set[regex][s2].add(pos)


    def has_overlap( self, p1, length, pos_list):
        for p2 in pos_list:
            if abs(p1 - p2) < length:
                return True
        return False


    def find_best_regex( self ):

        best_regex        = ""
        best_num_subtrees = 0
        best_num_terms    = 0
        best_height       = 0

        for r in self.map_regex_to_node_set:

            if self.check_balanced_tokens( r ) == False:
                continue

            node_pos_dict  = self.map_regex_to_node_set[r]
            nodes          = list (node_pos_dict.keys() )
            node0          = nodes[0]
            node0_pos0     = list(node_pos_dict[node0])[0]
            len_regex      = len( r.split('%') )
            node0_children = [ e.other_node_of( node0 ) for e in  node0.out_neighbors() ]

            cur_num_subtrees = 0
            for n in nodes:
                cur_num_subtrees += len( node_pos_dict[n] )

            cur_num_terms    = 0
            cur_height       = node0.height
            for i in range(node0_pos0, node0_pos0 + len_regex ):
                c = node0_children[i]
                cur_num_terms  += c.num_terms

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
