#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for fa_to_ast.py."""

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.fa
import nlpregex.regular_language.sse_forrest
import nlpregex.regular_language.fa_to_ast

from   nlpregex.regular_language.unit_tests.test_sse_asforrest_helper import test_sse_ASForrest_helper
from   nlpregex.regular_language.unit_tests.test_ast_helper           import test_AST_helper

from   nlpregex.regular_language.sse_symbol_manager                   import sseSymbolManager
from   nlpregex.regular_language.sse_solver                           import SymbolicSimultaneousEquations
from   nlpregex.regular_language.common_subtree_reducer               import CommonSubtreeReducer
from   nlpregex.regular_language.common_union_subexpression_reducer   import CommonUnionSubexpressionReducer
from   nlpregex.regular_language.common_substring_reducer             import CommonSubstringReducer


class test_FAtoAST( unittest.TestCase ):


    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.sse_helper = test_sse_ASForrest_helper()
        self.ast_helper = test_AST_helper()


    def test_constructor_0001( self ):

        fa01 = nlpregex.regular_language.fa.FA()

        inst01 = nlpregex.regular_language.fa_to_ast.FAtoAST( fa01 )

        self.assertEqual( inst01.fa,                  fa01 )
        self.assertEqual( inst01.ASTs,                {}   )
        self.assertEqual( inst01.min_num_occurrences, 2    )
        self.assertEqual( inst01.min_num_terms,       2    )


    def test_visit_and_construct_AST_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        fa01      = nlpregex.regular_language.fa.make_unit_transition( 'ABC', '' )
        inst01    = nlpregex.regular_language.fa_to_ast.FAtoAST( fa01 )
        forrest01 = inst01.convert()

        spec02 = self.sse_helper.display_tree( forrest01.root )
#        print ( spec02 )
#        print ( inst01.get_nonterminals() )
        str01 = inst01.get_main_AST().emit_formatted_text( 100, 4 )
#        print ( '[' + str01 + ']' )


    def test_visit_and_construct_AST_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        fa01      = nlpregex.regular_language.fa.make_unit_transition( 'ABC', '' )
        fa02      = nlpregex.regular_language.fa.make_unit_transition( 'DEF', '' )
        fa03      = nlpregex.regular_language.fa.make_unit_transition( 'GHI', '' )
        fa04      = nlpregex.regular_language.fa.make_unit_transition( 'JKL', '' )
        fa05      = nlpregex.regular_language.fa.ttsp_concatenate( [ fa01, fa02, fa03, fa04 ] )

        inst01    = nlpregex.regular_language.fa_to_ast.FAtoAST( fa05 )
        forrest01 = inst01.convert()

        spec02 = self.sse_helper.display_tree( forrest01.root )
#        print ( spec02 )
#        print ( inst01.get_nonterminals() )
        str01 = inst01.get_main_AST().emit_formatted_text( 100, 4 )
#        print ( '[' + str01 + ']' )


    def test_visit_and_construct_AST_0003( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        fa01      = nlpregex.regular_language.fa.make_unit_transition( 'ABC', '' )
        fa02      = nlpregex.regular_language.fa.make_unit_transition( 'DEF', '' )
        fa03      = nlpregex.regular_language.fa.make_unit_transition( 'GHI', '' )
        fa04      = nlpregex.regular_language.fa.make_unit_transition( 'JKL', '' )
        fa05      = nlpregex.regular_language.fa.ttsp_bundle( [ fa01, fa02, fa03, fa04 ] )
        inst01    = nlpregex.regular_language.fa_to_ast.FAtoAST( fa05 )
        forrest01 = inst01.convert()

        spec02 = self.sse_helper.display_tree( forrest01.root )
#        print ( spec02 )
#        print ( inst01.get_nonterminals() )
        str01 = inst01.get_main_AST().emit_formatted_text( 100, 4 )
#        print ( '[' + str01 + ']' )


    def test_visit_and_construct_AST_0004( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        fa01      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_00', '' )
        fa02      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_01', '' )
        fa03      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_02', '' )
        fa04      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_03', '' )
        fa05      = nlpregex.regular_language.fa.ttsp_concatenate( [ fa01, fa02, fa03, fa04 ] )
        fa06      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_04', '' )
        fa07      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_05', '' )
        fa08      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_06', '' )
        fa09      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_07', '' )
        fa10      = nlpregex.regular_language.fa.ttsp_concatenate( [ fa06, fa07, fa08, fa09 ] )

        fa11      = nlpregex.regular_language.fa.ttsp_bundle( [ fa05, fa10 ] )

        inst01    = nlpregex.regular_language.fa_to_ast.FAtoAST( fa11 )
        forrest01 = inst01.convert()

        spec02 = self.sse_helper.display_tree( forrest01.root )
#        print ( spec02 )
#        print ( inst01.get_nonterminals() )
        str01 = inst01.get_main_AST().emit_formatted_text( 100, 4 )
#        print ( '[' + str01 + ']' )


    def test_visit_and_construct_AST_0005( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        fa01      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_00', '' )
        fa02      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_01', '' )
        fa03      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_02', '' )
        fa04      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_03', '' )
        fa05      = nlpregex.regular_language.fa.ttsp_bundle( [ fa01, fa02, fa03, fa04 ] )
        fa06      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_04', '' )
        fa07      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_05', '' )
        fa08      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_06', '' )
        fa09      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_07', '' )
        fa10      = nlpregex.regular_language.fa.ttsp_bundle( [ fa06, fa07, fa08, fa09 ] )

        fa11      = nlpregex.regular_language.fa.ttsp_concatenate( [ fa05, fa10 ] )

        inst01    = nlpregex.regular_language.fa_to_ast.FAtoAST( fa11 )
        forrest01 = inst01.convert()

        spec02 = self.sse_helper.display_tree( forrest01.root )
#        print ( spec02 )
#        print ( inst01.get_nonterminals() )
        str01 = inst01.get_main_AST().emit_formatted_text( 100, 4 )
#        print ( '[' + str01 + ']' )


    def test_visit_and_construct_AST_0006( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        fa01      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_00', '' )
        fa02      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_01', '' )
        fa03      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_02', '' )
        fa04      = nlpregex.regular_language.fa.enclose_in_cycle( fa03, '*' )
        fa05      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_03', '' )
        fa06      = nlpregex.regular_language.fa.ttsp_concatenate( [ fa01, fa02, fa04, fa05 ] )

        fa07      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_04', '' )
        fa08      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_05', '' )
        fa09      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_06', '' )
        fa10      = nlpregex.regular_language.fa.make_unit_transition( 'TERM_07', '' )
        fa11      = nlpregex.regular_language.fa.ttsp_bundle( [ fa07, fa08, fa09, fa10 ] )

#        fa12      = nlpregex.regular_language.fa.ttsp_concatenate( [ fa06, fa11 ] )

        inst01    = nlpregex.regular_language.fa_to_ast.FAtoAST( fa06 )
        forrest01 = inst01.convert()

        spec02 = self.sse_helper.display_tree( forrest01.root )
        print ( spec02 )
        print ( inst01.get_nonterminals() )
        str01 = inst01.get_main_AST().emit_formatted_text( 100, 4 )
        print ( '[' + str01 + ']' )



if __name__ == '__main__':
    unittest.main()
