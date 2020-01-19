#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.AST.clone_subtree() """

import unittest
import nlpregex.regular_language.ast

from  nlpregex.regular_language.unit_tests.test_ast_helper import test_AST_helper

class test_ast_AST_clone_subtree( unittest.TestCase ):

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

        spec01           = 'T_001'
        node_spec01      = 'T_001'
        spec_expected_01 = 'T_001'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0002(self):

        spec01           = 'N_001'
        node_spec01      = 'N_001'
        spec_expected_01 = 'N_001'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0003(self):

        spec01           = 'E_001'
        node_spec01      = 'E_001'
        spec_expected_01 = 'E_001'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0004(self):

        spec01           = 'S_001:T_001'
        node_spec01      = 'T_001'
        spec_expected_01 = 'T_001'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0005(self):

        spec01           = 'S_001:T_001'
        node_spec01      = 'S_001'
        spec_expected_01 = 'S_001:T_001'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0006(self):

        spec01           = 'S_001:T_001 T_002'
        node_spec01      = 'S_001'
        spec_expected_01 = 'S_001:T_001 T_002'

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
       
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0007(self):

        spec01           = '''
            S_001:T_001 |_002
            |_002:T_003 T_004
        '''

        node_spec01      = 'S_001'

        spec_expected_01 = '''
            S_001:T_001 |_002
            |_002:T_003 T_004
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)

        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0008(self):

        spec01           = '''
            S_001:T_001 |_002
            |_002:T_003 T_004
        '''

        node_spec01      = '|_002'

        spec_expected_01 = '''
            |_002:T_003 T_004
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)

        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0009(self):

        spec01           = '''
            S_001:T_001 |_002
            |_002:T_003 T_004
        '''

        node_spec01      = 'T_001'

        spec_expected_01 = '''
            T_001
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0010(self):

        spec01           = '''
            S_001:T_001 |_002
            |_002:T_003 T_004
        '''

        node_spec01      = 'T_003'

        spec_expected_01 = '''
            T_003
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0011(self):

        spec01           = '''
            S_001:T_001 |_002
            |_002:T_003 T_004
        '''

        node_spec01      = 'T_004'

        spec_expected_01 = '''
            T_004
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0012(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_001'

        spec_expected_01 = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0013(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_002'

        spec_expected_01 = '''
            T_002
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0014(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = '|_003'

        spec_expected_01 = '''
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0015(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_004'

        spec_expected_01 = '''
            T_004
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0016(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_005'

        spec_expected_01 = '''
            S_005:?_008 T_009 +_010
            ?_008:S_016
            +_010:S_017
            S_016:T_020 T_021
            S_017:E_022 T_023
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0017(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_006'

        spec_expected_01 = '''
            S_006:{2,3}_011 *_012 T_013
            {2,3}_011:S_018
            *_012:S_019
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0018(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_007'

        spec_expected_01 = '''
            S_007:T_014 T_015
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0019(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = '?_008'

        spec_expected_01 = '''
            ?_008:S_016
            S_016:T_020 T_021
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0020(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = '+_010'

        spec_expected_01 = '''
            +_010:S_017
            S_017:E_022 T_023
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0021(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = '{2,3}_011'

        spec_expected_01 = '''
            {2,3}_011:S_018
            S_018:T_024 T_025
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0022(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = '*_012'

        spec_expected_01 = '''
            *_012:S_019
            S_019:T_026 E_027
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0023(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_013'

        spec_expected_01 = '''
            T_013
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0024(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_014'

        spec_expected_01 = '''
            T_014
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0025(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_015'

        spec_expected_01 = '''
            T_015
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0026(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_016'

        spec_expected_01 = '''
            S_016:T_020 T_021
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0027(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_017'

        spec_expected_01 = '''
            S_017:E_022 T_023
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0028(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_018'

        spec_expected_01 = '''
            S_018:T_024 T_025
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0029(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'S_019'

        spec_expected_01 = '''
            S_019:T_026 E_027
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0030(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_020'

        spec_expected_01 = '''
            T_020
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0031(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_021'

        spec_expected_01 = '''
            T_021
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0032(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'E_022'

        spec_expected_01 = '''
            E_022
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0033(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_023'

        spec_expected_01 = '''
            T_023
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0034(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_024'

        spec_expected_01 = '''
            T_024
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0035(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_025'

        spec_expected_01 = '''
            T_025
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0036(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'T_026'

        spec_expected_01 = '''
            T_026
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )


    def test_0037(self):

        spec01           = '''
            S_001:T_002 |_003 T_004
            |_003:S_005 S_006 S_007
            S_005:?_008 T_009 +_010
            S_006:{2,3}_011 *_012 T_013
            S_007:T_014 T_015
            ?_008:S_016
            +_010:S_017
            {2,3}_011:S_018
            *_012:S_019
            S_016:T_020 T_021
            S_017:E_022 T_023
            S_018:T_024 T_025
            S_019:T_026 E_027
        '''

        node_spec01      = 'E_027'

        spec_expected_01 = '''
            E_027
        '''

        ast01  = self.construct_ast_from_spec(spec01)
        node01 = self.helper.get_node(ast01, node_spec01)
        ast02  = ast01.clone_subtree(node01)
        spec02 = self.display_tree(ast02)
        self.assertEqual( self.compare_specs(spec_expected_01, spec02), True )



if __name__ == '__main__':
    unittest.main()
