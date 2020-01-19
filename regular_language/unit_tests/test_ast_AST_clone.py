#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.clone() """


import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_clone( unittest.TestCase ):

    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.helper = test_AST_helper()


    def construct_ast_from_spec( self, spec01 ):
        return self.helper.construct_ast_from_spec(spec01)


    def display_tree( self, ast01 ):
        return self.helper.display_tree(ast01)


    def compare_specs( self, spec01, spec02 ):
        return self.helper.compare_specs( spec01, spec02 )



    def test_clone_0001(self):

        spec01 = ''
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0002(self):

        spec01 = 'T_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0002(self):

        spec01 = 'N_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0003(self):

        spec01 = 'E_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0004(self):

        spec01 = 'S_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0005(self):

        spec01 = '|_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0006(self):

        spec01 = '*_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0007(self):

        spec01 = '+_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0008(self):

        spec01 = '{2,3}_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0009(self):

        spec01 = '?_001'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0010(self):

        spec01 = 'S_001:T_002'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0011(self):

        spec01 = 'S_001:T_002 T_003'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0012(self):

        spec01 = 'S_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0013(self):

        spec01 = 'S_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0014(self):

        spec01 = 'S_001:N_002 N_003 N_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0015(self):

        spec01 = 'S_001:E_002 E_003 E_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0016(self):

        spec01 = 'S_001:|_002 |_003 |_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0017(self):

        spec01 = 'S_001:*_002 *_003 *_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0018(self):

        spec01 = 'S_001:+_002 +_003 +_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0019(self):

        spec01 = 'S_001:?_002 ?_003 ?_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0020(self):

        spec01 = 'S_001:{1,2}_002 {2,3}_003 {123,456}_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0021(self):

        spec01 = '|_001:T_002'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0022(self):

        spec01 = '|_001:T_002 T_003'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0023(self):

        spec01 = '|_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0024(self):

        spec01 = '|_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0025(self):

        spec01 = '|_001:N_002 N_003 N_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0026(self):

        spec01 = '|_001:E_002 E_003 E_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0027(self):

        spec01 = '|_001:|_002 |_003 |_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0028(self):

        spec01 = '|_001:*_002 *_003 *_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0029(self):

        spec01 = '|_001:+_002 +_003 +_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0030(self):

        spec01 = '|_001:?_002 ?_003 ?_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0031(self):

        spec01 = '|_001:{1,2}_002 {2,3}_003 {123,456}_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0032(self):

        spec01 = '*_001:T_002'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0033(self):

        spec01 = '*_001:T_002 T_003'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0034(self):

        spec01 = '*_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0035(self):

        spec01 = '*_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0036(self):

        spec01 = '*_001:N_002 N_003 N_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0037(self):

        spec01 = '*_001:E_002 E_003 E_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0038(self):

        spec01 = '*_001:|_002 |_003 |_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0039(self):

        spec01 = '*_001:*_002 *_003 *_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0040(self):

        spec01 = '*_001:+_002 +_003 +_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0041(self):

        spec01 = '*_001:?_002 ?_003 ?_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0042(self):

        spec01 = '*_001:{1,2}_002 {2,3}_003 {123,456}_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0043(self):

        spec01 = '+_001:T_002'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0044(self):

        spec01 = '+_001:T_002 T_003'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0045(self):

        spec01 = '+_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0046(self):

        spec01 = '+_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0047(self):

        spec01 = '+_001:N_002 N_003 N_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0048(self):

        spec01 = '+_001:E_002 E_003 E_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0049(self):

        spec01 = '+_001:|_002 |_003 |_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0050(self):

        spec01 = '+_001:*_002 *_003 *_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0051(self):

        spec01 = '+_001:+_002 +_003 +_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0052(self):

        spec01 = '+_001:?_002 ?_003 ?_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0053(self):

        spec01 = '+_001:{1,2}_002 {2,3}_003 {123,456}_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0054(self):

        spec01 = '?_001:T_002'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0055(self):

        spec01 = '?_001:T_002 T_003'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0056(self):

        spec01 = '?_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0057(self):

        spec01 = '?_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0058(self):

        spec01 = '?_001:N_002 N_003 N_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0059(self):

        spec01 = '?_001:E_002 E_003 E_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0060(self):

        spec01 = '?_001:|_002 |_003 |_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0061(self):

        spec01 = '?_001:*_002 *_003 *_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0062(self):

        spec01 = '?_001:+_002 +_003 +_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0063(self):

        spec01 = '?_001:?_002 ?_003 ?_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0064(self):

        spec01 = '?_001:{1,2}_002 {2,3}_003 {123,456}_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0065(self):

        spec01 = '{2,3}_001:T_002'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0066(self):

        spec01 = '{2,3}_001:T_002 T_003'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0067(self):

        spec01 = '{2,3}_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0068(self):

        spec01 = '{2,3}_001:T_002 T_003 T_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0069(self):

        spec01 = '{2,3}_001:N_002 N_003 N_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0070(self):

        spec01 = '{2,3}_001:E_002 E_003 E_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0071(self):

        spec01 = '{2,3}_001:|_002 |_003 |_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0072(self):

        spec01 = '{2,3}_001:*_002 *_003 *_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0073(self):

        spec01 = '{2,3}_001:+_002 +_003 +_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0074(self):

        spec01 = '{2,3}_001:?_002 ?_003 ?_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0075(self):

        spec01 = '{2,3}_001:{1,2}_002 {2,3}_003 {123,456}_004'
        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )


    def test_clone_0076(self):

        spec01 = '''
            S_001:S_002 |_003 S_004 |_005
            S_002:E_006 *_007 +_008 ?_009
            |_003:E_010 *_011 +_012 {2,3}_013
            |_005:T_025 T_026 E_027
            *_007:T_014 T_015
            ?_009:T_016 T_017
            *_011:T_018 T_019
            +_012:T_020 T_021
            {2,3}_013:T_022 T_023 E_024
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        ast02 = ast01.clone()
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec01, spec02), True )



if __name__ == '__main__':
    unittest.main()
