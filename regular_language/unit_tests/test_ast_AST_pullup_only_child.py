#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.pullup_only_child() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_pullup_only_child( unittest.TestCase ):

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
        node_spec01      = 'S_001'
        node_spec02      = 'E_002'
        spec_expected_01 = 'E_002'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0002(self):

        spec01           = '''
            S_001:S_002
            S_002:T_003
        '''

        node_spec01      = 'S_001'
        node_spec02      = 'S_002'
        spec_expected_01 = 'S_002:T_003'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)

        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0003(self):

        spec01           = '''
            S_001:S_002
            S_002:T_003 T_004 T_005
        '''

        node_spec01      = 'S_001'
        node_spec02      = 'S_002'
        spec_expected_01 = 'S_002:T_003 T_004 T_005'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)

        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0004(self):

        spec01           = '''
            S_001:S_002
            S_002:|_003 +_004 ?_005
            |_003:T_006 T_007 T_008
            +_004:T_009 T_010 T_011
            ?_005:T_012 E_013 T_014
        '''

        node_spec01      = 'S_001'
        node_spec02      = 'S_002'
        spec_expected_01 = '''
            S_002:|_003 +_004 ?_005
            |_003:T_006 T_007 T_008
            +_004:T_009 T_010 T_011
            ?_005:T_012 E_013 T_014
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)

        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0005(self):


        spec01           = '''
            S_001:S_002
            S_002:E_003
        '''
        node_spec01      = 'S_002'
        node_spec02      = 'E_003'
        spec_expected_01 = '''
            S_001:E_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0006(self):


        spec01           = '''
            S_001:S_002
            S_002:S_003
            S_003:T_004
        '''

        node_spec01      = 'S_002'
        node_spec02      = 'S_003'
        spec_expected_01 = '''
            S_001:S_003
            S_003:T_004
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0007(self):


        spec01           = '''
            S_001:S_002
            S_002:S_003
            S_003:T_004 T_005 T_006
        '''

        node_spec01      = 'S_002'
        node_spec02      = 'S_003'
        spec_expected_01 = '''
            S_001:S_003
            S_003:T_004 T_005 T_006
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0008(self):


        spec01           = '''
            S_001:S_002
            S_002:S_003
            S_003:|_004 +_005 ?_006
            |_004:T_007 T_008 T_009
            +_005:T_010 T_011 T_012
            ?_006:T_013 E_014 T_015
        '''

        node_spec01      = 'S_002'
        node_spec02      = 'S_003'
        spec_expected_01 = '''
            S_001:S_003
            S_003:|_004 +_005 ?_006
            |_004:T_007 T_008 T_009
            +_005:T_010 T_011 T_012
            ?_006:T_013 E_014 T_015
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0009(self):

        spec01           = '''
            S_001:T_002 S_003 T_004
            S_003:S_004
            S_004:|_005 +_006 ?_007
            |_005:T_008 T_009 T_010
            +_006:T_011 T_012 T_013
            ?_007:T_014 E_015 T_016
        '''

        node_spec01      = 'S_003'
        node_spec02      = 'S_004'

        spec_expected_01 = '''
            S_001:T_002 S_004 T_004
            S_004:|_005 +_006 ?_007
            |_005:T_008 T_009 T_010
            +_006:T_011 T_012 T_013
            ?_007:T_014 E_015 T_016
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0010(self):

        spec01           = '''
            S_001:S_003 T_002 T_004
            S_003:S_004
            S_004:|_005 +_006 ?_007
            |_005:T_008 T_009 T_010
            +_006:T_011 T_012 T_013
            ?_007:T_014 E_015 T_016
        '''

        node_spec01      = 'S_003'
        node_spec02      = 'S_004'

        spec_expected_01 = '''
            S_001:S_004 T_002 T_004
            S_004:|_005 +_006 ?_007
            |_005:T_008 T_009 T_010
            +_006:T_011 T_012 T_013
            ?_007:T_014 E_015 T_016
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0011(self):

        spec01           = '''
            S_001:T_002 T_004 S_003
            S_003:S_004
            S_004:|_005 +_006 ?_007
            |_005:T_008 T_009 T_010
            +_006:T_011 T_012 T_013
            ?_007:T_014 E_015 T_016
        '''

        node_spec01      = 'S_003'
        node_spec02      = 'S_004'

        spec_expected_01 = '''
            S_001:T_002 T_004 S_004
            S_004:|_005 +_006 ?_007
            |_005:T_008 T_009 T_010
            +_006:T_011 T_012 T_013
            ?_007:T_014 E_015 T_016
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )


    def test_0012(self):

        spec01           = '''
            |_020:T_021 S_001 T_022
            S_001:T_002 S_003 T_004
            S_003:S_005
            S_005:|_006 +_007 ?_008
            |_006:T_009 T_010 T_011
            +_007:T_012 T_013 T_014
            ?_008:T_015 E_016 T_017
        '''

        node_spec01      = 'S_003'
        node_spec02      = 'S_005'

        spec_expected_01 = '''
            |_020:T_021 S_001 T_022
            S_001:T_002 S_005 T_004
            S_005:|_006 +_007 ?_008
            |_006:T_009 T_010 T_011
            +_007:T_012 T_013 T_014
            ?_008:T_015 E_016 T_017
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        node02 = self.helper.get_node(ast01, node_spec02)

        node01.append_out_token_pre ('token01')
        node01.append_out_token_post('token02')

        node02.append_out_token_pre ('token03')
        node02.append_out_token_post('token04')

        ast01.pullup_only_child(node01)
        spec02 = self.display_tree(ast01)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )
        self.assertEqual( len(node01.out_token_pre),  2 )
        self.assertEqual( node01.out_token_pre[0],   'token03' )
        self.assertEqual( node01.out_token_pre[1],   'token01' )
        self.assertEqual( len(node01.out_token_post), 2 )
        self.assertEqual( node01.out_token_post[0],  'token04' )
        self.assertEqual( node01.out_token_post[1],  'token02' )




if __name__ == '__main__':
    unittest.main()
