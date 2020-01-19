#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.emit_formatted_text() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_emit_formatted_text( unittest.TestCase ):

    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.helper = test_AST_helper()


    def construct_ast_from_spec( self, spec01 ):
        return self.helper.construct_ast_from_spec(spec01)


    def display_tree( self, ast01 ):
        return self.helper.display_tree(ast01)


    def compare_specs( self, spec01, spec02 ):
        return self.helper.compare_specs( spec01, spec02 )


    def test_0001(self):

        spec01           = ''
        string_expected  = ''

        ast01 = self.construct_ast_from_spec(spec01)
        str01 = ast01.emit_formatted_text(80, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0002(self):

        spec01           = 'T_T01'
        string_expected  = 'T01 [ token02 ]'

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )



    def test_0003(self):

        spec01           = 'N_N01'
        string_expected  = 'N01 [ token02 ]'

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_N01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0004(self):

        spec01           = 'E_E01'
        string_expected  = ''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'E_E01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )



    def test_0005(self):

        spec01           = '''
            S_S01:T_T01
        '''
        string_expected  = '''
            T01
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0005a(self):

        spec01           = '''
            S_S01:T_T01
        '''
        string_expected  = '''
            [ token01 ] ( T01 ) [ token02 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'S_S01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')


        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0005b(self):

        spec01           = '''
            S_S01:T_T01
        '''
        string_expected  = '''
            [ token01 ] ( T01 [ token04 ] ) [ token02 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'S_S01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token03')
        node_002.append_out_token_post('token04')


        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006(self):

        spec01           = '''
            S_S01:T_T01 T_T02
        '''
        string_expected  = '''
            T01 T02
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006a(self):

        spec01           = '''
            S_S01:T_T01 T_T02
        '''
        string_expected  = '''
            [ token01 ] ( T01 T02 ) [ token02 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'S_S01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006b(self):

        spec01           = '''
            S_S01:T_T01 T_T02
        '''
        string_expected  = '''
            T01 [ token02 ] T02
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006c(self):

        spec01           = '''
            S_S01:T_T01 T_T02
        '''
        string_expected  = '''
            T01 T02 [ token02 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T02')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006d(self):

        spec01           = '''
            S_S01:T_T01 T_T02
        '''
        string_expected  = '''
            T01 [ token02 ] T02 [ token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        node_002 = self.helper.get_node(ast01, 'T_T02')
        node_002.append_out_token_pre ('token03')
        node_002.append_out_token_post('token04')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006e(self):

        spec01           = '''
            S_S01:T_T01 T_T02
        '''
        string_expected  = '''
            [ token05 ] ( T01 [ token02 ] T02 [ token04 ] ) [ token06 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        node_002 = self.helper.get_node(ast01, 'T_T02')
        node_002.append_out_token_pre ('token03')
        node_002.append_out_token_post('token04')

        node_003 = self.helper.get_node(ast01, 'S_S01')
        node_003.append_out_token_pre ('token05')
        node_003.append_out_token_post('token06')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007(self):

        spec01           = '''
            S_T01:N_N01 N_N02
        '''
        string_expected  = '''
            N01 N02
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007a(self):

        spec01           = '''
            S_S01:N_N01 N_N02
        '''
        string_expected  = '''
            [ token01 ] ( N01 N02 ) [ token02 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'S_S01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007b(self):

        spec01           = '''
            S_S01:N_N01 N_N02
        '''
        string_expected  = '''
            N01 [ token02 ] N02
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_N01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007c(self):

        spec01           = '''
            S_S01:N_N01 N_N02
        '''
        string_expected  = '''
            N01 N02 [ token02 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_N02')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007d(self):

        spec01           = '''
            S_S01:N_N01 N_N02
        '''
        string_expected  = '''
            N01 [ token02 ] N02 [ token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_N01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        node_002 = self.helper.get_node(ast01, 'N_N02')
        node_002.append_out_token_pre ('token03')
        node_002.append_out_token_post('token04')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007e(self):

        spec01           = '''
            S_S01:N_N01 N_N02
        '''
        string_expected  = '''
            [ token05 ] ( N01 [ token02 ] N02 [ token04 ] ) [ token06 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_N01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        node_002 = self.helper.get_node(ast01, 'N_N02')
        node_002.append_out_token_pre ('token03')
        node_002.append_out_token_post('token04')

        node_003 = self.helper.get_node(ast01, 'S_S01')
        node_003.append_out_token_pre ('token05')
        node_003.append_out_token_post('token06')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007f(self):

        spec01           = '''
            S_S01:N_N01 N_N02
        '''
        string_expected  = '''
            [ token10 token09 ] ( N01 [ token03 token04 ] N02 [ token07 token08 ] ) [ token11 token12 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_N01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'N_N02')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        node_003 = self.helper.get_node(ast01, 'S_S01')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0008(self):

        spec01           = '''
            |_U01:T_T01 N_N02
        '''
        string_expected  = '''
            [ token10 token09 ] (
                T01 [ token03 token04 ] |
                N02 [ token07 token08 ]
            ) [ token11 token12 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'N_N02')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        node_003 = self.helper.get_node(ast01, '|_U01')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')

        str01 = ast01.emit_formatted_text(80, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0008a(self):

        spec01           = '''
            |_U01:T_T01 N_N02
        '''
        string_expected  = '''
            [ token10 token09 ] ( T01 [ token03 token04 ] | N02 [ token07 token08 ] ) [ token11 token12 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'N_N02')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        node_003 = self.helper.get_node(ast01, '|_U01')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')

        str01 = ast01.emit_formatted_text(0, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0009(self):

        spec01           = '''
            |_U01:T_T01
        '''
        string_expected  = '''
            [ token10 token09 ] ( T01 [ token03 token04 ] ) [ token11 token12 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_003 = self.helper.get_node(ast01, '|_U01')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')

        str01 = ast01.emit_formatted_text(10, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0009a(self):

        spec01           = '''
            |_U01:T_T01
        '''
        string_expected  = '''
            [ token10 token09 ] ( T01 [ token03 token04 ] ) [ token11 token12 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_003 = self.helper.get_node(ast01, '|_U01')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')

        str01 = ast01.emit_formatted_text(0, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0009b(self):

        spec01           = '''
            |_U01:T_T01
        '''
        string_expected  = '''
            ( T01 [ token03 token04 ] )
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        str01 = ast01.emit_formatted_text(0, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0009c(self):

        spec01           = '''
            |_U01:T_T01
        '''
        string_expected  = '''
            [ token10 token09 ] ( T01 ) [ token11 token12 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_003 = self.helper.get_node(ast01, '|_U01')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')

        str01 = ast01.emit_formatted_text(0, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0009d(self):

        spec01           = '''
            |_U01:T_T01
        '''

        string_expected  = '''
            T01
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        str01 = ast01.emit_formatted_text(0, 4)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0010(self):

        spec01           = '''
            ?_R01:T_T01
        '''

        string_expected  = '''
            T01?
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0010a(self):

        spec01           = '''
            ?_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( T01? ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '?_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0010b(self):

        spec01           = '''
            ?_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( ( T01 [ token07 token08 ] )? ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '?_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0011(self):

        spec01           = '''
            {0,2}_R01:T_T01
        '''

        string_expected  = '''
            T01{ 0, 2 }
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0011a(self):

        spec01           = '''
            {0,2}_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( T01{ 0, 2 } ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '?_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0011b(self):

        spec01           = '''
            {0,2}_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( ( T01 [ token07 token08 ] ){ 0, 2 } ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '?_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0012(self):

        spec01           = '''
            {0,2}_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( ( T01 [ token07 token08 ] ){ 0, 2 } ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '?_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0013(self):

        spec01           = '''
            *_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( ( T01 [ token07 token08 ] )* ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '*_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0013a(self):

        spec01           = '''
            *_R01:T_T01
        '''

        string_expected  = '''
            ( T01 [ token07 token08 ] )*
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0013b(self):

        spec01           = '''
            *_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( T01* ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '*_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0013c(self):

        spec01           = '''
            *_R01:T_T01
        '''

        string_expected  = '''
            T01*
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0014(self):

        spec01           = '''
            +_R01:T_T01
        '''

        string_expected  = '''
            [ token02 token01 ] ( ( T01 [ token07 token08 ] )+ ) [ token03 token04 ]
        '''

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '*_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')


        str01 = ast01.emit_formatted_text(0, 4)

        self.assertEqual( self.compare_specs(str01, string_expected), True )









if __name__ == '__main__':
    unittest.main()
