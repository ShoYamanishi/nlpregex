#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph

import nlpregex.regular_language.fa
import nlpregex.regular_language.ast
from   nlpregex.regular_language.sse_symbol_manager import sseSymbolManager
from   nlpregex.regular_language.sse_solver         import SymbolicSimultaneousEquations

from   nlpregex.regular_language.common_subtree_reducer             import CommonSubtreeReducer
from   nlpregex.regular_language.common_union_subexpression_reducer import CommonUnionSubexpressionReducer
from   nlpregex.regular_language.common_substring_reducer           import CommonSubstringReducer
from   nlpregex.regular_language.common_repetition_reducer          import CommonRepetitionReducer

# @class FAtoAST
# 
# @description 
#
#   This converts a finite state automaton to a corresponding set of ASTs.
#   it first converts the finist state automaton to a single AST by solving a set of simultaneous symbolic equations.
#   it then finds common subexpressions in the AST and isolate them in a greedy way to sub-ASTs.
#
#
# @usage
#
#   converter = FAtoAST( fa, min_num_occurrences, min_num_terms )
#
#   @param fa : FA (finite state automata) to be converted to AST.
#   @param min_num_corrences : the minimum number of occurences of a common subexpression
#                              required to be subject for reduction.
#   @param min_num_terms     : the minimum number of terminals in a common subexpression
#                              required to be subject for reduction.
#
#   converter.convert( reduceCommonSubtree, reduceCommonUnionSubexpression, reduceCommonSubstring )
#  
#   @param reduceCommonSubtree : set to True if you want to perform common subtree reduction.
#   @param reduceCommonUnionSubexpression : set to True if you want perform common union subexpression reduction. 
#   @param reduceCommonSubstring : set to True if you want to perform common substring reduction.
#
#
#   The resultant ASTs can be retrieved with the following functions.
#
#   1. Get the top-level AST.
#   
#   ast = converter.get_main_AST() # Returns the top-level AST.
#   
#   2. Get the nonterminals. Each AST is associated with a corresponding nonterminal.
#
#   nonterminal_list = converter.get_nonterminals()
#   
#   3. Get the AST for a specified nonterminal
#
#   converter.ASTs[nonterminal]
#
#   The top-level AST is associated with <NT_0>.
#
#
# @note
#
# NOTES on the treatment of output tokens in FA.
# The pair output tokens are designated by the following input tokens.
#   '[PRE {:d}]' /  '[POST {:d}]'
#
# Those are assumed to be serially changed together in FA.
#
#                 in:'[PRE 123]'                                 in:'[POST 123]'
#  Ex. State 1 -------------------> State 2 -> ... -> State N-1 -------------------> State N 
#                out: 'str pre'                                  out: 'str post'
#
# Those are restored in the resultant ASTNode of 'terminal' or 'sequence' type as follows:
#
#   out_token_pre  = 'str pre'
#   out_token_post = 'str post'


def get_main_AST( self ):
    return self.ASTs[self.symManager.get_NT('n0')]

def get_nonterminals( self ):
    return list( self.ASTs.keys() )

class FAtoAST():


    def __init__( self, fa, min_num_occurrences = 2, min_num_terms = 2 ):

        self.fa  = fa # FA
        self.symManager = sseSymbolManager(fa)
        self.symManager.generate_symbols()

        self.ASTs= {} # k: nonterminal, v: root node to AST
        self.min_num_occurrences = min_num_occurrences 
        self.min_num_terms       = min_num_terms


    def convert( self, reduceCommonSubtree = True, reduceCommonUnionSubexpression = True, reduceCommonSubstring = True ):

        # 1. Construct SSE and solve
        solver = SymbolicSimultaneousEquations()

        for ( i, j, sym ) in self.symManager.sse_solver_input():
            solver.add_coeff( i, j, [sym] )

        forrest = solver.solve( self.symManager.sse_solver_start_node(), self.symManager.sse_solver_final_nodes() )

        # 2. Reduce ( T T* )? to T*
        reducer01 = CommonRepetitionReducer( forrest )
        reducer01.reduce()

        # 3. Reduce common subtrees
        if reduceCommonSubtree:
            reducer02 = CommonSubtreeReducer( forrest, self.min_num_occurrences, self.min_num_terms )
            reducer02.set_balanced_tokens( self.symManager.sse_common_expression_reducer_balanced_pairs() )
            reducer02.reduce()

        # 4. Reduce common union subexpressions
        if reduceCommonUnionSubexpression:
            reducer03 = CommonUnionSubexpressionReducer( forrest, self.min_num_occurrences, self.min_num_terms )
            reducer03.set_balanced_tokens( self.symManager.sse_common_expression_reducer_balanced_pairs() )
            reducer03.reduce()

        # 5. Reduce common substrings
        if reduceCommonSubstring:
            reducer04 = CommonSubstringReducer( forrest, self.min_num_occurrences, self.min_num_terms )
            reducer04.set_balanced_tokens( self.symManager.sse_common_expression_reducer_balanced_pairs() )
            reducer04.reduce()

        # 6. Remove nonterminal-only trees.
        forrest.remove_nt_only_trees();

        # 7. Modify sseAST for balanced tokens.
        forrest.balance_trees_for_out_tokens( self.symManager.sse_common_expression_reducer_balanced_pairs() )

        # 8. Find all the nonterminals and generate proper symbols.
        nonterminals = forrest.find_nonterminals()
        self.symManager.handle_nonterminals( nonterminals )

        # 9. Convert sseASTs to ASTs
        self.construct_ASTs(forrest)

        return forrest;


    def get_main_AST( self ):
        return self.ASTs[self.symManager.get_NT('n0')]

    def get_nonterminals( self ):
        return list( self.ASTs.keys() )


    def construct_ASTs( self, forrest ):

        master_root = forrest.root
        for nt in forrest.root.children_map:

            sse_root = forrest.root.children_map[nt]
            ast      = nlpregex.regular_language.ast.AST()
            ast_root = self.visit_and_construct_AST( ast, sse_root )
            ast.add_root( ast_root )
            self.ASTs[self.symManager.get_NT(nt)] = ast


    def visit_and_construct_AST( self, ast, sse_n ):

        sse_children = [ e.other_node_of( sse_n ) for e in  sse_n.out_neighbors() ]
        ast_children = []
        ast_n = None

        for sse_c in sse_children:
            ast_children.append( self.visit_and_construct_AST(ast, sse_c) )


        if sse_n.ast_node_type == 'u':
            ast_n = nlpregex.regular_language.ast.ASTNode('union', '')

        elif sse_n.ast_node_type == 's':
            ast_n = nlpregex.regular_language.ast.ASTNode('sequence', '')

        elif sse_n.ast_node_type == '*':
            ast_n = nlpregex.regular_language.ast.ASTNode('infinite repeat', '')
            ast_n.set_repeat( 0, -1 )

        elif sse_n.ast_node_type == '?':
            ast_n = nlpregex.regular_language.ast.ASTNode('finite repeat', '')
            ast_n.set_repeat( 0, 1 )

        elif sse_n.ast_node_type[0] == 't':
            T1, T2 = self.symManager.get_fa_token_pair( sse_n.ast_node_type )
            ast_n = nlpregex.regular_language.ast.ASTNode( 'terminal', T1 )

        elif sse_n.ast_node_type[0] == 'n':
            NT = self.symManager.get_NT( sse_n.ast_node_type )
            ast_n = nlpregex.regular_language.ast.ASTNode( 'nonterminal', NT )
        else:
            print ('ERROR UNKNOWN TYPE: ' + sse_n.ast_node_type )
            return None

        if sse_n.balanced_out_pre  != '':
            out_tokens = list( reversed( sse_n.balanced_out_pre.split(' ') ) )
            for t in out_tokens:
                ast_n.append_out_token_pre(t)

        if sse_n.balanced_out_post != '':
            out_tokens = sse_n.balanced_out_post.split(' ')
            for t in out_tokens:
                ast_n.append_out_token_post(t)

        ast_n.add_to_graph(ast)

        for ast_c in ast_children:
            ast_e = nlpregex.regular_language.ast.ASTEdge()
            ast_e.add_to_graph(  ast, ast_n, ast_c,  dir="directed" )

        return ast_n
