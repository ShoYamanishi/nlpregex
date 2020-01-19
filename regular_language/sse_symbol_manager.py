#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import re
from graphviz import Digraph

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph

from nlpregex.regular_language import fa


# @brief manages the in/out tokens of fa.FA
# Those tokens in fa.FA are converted to 't0', 't1', ...
# It also handles the special paired tokens denoted by
#     [PRE {:d}] and [POST {:d}].
# 
# - fa_to_ast
# - sse_forrest
# - sse_solver
# - common_subtree_reducer
# - common_union_subexpression_reducer
# - common_substring_reducer

class sseSymbolManager():

    def __init__(self, fa):


        self.fa = fa # FA
        self.sse_to_FAin  = {} # Mapping from sse's terminal such as 't0' to FA's in-token.
        self.sse_to_FAout = {} # Mapping from sse's terminal such as 't0' to FA's out-token.

        self.FAin_to_sse  = {} # Mapping from FA's in-token to sse's terminal
        self.sse_to_NT    = {} # Mapping from sse's nonterminal to '<NT_XXX>'

        self.next_id_to_be_allocated = 1

        self.balanced_pairs = []
        self.solver_inputs  = []

        self.re_balanced_token_patten = re.compile( r'^\[PRE [0-9]+\]$' )


    def new_sse_token( self ):

        next_token = 't{:d}'.format( self.next_id_to_be_allocated )

        self.next_id_to_be_allocated  += 1

        return next_token


    # Scan through the FA's in- and out- tokens, and construct mapping.
    def generate_symbols( self ):

        # generate sse terminals
        for e in self.fa.edges():

            if not e.is_epsilon():

                if e.in_token not in self.FAin_to_sse:

                    sse_token = self.new_sse_token()
                    self.FAin_to_sse  [ e.in_token ] = sse_token
                    self.sse_to_FAin  [ sse_token  ] = e.in_token

                    if e.out_token != '':

                        # Assume in_token is unique as in [PRE {:d}] or [POST {:d}].
                        self.sse_to_FAout [ sse_token  ] = e.out_token

        # generate sse_solver input list
        for e in self.fa.edges():

            if e.is_epsilon():
                self.solver_inputs.append( ( e.src_node.node_id, e.dst_node.node_id, 'e' ) )

            else:
                self.solver_inputs.append( ( e.src_node.node_id, e.dst_node.node_id, self.FAin_to_sse[e.in_token] ) )

        # generate balanced terminal list
        for fa_in in self.FAin_to_sse:
            if re.match( self.re_balanced_token_patten, fa_in ): 
                fa_in_pair = fa_in.replace( 'PRE', 'POST' )
                self.balanced_pairs.append( ( self.FAin_to_sse[fa_in], self.FAin_to_sse[fa_in_pair] ) )

    def handle_nonterminals( self,  nonterminals ):
        for nt in nonterminals:
            num_str = nt[1:] # 'nXXXX' -> 'XXXX'
            self.sse_to_NT[nt] = '<NT_' + num_str + '>'


    def sse_solver_input( self ):
        return self.solver_inputs


    def sse_solver_start_node( self ):
        return self.fa.start_node.node_id


    def sse_solver_final_nodes( self ):
        return [ n.node_id for n in self.fa.final_nodes ]


    def sse_common_expression_reducer_balanced_pairs( self ):
        return self.balanced_pairs


    def get_fa_token_pair(self, sse_token ):
        if sse_token in self.sse_to_FAout:
            return ( self.sse_to_FAin[sse_token],  self.sse_to_FAout[sse_token])
        else:
            return ( self.sse_to_FAin[sse_token], '' )

    def get_NT(self, sse_token):
        return self.sse_to_NT[sse_token]
