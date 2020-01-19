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
class CommonRepetitionReducer():


    # @param forrest          : sseASForrect with a single tree under root.
    # @param min_num_subtrees : minimum number of identical subtrees 
    #                           required to be considered for reduction
    # @param min_num_terms    : minimum number of terms under the subtree
    #                           required to be considered for reduction
    def __init__( self, forrest ):

        super().__init__()
        self.forrest = forrest


    # @brief main public function to find and reduce common subtrees
    #
    def reduce( self ):

        self.forrest.prepare_for_reduction()

        self.visit_and_reduce( self.forrest.root )

    def visit_and_reduce( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            self.visit_and_reduce( c )

        if self.match_target_pattern(n):
            self.transform_pattern(n)



    # @brief detect the following pattern
    #
    #        ?
    #       / \
    #      Tr  *  
    #          |
    #          Tr
    #
    def match_target_pattern( self, n ):

        if n.ast_node_type != '?':
            return False

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        c0 = children[0]
        if c0.ast_node_type != 's':
            return False

        grand_children = [ e.other_node_of( c0 ) for e in  c0.out_neighbors() ]

        if len(grand_children) != 2:
            return False

        gc0 = grand_children[0]
        gc1 = grand_children[1]
        if gc1.ast_node_type != '*':
            return False

        grand_grand_children = [ e.other_node_of( gc1 ) for e in  gc1.out_neighbors() ]
        ggc0 = grand_grand_children[0]


        return gc0.regex == ggc0.regex


    # @brief detect the following pattern
    #
    #        ?                 *
    #       / \                |
    #      Tr  *         =>    Tr
    #          |
    #          Tr
    #
    def transform_pattern( self, n ):
        
        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        c0 = children[0]
        grand_children = [ e.other_node_of( c0 ) for e in  c0.out_neighbors() ]
        gc0 = grand_children[0]
        gc1 = grand_children[1]
        grand_grand_children = [ e.other_node_of( gc1 ) for e in  gc1.out_neighbors() ]
        ggc0 = grand_grand_children[0]

        self.forrest.remove_AST(gc1)
        self.forrest.pull_up_only_child( n )
        n.ast_node_type = '*'
        n.generate_regex()
        
