#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for sse_symbol_manager.py """

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.fa
import nlpregex.regular_language.sse_forrest
import nlpregex.regular_language.sse_symbol_manager

class test_SymbolicEquation( unittest.TestCase ):


    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)


    def test_constructor_0001( self ):

        fa01 = nlpregex.regular_language.fa.FA()
        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa01 )

        self.assertEqual( manager01.sse_to_FAin,  {} )
        self.assertEqual( manager01.sse_to_FAout, {} )
        self.assertEqual( manager01.FAin_to_sse,  {} )
        self.assertEqual( manager01.next_id_to_be_allocated ,  1 )
        self.assertEqual( manager01.balanced_pairs ,  [] )
        self.assertEqual( manager01.solver_inputs ,  [] )


    def test_new_sse_token_0001( self ):

        fa01 = nlpregex.regular_language.fa.FA()
        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa01 )
        token01 = manager01.new_sse_token()
        token02 = manager01.new_sse_token()
        token03 = manager01.new_sse_token()
        token04 = manager01.new_sse_token()
        token05 = manager01.new_sse_token()
        token06 = manager01.new_sse_token()
        token07 = manager01.new_sse_token()
        token08 = manager01.new_sse_token()
        token09 = manager01.new_sse_token()
        token10 = manager01.new_sse_token()
        token11 = manager01.new_sse_token()
        token12 = manager01.new_sse_token()

        self.assertEqual( token01, 't1' )
        self.assertEqual( token02, 't2' )
        self.assertEqual( token03, 't3' )
        self.assertEqual( token04, 't4' )
        self.assertEqual( token05, 't5' )
        self.assertEqual( token06, 't6' )
        self.assertEqual( token07, 't7' )
        self.assertEqual( token08, 't8' )
        self.assertEqual( token09, 't9' )
        self.assertEqual( token10, 't10' )
        self.assertEqual( token11, 't11' )
        self.assertEqual( token12, 't12' )


    def test_generate_symbols_0001( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_epsilon()
        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa01 )
        manager01.generate_symbols()

        self.assertEqual( manager01.sse_to_FAin,  {} )
        self.assertEqual( manager01.sse_to_FAout, {} )
        self.assertEqual( manager01.FAin_to_sse,  {} )
        self.assertEqual( manager01.next_id_to_be_allocated ,  1 )
        self.assertEqual( manager01.balanced_pairs ,  [] )
        self.assertEqual( len(manager01.solver_inputs) ,  1 )
        self.assertEqual( manager01.solver_inputs[0] ,  ( 0, 1, 'e' ) )


    def test_generate_symbols_0002( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition('str01', '')
        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa01 )
        manager01.generate_symbols()

        self.assertEqual( len(manager01.sse_to_FAin),  1 )
        self.assertEqual( manager01.sse_to_FAin['t1'], 'str01' )

        self.assertEqual( manager01.sse_to_FAout, {} )

        self.assertEqual( len(manager01.FAin_to_sse),  1 )
        self.assertEqual( manager01.FAin_to_sse['str01'], 't1' )

        self.assertEqual( manager01.balanced_pairs ,  [] )

        self.assertEqual( len(manager01.solver_inputs) ,  1 )
        self.assertEqual( manager01.solver_inputs[0] ,  ( 0, 1, 't1' ) )


    def test_generate_symbols_0003( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition('[PRE 123]', 'str01')
        fa02 = nlpregex.regular_language.fa.make_unit_transition('str02', '')
        fa03 = nlpregex.regular_language.fa.make_unit_transition('[POST 123]', 'str03')

        serial01 = [fa01, fa02, fa03]

        fa04 = nlpregex.regular_language.fa.ttsp_concatenate( serial01 )

        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa04 )
        manager01.generate_symbols()

        self.assertEqual( len(manager01.sse_to_FAin),  3 )
        self.assertEqual( manager01.sse_to_FAin['t1'], '[PRE 123]' )
        self.assertEqual( manager01.sse_to_FAin['t2'], 'str02' )
        self.assertEqual( manager01.sse_to_FAin['t3'], '[POST 123]' )


        self.assertEqual( len(manager01.sse_to_FAout),  2 )
        self.assertEqual( manager01.sse_to_FAout['t1'], 'str01' )
        self.assertEqual( manager01.sse_to_FAout['t3'], 'str03' )

        self.assertEqual( len(manager01.FAin_to_sse),  3 )
        self.assertEqual( manager01.FAin_to_sse['[PRE 123]'],  't1' )
        self.assertEqual( manager01.FAin_to_sse['str02'],      't2' )
        self.assertEqual( manager01.FAin_to_sse['[POST 123]'], 't3' )

        self.assertEqual( len(manager01.balanced_pairs),  1 )
        self.assertEqual( manager01.balanced_pairs[0],  ('t1', 't3') )

        self.assertEqual( len(manager01.solver_inputs) ,  3 )
        self.assertEqual( manager01.solver_inputs[0] ,  ( 0, 1, 't1' ) )
        self.assertEqual( manager01.solver_inputs[1] ,  ( 1, 2, 't2' ) )
        self.assertEqual( manager01.solver_inputs[2] ,  ( 2, 3, 't3' ) )


    def test_generate_symbols_0003( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition('str01', '')
        fa02 = nlpregex.regular_language.fa.make_unit_transition('str02', '')
        fa03 = nlpregex.regular_language.fa.make_unit_transition('str01', '')
        fa04 = nlpregex.regular_language.fa.make_unit_transition('str02', '')

        serial01 = [ fa01, fa02, fa03, fa04 ]

        fa05 = nlpregex.regular_language.fa.ttsp_concatenate( serial01 )

        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa05 )
        manager01.generate_symbols()

        self.assertEqual( len(manager01.sse_to_FAin),  2 )
        self.assertEqual( manager01.sse_to_FAin['t1'], 'str01' )
        self.assertEqual( manager01.sse_to_FAin['t2'], 'str02' )

        self.assertEqual( len(manager01.sse_to_FAout),  0 )

        self.assertEqual( len(manager01.FAin_to_sse),  2 )
        self.assertEqual( manager01.FAin_to_sse['str01'],      't1' )
        self.assertEqual( manager01.FAin_to_sse['str02'],      't2' )

        self.assertEqual( len(manager01.balanced_pairs),  0 )

        self.assertEqual( len(manager01.solver_inputs) ,  4 )
        self.assertEqual( manager01.solver_inputs[0] ,  ( 0, 1, 't1' ) )
        self.assertEqual( manager01.solver_inputs[1] ,  ( 1, 2, 't2' ) )
        self.assertEqual( manager01.solver_inputs[2] ,  ( 2, 3, 't1' ) )
        self.assertEqual( manager01.solver_inputs[3] ,  ( 3, 4, 't2' ) )


    def test_get_fa_token_pair_0001( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition('[PRE 123]', 'str01')
        fa02 = nlpregex.regular_language.fa.make_unit_transition('str02', '')
        fa03 = nlpregex.regular_language.fa.make_unit_transition('[POST 123]', 'str03')

        serial01 = [fa01, fa02, fa03]

        fa04 = nlpregex.regular_language.fa.ttsp_concatenate( serial01 )

        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa04 )
        manager01.generate_symbols()

        fa_token_01 = manager01.get_fa_token_pair('t1')
        fa_token_02 = manager01.get_fa_token_pair('t2')
        fa_token_03 = manager01.get_fa_token_pair('t3')

        self.assertEqual( fa_token_01,  ( '[PRE 123]', 'str01' ) )
        self.assertEqual( fa_token_02,  ( 'str02', '' ) )
        self.assertEqual( fa_token_03,  ( '[POST 123]', 'str03' ) )


    def test_get_fa_token_pair_0002( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition('str01', '')
        fa02 = nlpregex.regular_language.fa.make_unit_transition('str02', '')
        fa03 = nlpregex.regular_language.fa.make_unit_transition('str01', '')
        fa04 = nlpregex.regular_language.fa.make_unit_transition('str02', '')

        serial01 = [ fa01, fa02, fa03, fa04 ]

        fa05 = nlpregex.regular_language.fa.ttsp_concatenate( serial01 )

        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa05 )
        manager01.generate_symbols()

        fa_token_01 = manager01.get_fa_token_pair('t1')
        fa_token_02 = manager01.get_fa_token_pair('t2')

        self.assertEqual( fa_token_01,  ( 'str01', '' ) )
        self.assertEqual( fa_token_02,  ( 'str02', '' ) )


    def test_handle_nonterminals_0001( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition('', '')
        nonterminals01 = []
        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa01 )

        manager01.handle_nonterminals( nonterminals01 )
        self.assertEqual( manager01.sse_to_NT, {} )


    def test_handle_nonterminals_0002( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition('', '')
        nonterminals01 = [ 'n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9' ]
        manager01 = nlpregex.regular_language.sse_symbol_manager.sseSymbolManager( fa01 )

        manager01.handle_nonterminals( nonterminals01 )
        self.assertEqual( len(manager01.sse_to_NT), 10 )
        self.assertEqual( manager01.sse_to_NT[ 'n0' ],  '<NT_0>' )
        self.assertEqual( manager01.sse_to_NT[ 'n1' ],  '<NT_1>' )
        self.assertEqual( manager01.sse_to_NT[ 'n2' ],  '<NT_2>' )
        self.assertEqual( manager01.sse_to_NT[ 'n3' ],  '<NT_3>' )
        self.assertEqual( manager01.sse_to_NT[ 'n4' ],  '<NT_4>' )
        self.assertEqual( manager01.sse_to_NT[ 'n5' ],  '<NT_5>' )
        self.assertEqual( manager01.sse_to_NT[ 'n6' ],  '<NT_6>' )
        self.assertEqual( manager01.sse_to_NT[ 'n7' ],  '<NT_7>' )
        self.assertEqual( manager01.sse_to_NT[ 'n8' ],  '<NT_8>' )
        self.assertEqual( manager01.sse_to_NT[ 'n9' ],  '<NT_9>' )


if __name__ == '__main__':

    unittest.main()

