#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.clean_epsilon() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_clean_epsilon( unittest.TestCase ):

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

        spec01           = 'S_001:E_002'
        spec_expected_01 = ''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0002(self):

        spec01           = 'S_001:T_002 E_003'
        spec_expected_01 = 'T_002'

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0003(self):

        spec01           = 'S_001:T_002 E_003 T_004'
        spec_expected_01 = 'S_001:T_002 T_004'

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0004(self):

        spec01           = '|_001:E_002'
        spec_expected_01 = ''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0005(self):

        spec01           = '|_001:T_002 E_003'
        spec_expected_01 = '?_001:T_002'

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0006(self):

        spec01           = '|_001:T_002 E_003 T_003'
        spec_expected_01 = '''
            ?_???:|_001
            |_001:T_002 T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0007(self):

        spec01           = '|_001:T_002'
        spec_expected_01 = '''
            T_002
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0008(self):

        spec01           = '?_001:E_002'
        spec_expected_01 = '''
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0009(self):

        spec01           = '?_001:T_002'
        spec_expected_01 = '''
            ?_001:T_002
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0010(self):

        spec01           = '''
            ?_001:S_002
            S_002:T_003
        '''
        spec_expected_01 = '''
            ?_001:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0011(self):

        spec01           = '''
            ?_001:T_002
        '''
        spec_expected_01 = '''
            ?_001:T_002
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0011a(self):

        spec01           = '''
            ?_001:?_002
            ?_002:T_003
        '''
        spec_expected_01 = '''
            ?_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0011b(self):

        spec01           = '''
            ?_001:{0,2}_002
            {0,2}_002:T_003
        '''
        spec_expected_01 = '''
            {0,2}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0011c(self):

        spec01           = '''
            ?_001:{1,3}_002
            {1,3}_002:T_003
        '''
        spec_expected_01 = '''
            {0,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0011d(self):

        spec01           = '''
            ?_001:{2,3}_002
            {2,3}_002:T_003
        '''
        spec_expected_01 = '''
            ?_001:{2,3}_002
            {2,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0012(self):

        spec01           = '''
            {0,3}_001:E_002
        '''
        spec_expected_01 = '''
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0013(self):

        spec01           = '''
            {0,3}_001:T_002
        '''
        spec_expected_01 = '''
            {0,3}_001:T_002
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0014(self):

        spec01           = '''
            {0,3}_001:*_002
            *_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0015(self):

        spec01           = '''
            {0,3}_001:+_002
            +_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0015a(self):

        spec01           = '''
            {0,3}_001:?_002
            ?_002:T_003
        '''
        spec_expected_01 = '''
            {0,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0015b(self):

        spec01           = '''
            {0,3}_001:{0,3}_002
            {0,3}_002:T_003
        '''
        spec_expected_01 = '''
            {0,3}_001:{0,3}_002
            {0,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0015c(self):

        spec01           = '''
            {0,3}_001:{1,3}_002
            {1,3}_002:T_003
        '''
        spec_expected_01 = '''
            {0,3}_001:{1,3}_002
            {1,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0015d(self):

        spec01           = '''
            {0,3}_001:{2,6}_002
            {2,6}_002:T_003
        '''
        spec_expected_01 = '''
            {0,3}_001:{2,6}_002
            {2,6}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )



    def test_0016(self):

        spec01           = '''
            {1,3}_001:E_002
        '''
        spec_expected_01 = '''
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0017(self):

        spec01           = '''
            {1,3}_001:*_002
            *_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0018(self):

        spec01           = '''
            {1,3}_001:+_002
            +_002:T_003
        '''
        spec_expected_01 = '''
            +_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0018a(self):

        spec01           = '''
            {1,3}_001:?_002
            ?_002:T_003
        '''
        spec_expected_01 = '''
            {0,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0018b(self):

        spec01           = '''
            {1,3}_001:{0,3}_002
            {0,3}_002:T_003
        '''
        spec_expected_01 = '''
            {1,3}_001:{0,3}_002
            {0,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0018c(self):

        spec01           = '''
            {1,3}_001:{1,3}_002
            {1,3}_002:T_003
        '''
        spec_expected_01 = '''
            {1,3}_001:{1,3}_002
            {1,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0018d(self):

        spec01           = '''
            {1,3}_001:{2,4}_002
            {2,4}_002:T_003
        '''
        spec_expected_01 = '''
            {1,3}_001:{2,4}_002
            {2,4}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0019(self):

        spec01           = '''
            {2,3}_001:E_002
        '''
        spec_expected_01 = '''
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0020(self):

        spec01           = '''
            {2,3}_001:T_002
        '''
        spec_expected_01 = '''
            {2,3}_001:T_002
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0021(self):

        spec01           = '''
            {2,3}_001:*_002
            *_002:T_003
        '''
        spec_expected_01 = '''
            {2,3}_001:*_002
            *_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0021(self):

        spec01           = '''
            {2,3}_001:+_002
            +_002:T_003
        '''
        spec_expected_01 = '''
            {2,3}_001:+_002
            +_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0021a(self):

        spec01           = '''
            {2,3}_001:?_002
            ?_002:T_003
        '''
        spec_expected_01 = '''
            {2,3}_001:?_002
            ?_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0021b(self):

        spec01           = '''
            {2,3}_001:{0,3}_002
            {0,3}_002:T_003
        '''
        spec_expected_01 = '''
            {2,3}_001:{0,3}_002
            {0,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0021c(self):

        spec01           = '''
            {2,3}_001:{1,3}_002
            {1,3}_002:T_003
        '''
        spec_expected_01 = '''
            {2,3}_001:{1,3}_002
            {1,3}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0021d(self):

        spec01           = '''
            {2,3}_001:{2,4}_002
            {2,4}_002:T_003
        '''
        spec_expected_01 = '''
            {2,3}_001:{2,4}_002
            {2,4}_002:T_003
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0022(self):

        spec01           = '''
            *_001:E_002
        '''
        spec_expected_01 = '''
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0022b(self):

        spec01           = '''
            *_001:T_002
        '''
        spec_expected_01 = '''
            *_001:T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0023(self):

        spec01           = '''
            *_001:S_002
            S_002:E_003
        '''
        spec_expected_01 = '''
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0024(self):

        spec01           = '''
            *_001:S_002
            S_002:T_003
        '''
        spec_expected_01 = '''
            *_001:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0025(self):

        spec01           = '''
            *_001:?_002
            ?_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0026(self):

        spec01           = '''
            *_001:{0,2}_002
            {0,2}_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0027(self):

        spec01           = '''
            *_001:{1,2}_002
            {1,2}_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0028(self):

        spec01           = '''
            *_001:{2,4}_002
            {2,4}_002:T_003
        '''
        spec_expected_01 = '''
            *_001:{2,4}_002
            {2,4}_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0029(self):

        spec01           = '''
            *_001:*_002
            *_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0030(self):

        spec01           = '''
            *_001:+_002
            +_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0031(self):

        spec01           = '''
            *_001:+_002
            +_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0032(self):

        spec01           = '''
            +_001:E_002
        '''
        spec_expected_01 = '''
        '''
        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0033(self):

        spec01           = '''
            +_001:T_002
        '''
        spec_expected_01 = '''
            +_001:T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0034(self):

        spec01           = '''
            +_001:S_002
            S_002:E_003
        '''
        spec_expected_01 = '''
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0035(self):

        spec01           = '''
            +_001:S_002
            S_002:T_003
        '''
        spec_expected_01 = '''
            +_001:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0036(self):

        spec01           = '''
            +_001:?_002
            ?_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0037(self):

        spec01           = '''
            +_001:{0,2}_002
            {0,2}_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0038(self):

        spec01           = '''
            +_001:{1,2}_002
            {1,2}_002:T_003
        '''
        spec_expected_01 = '''
            +_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )



    def test_0039(self):

        spec01           = '''
            +_001:{2,4}_002
            {2,4}_002:T_003
        '''
        spec_expected_01 = '''
            +_001:{2,4}_002
            {2,4}_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0040(self):

        spec01           = '''
            +_001:*_002
            *_002:T_003
        '''
        spec_expected_01 = '''
            *_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0041(self):

        spec01           = '''
            +_001:+_002
            +_002:T_003
        '''
        spec_expected_01 = '''
            +_002:T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.clean_epsilon()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )





if __name__ == '__main__':
    unittest.main()
