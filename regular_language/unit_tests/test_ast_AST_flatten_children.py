#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.flatten_children() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_flatten_children( unittest.TestCase ):

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
        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0002(self):

        spec01           = 'E_001'
        spec_expected_01 = 'E_001'

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0003(self):

        spec01           = 'T_001'
        spec_expected_01 = 'T_001'

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0004(self):

        spec01           = '''
            S_001:T_002 S_003
            S_003:T_004 T_005
        '''

        spec_expected_01 = '''
            S_001:T_002 T_004 T_005
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0005(self):

        spec01           = '''
            S_001:T_002 S_003
            S_003:T_004 T_005
        '''

        spec_expected_01 = '''
            S_001:T_002 S_003
            S_003:T_004 T_005
        '''


        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, 'S_003')
        node01.append_out_token_pre  ('token01')
        node01.append_out_token_post ('token02')

        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0006(self):

        spec01           = '''
            S_001:T_002 S_003
            S_003:T_004 T_005
        '''

        spec_expected_01 = '''
            S_001:T_002 T_004 T_005
        '''


        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, 'S_001')
        node01.append_out_token_pre  ('token01')
        node01.append_out_token_post ('token02')


        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )

        self.assertEqual( len(node01.out_token_pre),  1         )
        self.assertEqual( node01.out_token_pre[0],    'token01' )
        self.assertEqual( len(node01.out_token_post), 1         )
        self.assertEqual( node01.out_token_post[0],   'token02' )


    def test_0006(self):

        spec01           = '''
            S_001:T_002 S_003
            S_003:T_004 T_005
        '''

        spec_expected_01 = '''
            S_001:T_002 T_004 T_005
        '''


        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, 'S_001')
        node01.append_out_token_pre  ('token01')
        node01.append_out_token_post ('token02')


        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )

        self.assertEqual( len(node01.out_token_pre),  1         )
        self.assertEqual( node01.out_token_pre[0],    'token01' )
        self.assertEqual( len(node01.out_token_post), 1         )
        self.assertEqual( node01.out_token_post[0],   'token02' )


    def test_0007(self):

        spec01           = '''
            S_001:S_002 T_003
            S_002:T_004 T_005
        '''

        spec_expected_01 = '''
            S_001:T_004 T_005 T_003
        '''


        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, 'S_001')
        node01.append_out_token_pre  ('token01')
        node01.append_out_token_post ('token02')


        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )

        self.assertEqual( len(node01.out_token_pre),  1         )
        self.assertEqual( node01.out_token_pre[0],    'token01' )
        self.assertEqual( len(node01.out_token_post), 1         )
        self.assertEqual( node01.out_token_post[0],   'token02' )


    def test_0008(self):

        spec01           = '''
            S_001:S_002 T_003
            S_002:T_004 S_005 S_006 T_007
            S_005:T_008 T_009
            S_006:T_010 T_011
        '''

        spec_expected_01 = '''
            S_001:T_004 T_008 T_009 T_010 T_011 T_007 T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, 'S_001')
        node01.append_out_token_pre  ('token01')
        node01.append_out_token_post ('token02')


        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )

        self.assertEqual( len(node01.out_token_pre),  1         )
        self.assertEqual( node01.out_token_pre[0],    'token01' )
        self.assertEqual( len(node01.out_token_post), 1         )
        self.assertEqual( node01.out_token_post[0],   'token02' )


    def test_0009(self):

        spec01           = '''
            |_001:|_002 T_003
            |_002:T_004 |_005 |_006 T_007
            |_005:T_008 T_009
            |_006:T_010 T_011
        '''

        spec_expected_01 = '''
            |_001:T_004 T_008 T_009 T_010 T_011 T_007 T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, '|_001')
        node01.append_out_token_pre  ('token01')
        node01.append_out_token_post ('token02')


        ast01.flatten_children()
        spec02 = self.display_tree(ast01)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )

        self.assertEqual( len(node01.out_token_pre),  1         )
        self.assertEqual( node01.out_token_pre[0],    'token01' )
        self.assertEqual( len(node01.out_token_post), 1         )
        self.assertEqual( node01.out_token_post[0],   'token02' )




if __name__ == '__main__':
    unittest.main()
