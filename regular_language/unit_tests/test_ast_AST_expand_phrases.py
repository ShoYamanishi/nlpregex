#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.expand_phrases() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_expand_phrases( unittest.TestCase ):

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
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0002(self):

        spec01           = 'E_E01'
        string_expected  = ''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )

    def test_0003(self):

        spec01           = 'T_T01'
        string_expected  = 'T01'
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0003a(self):

        spec01           = 'T_T01'
        string_expected  = '( T01 [ token03 token04 ] )'
        ast01    = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')


        list01   = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0004(self):

        spec01           = 'N_N01'
        string_expected  = 'N01'
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0004a(self):

        spec01           = 'N_N01'
        string_expected  = '( N01 [ token03 token04 ] )'
        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_N01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0005(self):

        spec01           = 'S_S01:T_T01'
        string_expected  = 'T01'
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0005a(self):

        spec01           = 'S_S01:T_T01'
        string_expected  = '( [ token02 token01 ] ( T01 ) [ token03 token04 ] )'
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, 'S_S01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0005b(self):

        spec01           = 'S_S01:T_T01'
        string_expected  = '( T01 [ token03 token04 ] )'
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0005c(self):

        spec01           = 'S_S01:T_T01'
        string_expected  = '( [ token02 token01 ] ( ( T01 [ token07 token08 ] ) ) [ token03 token04 ] )'
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, 'S_S01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006(self):

        spec01           = 'S_S01:T_T01 N_N02'
        string_expected  = 'T01 N02'
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0006a(self):

        spec01           = 'S_S01:T_T01 N_N02'
        string_expected  = '( [ token02 token01 ] ( ( T01 [ token07 token08 ] ) ( N02 [ token11 token12 ] ) ) [ token03 token04 ] )'

        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, 'S_S01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        node_003 = self.helper.get_node(ast01, 'N_N02')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')


        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007(self):

        spec01           = '|_U01:T_T01'
        string_expected  = 'T01'
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007a(self):

        spec01           = '|_U01:T_T01'
        string_expected  = '( [ token02 token01 ] T01 [ token03 token04 ] )'
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '|_U01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')


        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007b(self):

        spec01           = '|_U01:T_T01'
        string_expected  = '( T01 [ token03 token04 ] )'
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, 'T_T01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')


        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0007c(self):

        spec01           = '|_U01:T_T01'
        string_expected  = '( [ token02 token01 ] ( T01 [ token07 token08 ] ) [ token03 token04 ] )'
                            
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '|_U01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0008(self):

        spec01           = '|_U01:T_T01 T_T02'
        string_expected  = '''
            T01
            T02
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0008a(self):

        spec01           = '|_U01:T_T01 T_T02'
        string_expected  = '''
            ( [ token02 token01 ] T01 [ token03 token04 ] )
            ( [ token02 token01 ] T02 [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '|_U01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)



        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0008b(self):

        spec01           = '|_U01:T_T01 T_T02'
        string_expected  = '''
            ( [ token02 token01 ] ( T01 [ token07 token08 ] ) [ token03 token04 ] )
            ( [ token02 token01 ] ( T02 [ token11 token12 ] ) [ token03 token04 ] )
        '''


        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '|_U01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        node_003 = self.helper.get_node(ast01, 'T_T02')
        node_003.append_out_token_pre ('token09')
        node_003.append_out_token_pre ('token10')
        node_003.append_out_token_post('token11')
        node_003.append_out_token_post('token12')


        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )



    def test_0009(self):

        spec01           = '|_U01:T_T01 N_N02 T_T03'
        string_expected  = '''
            T01
            N02
            T03
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0010(self):

        spec01           = '?_R01:T_T01'
        string_expected  = '''
            T01
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0010a(self):

        spec01           = '?_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] __EPS__ [ token03 token04 ] )
            ( [ token02 token01 ] T01 [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '?_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0010b(self):

        spec01           = '?_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] __EPS__ [ token03 token04 ] )
            ( [ token02 token01 ] ( T01 [ token07 token08 ] ) [ token03 token04 ] )
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

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0011(self):

        spec01           = '{0,3}_R01:T_T01'
        string_expected  = '''
            T01{ 0, 3 }
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0011a(self):

        spec01           = '{0,3}_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( T01{ 0, 3 } ) [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '{0,3}_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0011b(self):

        spec01           = '{0,3}_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] ){ 0, 3 } ) [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '{0,3}_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0012(self):

        spec01           = '{2,7}_R01:T_T01'
        string_expected  = '''
            T01{ 2, 7 }
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0012a(self):

        spec01           = '{2,7}_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( T01{ 2, 7 } ) [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '{2,7}_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)


        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0012b(self):

        spec01           = '{2,7}_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] ){ 2, 7 } ) [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '{2,7}_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0013(self):

        spec01           = '*_R01:T_T01'
        string_expected  = '''
            T01*
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0013a(self):

        spec01           = '*_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( T01* ) [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '*_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)


        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0013b(self):

        spec01           = '*_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] )* ) [ token03 token04 ] )
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

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)


        self.assertEqual( self.compare_specs(str01, string_expected), True )



    def test_0014(self):

        spec01           = '+_R01:T_T01'
        string_expected  = '''
            T01+
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0014a(self):

        spec01           = '+_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( T01+ ) [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '+_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)

        self.assertEqual( self.compare_specs(str01, string_expected), True )


    def test_0014b(self):

        spec01           = '+_R01:T_T01'
        string_expected  = '''
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] )+ ) [ token03 token04 ] )
        '''
        ast01 = self.construct_ast_from_spec(spec01)

        node_001 = self.helper.get_node(ast01, '+_R01')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_pre ('token02')
        node_001.append_out_token_post('token03')
        node_001.append_out_token_post('token04')

        node_002 = self.helper.get_node(ast01, 'T_T01')
        node_002.append_out_token_pre ('token05')
        node_002.append_out_token_pre ('token06')
        node_002.append_out_token_post('token07')
        node_002.append_out_token_post('token08')

        list01 = ast01.expand_phrases(True)
        str01 = '\n'.join(list01)
        self.assertEqual( self.compare_specs(str01, string_expected), True )




if __name__ == '__main__':
    unittest.main()
