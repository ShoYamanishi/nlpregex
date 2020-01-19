#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.expand_nonterminals() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_expand_nonterminals( unittest.TestCase ):

    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.helper = test_AST_helper()


    def construct_ast_from_spec( self, spec01 ):
        return self.helper.construct_ast_from_spec(spec01)


    def display_tree( self, ast01 ):
        return self.helper.display_tree(ast01)


    def compare_specs( self, spec01, spec02 ):
        return self.helper.compare_specs( spec01, spec02 )


    def test_find_dependent_nonterminals_0001(self):

        spec01           = ''

        ast01 = self.construct_ast_from_spec(spec01)
        set01 = ast01.find_dependent_nonterminals()
        set02 = set()
        self.assertEqual( set01, set02 )


    def test_find_dependent_nonterminals_0002(self):

        spec01           = 'N_001'

        ast01 = self.construct_ast_from_spec(spec01)
        set01 = ast01.find_dependent_nonterminals()
        set02 = set()
        set02.add('001')
        self.assertEqual( set01, set02 )


    def test_find_dependent_nonterminals_0003(self):

        spec01           = '''
           S_001:N_001 N_002
        '''
        ast01 = self.construct_ast_from_spec(spec01)
        set01 = ast01.find_dependent_nonterminals()
        set02 = set()
        set02.add('001')
        set02.add('002')
        self.assertEqual( set01, set02 )


    def test_find_dependent_nonterminals_0004(self):

        spec01           = '''
           S_001:N_001 |_002 ?_003
           |_002:N_004 N_005
           ?_003:S_006
           S_006:N_007 N_008

        '''
        ast01 = self.construct_ast_from_spec(spec01)
        set01 = ast01.find_dependent_nonterminals()
        set02 = set()
        set02.add('001')
        set02.add('004')
        set02.add('005')
        set02.add('007')
        set02.add('008')
        self.assertEqual( set01, set02 )


    def test_expand_nonterminals_0001(self):

        spec01           = '''
            N_001
        '''

        spec02           = '''
            N_101
        '''

        spec_expected    = '''
            N_101
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_001')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')


        ast02 = self.construct_ast_from_spec(spec02)
        node_101 = self.helper.get_node(ast02, 'N_101')
        node_101.append_out_token_pre ('token03')
        node_101.append_out_token_post('token04')

        ASTs = {}
        ASTs['top'] = ast01
        ASTs['001'] = ast02

        nonterminals = ['001']

        ast01.expand_nonterminals( nonterminals, ASTs )
        
        spec03 = self.display_tree(ast01)
        
        self.assertEqual( self.compare_specs(spec_expected, spec03), True )
        node_101 = self.helper.get_node(ast01, 'N_101')
        self.assertEqual( len(node_101.out_token_pre ), 2 )
        self.assertEqual( node_101.out_token_pre[0],  'token03' )
        self.assertEqual( node_101.out_token_pre[1],  'token01' )
        self.assertEqual( len(node_101.out_token_post), 2 )
        self.assertEqual( node_101.out_token_post[0], 'token04' )
        self.assertEqual( node_101.out_token_post[1], 'token02' )


    def test_expand_nonterminals_0002(self):
        pass # removed


    def test_expand_nonterminals_0003(self):

        spec01           = '''
            N_001
        '''

        spec02           = '''
            N_101
        '''

        spec03           = '''
            N_201
        '''

        spec04           = '''
            N_301
        '''


        spec_expected    = '''
            N_301
        '''


        ast01 = self.construct_ast_from_spec(spec01)
        node_001 = self.helper.get_node(ast01, 'N_001')
        node_001.append_out_token_pre ('token01')
        node_001.append_out_token_post('token02')

        ast02 = self.construct_ast_from_spec(spec02)
        node_101 = self.helper.get_node(ast02, 'N_101')
        node_101.append_out_token_pre ('token03')
        node_101.append_out_token_post('token04')

        ast03 = self.construct_ast_from_spec(spec03)
        node_201 = self.helper.get_node(ast03, 'N_201')
        node_201.append_out_token_pre ('token05')
        node_201.append_out_token_post('token06')

        ast04 = self.construct_ast_from_spec(spec04)
        node_301 = self.helper.get_node(ast04, 'N_301')
        node_301.append_out_token_pre ('token07')
        node_301.append_out_token_post('token08')

        ASTs = {}
        ASTs['top'] = ast01
        ASTs['001'] = ast02
        ASTs['101'] = ast03
        ASTs['201'] = ast04

        nonterminals = ['001', '101', '201']

        ast01.expand_nonterminals( nonterminals, ASTs )
        node_301 = self.helper.get_node(ast01, 'N_301')
        
        spec05 = self.display_tree(ast01)
        
        self.assertEqual( self.compare_specs(spec_expected, spec05), True )

        self.assertEqual( len(node_301.out_token_pre ), 4 )
        self.assertEqual( node_301.out_token_pre[0],  'token07' )
        self.assertEqual( node_301.out_token_pre[1],  'token05' )
        self.assertEqual( node_301.out_token_pre[2],  'token03' )
        self.assertEqual( node_301.out_token_pre[3],  'token01' )
        self.assertEqual( len(node_301.out_token_post), 4 )
        self.assertEqual( node_301.out_token_post[0], 'token08' )
        self.assertEqual( node_301.out_token_post[1], 'token06' )
        self.assertEqual( node_301.out_token_post[2], 'token04' )
        self.assertEqual( node_301.out_token_post[3], 'token02' )



    def test_expand_nonterminals_0004(self):

        # TOP
        spec01           = '''
            |_001:T_002 T_003 N_004 S_005
            S_005:N_006 N_007
        '''

        # N_004
        spec02           = '''   
            S_101:N_102 T_103 T_105 S_106
            S_106:T_108 T_109
        '''

        # N_006
        spec03           = '''
            |_201:T_202 T_203 T_204
        '''

        # N_007
        spec04           = '''
            S_301:T_302 T_303
        '''

        # N_102
        spec05           = '''
            S_401:T_402 T_403
        '''

        spec_expected    = '''
            |_001:T_002 T_003 S_101 S_005
            S_005:|_201 S_301
            S_101:S_401 T_103 T_105 S_106
            S_106:T_108 T_109
            |_201:T_202 T_203 T_204
            S_301:T_302 T_303
            S_401:T_402 T_403
        '''

        ast01 = self.construct_ast_from_spec(spec01)
        node_004 = self.helper.get_node(ast01, 'N_004')
        node_004.append_out_token_pre ('token01')
        node_004.append_out_token_post('token02')

        node_006 = self.helper.get_node(ast01, 'N_006')
        node_006.append_out_token_pre ('token03')
        node_006.append_out_token_post('token04')

        node_007 = self.helper.get_node(ast01, 'N_007')
        node_007.append_out_token_pre ('token05')
        node_007.append_out_token_post('token06')

        ast02 = self.construct_ast_from_spec(spec02)
        node_101 = self.helper.get_node(ast02, 'S_101')
        node_101.append_out_token_pre ('token07')
        node_101.append_out_token_post('token08')

        node_102 = self.helper.get_node(ast02, 'N_102')
        node_102.append_out_token_pre ('token09')
        node_102.append_out_token_post('token10')


        ast03 = self.construct_ast_from_spec(spec03)
        node_201 = self.helper.get_node(ast03, '|_201')
        node_201.append_out_token_pre ('token11')
        node_201.append_out_token_post('token12')

        ast04 = self.construct_ast_from_spec(spec04)
        node_301 = self.helper.get_node(ast04, 'S_301')
        node_301.append_out_token_pre ('token13')
        node_301.append_out_token_post('token14')

        ast05 = self.construct_ast_from_spec(spec05)
        node_401 = self.helper.get_node(ast05, 'S_401')
        node_401.append_out_token_pre ('token15')
        node_401.append_out_token_post('token16')


        ASTs = {}
        ASTs['top'] = ast01
        ASTs['004'] = ast02
        ASTs['006'] = ast03
        ASTs['007'] = ast04
        ASTs['102'] = ast05

        nonterminals = ['004', '006', '007', '102']

        ast01.expand_nonterminals( nonterminals, ASTs )
        node_101 = self.helper.get_node(ast01, 'S_101')
        node_201 = self.helper.get_node(ast01, '|_201')
        node_301 = self.helper.get_node(ast01, 'S_301')
        node_401 = self.helper.get_node(ast01, 'S_401')

        
        spec05 = self.display_tree(ast01)
        
        self.assertEqual( self.compare_specs(spec_expected, spec05), True )

        self.assertEqual( len(node_401.out_token_pre ), 2 )
        self.assertEqual( node_401.out_token_pre[0],  'token15' )
        self.assertEqual( node_401.out_token_pre[1],  'token09' )
        self.assertEqual( len(node_401.out_token_post), 2 )
        self.assertEqual( node_401.out_token_post[0], 'token16' )
        self.assertEqual( node_401.out_token_post[1], 'token10' )

        self.assertEqual( len(node_301.out_token_pre ), 2 )
        self.assertEqual( node_301.out_token_pre[0],  'token13' )
        self.assertEqual( node_301.out_token_pre[1],  'token05' )
        self.assertEqual( len(node_301.out_token_post), 2 )
        self.assertEqual( node_301.out_token_post[0], 'token14' )
        self.assertEqual( node_301.out_token_post[1], 'token06' )

        self.assertEqual( len(node_201.out_token_pre ), 2 )
        self.assertEqual( node_201.out_token_pre[0],  'token11' )
        self.assertEqual( node_201.out_token_pre[1],  'token03' )
        self.assertEqual( len(node_201.out_token_post), 2 )
        self.assertEqual( node_201.out_token_post[0], 'token12' )
        self.assertEqual( node_201.out_token_post[1], 'token04' )

        self.assertEqual( len(node_101.out_token_pre ), 2 )
        self.assertEqual( node_101.out_token_pre[0],  'token07' )
        self.assertEqual( node_101.out_token_pre[1],  'token01' )
        self.assertEqual( len(node_101.out_token_post), 2 )
        self.assertEqual( node_101.out_token_post[0], 'token08' )
        self.assertEqual( node_101.out_token_post[1], 'token02' )



if __name__ == '__main__':
    unittest.main()
