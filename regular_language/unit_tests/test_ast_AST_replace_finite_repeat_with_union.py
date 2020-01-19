#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.replace_finite_repeat_with_union() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_replace_finite_repeat_with_union( unittest.TestCase ):

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
        spec_expected_01 = ''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0001a(self):

        spec01           = 'T_001'
        spec_expected_01 = 'T_001'

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0002(self):

        spec01           = 'E_001'
        spec_expected_01 = ''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0003(self):

        spec01           = '?_001:T_001'
        spec_expected_01 = '?_001:T_001'

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0004(self):

        spec01           = '''
            {0,2}_001:T_002
        '''

        spec_expected_01 = '''
            ?_001:|_???
            |_???:T_002 S_???
            S_???:T_002 T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0004(self):

        spec01           = '''
            {0,3}_001:T_002
        '''

        spec_expected_01 = '''
            ?_001:|_???
            |_???:T_002 S_??? S_???
            S_???:T_002 T_002
            S_???:T_002 T_002 T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0005(self):

        spec01           = '''
            {1,2}_001:T_002
        '''

        spec_expected_01 = '''
            |_???:T_002 S_???
            S_???:T_002 T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0006(self):

        spec01           = '''
            {1,3}_001:T_002
        '''

        spec_expected_01 = '''
            |_???:T_002 S_??? S_???
            S_???:T_002 T_002
            S_???:T_002 T_002 T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0007(self):

        spec01           = '''
            {0,0}_001:T_002
        '''

        spec_expected_01 = '''
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0008(self):

        spec01           = '''
            ?_001:T_002
        '''

        spec_expected_01 = '''
            ?_001:T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0009(self):

        spec01           = '''
            {2,2}_001:T_002
        '''

        spec_expected_01 = '''
            S_???:T_002 T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0010(self):

        spec01           = '''
            {5,5}_001:T_002
        '''

        spec_expected_01 = '''
            S_???:T_002 T_002 T_002 T_002 T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0011(self):

        spec01           = '''
            {3,6}_001:T_002
        '''

        spec_expected_01 = '''
            |_???:S_??? S_??? S_??? S_???
            S_???:T_002 T_002 T_002 
            S_???:T_002 T_002 T_002 T_002
            S_???:T_002 T_002 T_002 T_002 T_002
            S_???:T_002 T_002 T_002 T_002 T_002 T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.replace_finite_repeat_with_union()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )






if __name__ == '__main__':
    unittest.main()
