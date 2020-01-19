#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for common_subtree_reducer.py."""

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.sse_forrest
import nlpregex.regular_language.common_subtree_reducer

from nlpregex.regular_language.unit_tests.test_sse_asforrest_helper import test_sse_ASForrest_helper

class test_CommonSubtreeReducer( unittest.TestCase ):


    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.helper = test_sse_ASForrest_helper()


    def create_initial_serial_node( self, forrest, children ):

       if len( children ) == 0:
           return forrest.create_initial_node('e')

       if len( children )== 1:
           return forrest.create_initial_node( children[0] )

       r = forrest.create_initial_node('s' )

       for c in children:
           n = forrest.create_initial_node( c )
           e = nlpregex.regular_language.sse_forrest.sseASTEdge()
           e.add_to_graph( forrest, r, n, "directed" )

       r.generate_regex()

       return  r


    def add_question_node( self, forrest, n ):

       r = forrest.create_initial_node('?' )

       e = nlpregex.regular_language.sse_forrest.sseASTEdge()
       e.add_to_graph( forrest, r, n, "directed" )
       r.generate_regex()

       return  r


    def test_constructor_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )


        self.assertEqual( len(reducer01.map_regex_to_node_list), 0 )
        self.assertEqual( reducer01.min_num_subtrees,            2 )
        self.assertEqual( reducer01.min_num_terms,               2 )


    def test_find_best_common_subtree_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            E_0
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.visit_and_find_common_subtrees( root01 )
 
#        print (reducer01.map_regex_to_node_list)


    def test_find_best_common_subtree_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 T4_4
            |_2:T3_5 T4_6
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.visit_and_find_common_subtrees( root01 )
        regex01 = reducer01.find_best_common_subtree()
#        print (reducer01.map_regex_to_node_list)
#        print ( regex01 )
        self.assertEqual( regex01, '( t3 | t4 )' ) 


    def test_find_best_common_subtree_0003( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 S_4
            |_2:T3_5 S_6
            S_4:T7_7 T8_8
            S_6:T7_9 T8_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.visit_and_find_common_subtrees( root01 )
        regex01 = reducer01.find_best_common_subtree()
#        print ( regex01 )
#        print (reducer01.map_regex_to_node_list)
        self.assertEqual( regex01, '( t3 | t7 t8 )' ) 


    def test_find_best_common_subtree_0004( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1 S_2
            S_1:|_3 |_4 |_5
            S_2:|_6 |_7
            |_3:T1_8 S_9
            S_9:T2_10 T3_11
            |_4:T4_12 S_13
            S_13:T5_14 T6_15
            |_5:T1_16 S_17
            S_17:T2_18 T3_19
            |_6:T1_20 S_21
            S_21:T2_22 T3_23
            |_7:T4_24 S_25
            S_25:T5_26 T6_27
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )
        ast00 = self.helper.get_node( forrest01, 1)
        ast01 = self.helper.get_node( forrest01, 2)

        root01.children_map['n0'] = ast00
        root01.children_map['n1'] = ast01

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.visit_and_find_common_subtrees( root01 )
        regex01 = reducer01.find_best_common_subtree()
#        print(regex01)
        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
        '''


    def test_replace_subtree_with_nonterminal_and_place_under_root_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 S_4
            |_2:T3_5 S_6
            S_4:T7_7 T8_8
            S_6:T7_9 T8_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        root02 = self.helper.get_node( forrest01, 1)

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.replace_subtree_with_nonterminal_and_place_under_root( root02, 'n1' )
        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_11:S_0 |_12
            S_0:N1_1 |_2
            |_2:T3_5 S_6
            S_6:T7_9 T8_10
            |_12:T3_3 S_4
            S_4:T7_7 T8_8
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )
        self.assertEqual( len(forrest01.root.children_map), 2 )
        self.assertEqual( forrest01.root.children_map['n0'], root01 )

        root03 = self.helper.get_node( forrest01, 12)
        self.assertEqual( forrest01.root.children_map['n1'], root03 )


    def test_replace_subtree_with_nonterminal_and_place_under_root_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 S_4
            |_2:T3_5 S_6
            S_4:T7_7 T8_8
            S_6:T7_9 T8_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        root02 = self.helper.get_node( forrest01, 2)

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.replace_subtree_with_nonterminal_and_place_under_root( root02, 'n1' )
        spec02 = self.helper.display_tree( forrest01.root )
#        print(spec02)
        spec02_expected = '''
            R_11:S_0 |_12
            S_0:|_1 N1_2
            |_1:T3_3 S_4
            S_4:T7_7 T8_8
            |_12:T3_5 S_6
            S_6:T7_9 T8_10
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        self.assertEqual( len(forrest01.root.children_map), 2 )
        self.assertEqual( forrest01.root.children_map['n0'], root01 )

        root03 = self.helper.get_node( forrest01, 12)
        self.assertEqual( forrest01.root.children_map['n1'], root03 )


    def test_replace_subtree_with_nonterminal_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 S_4
            |_2:T3_5 S_6
            S_4:T7_7 T8_8
            S_6:T7_9 T8_10
        '''


        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        root02 = self.helper.get_node( forrest01, 1)

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.replace_subtree_with_nonterminal( root02, 'n1' )
        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_11:S_0
            S_0:N1_1 |_2
            |_2:T3_5 S_6
            S_6:T7_9 T8_10
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )
        self.assertEqual( len(forrest01.root.children_map), 1 )


    def test_replace_subtree_with_nonterminal_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 S_4
            |_2:T3_5 S_6
            S_4:T7_7 T8_8
            S_6:T7_9 T8_10
        '''


        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        root02 = self.helper.get_node( forrest01, 2)

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.replace_subtree_with_nonterminal( root02, 'n1' )
        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_11:S_0
            S_0:|_1 N1_2
            |_1:T3_3 S_4
            S_4:T7_7 T8_8
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )
        self.assertEqual( len(forrest01.root.children_map), 1 )


    def test_reduce_best_common_subtree_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 S_4
            |_2:T3_5 S_6
            S_4:T7_7 T8_8
            S_6:T7_9 T8_10
        '''


        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        root02 = self.helper.get_node( forrest01, 2)

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        return01 = reducer01.reduce_best_common_subtree()
        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_11:S_0 |_12
            S_0:N1_1 N1_2
            |_12:T3_3 S_4
            S_4:T7_7 T8_8
        '''

        self.assertEqual( return01,  True )
        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        self.assertEqual( len(forrest01.root.children_map), 2 )
        self.assertEqual( forrest01.root.children_map['n0'], root01 )

        root03 = self.helper.get_node( forrest01, 12)
        self.assertEqual( forrest01.root.children_map['n1'], root03 )


    def test_reduce_best_common_subtree_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1 S_2
            S_1:|_3 |_4 |_5
            S_2:|_6 |_7
            |_3:T1_8 S_9
            S_9:T2_10 T3_11
            |_4:T4_12 S_13
            S_13:T5_14 T6_15
            |_5:T1_16 S_17
            S_17:T2_18 T3_19
            |_6:T1_20 S_21
            S_21:T2_22 T3_23
            |_7:T4_24 S_25
            S_25:T5_26 T6_27
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )
        ast00 = self.helper.get_node( forrest01, 1)
        ast01 = self.helper.get_node( forrest01, 2)

        root01.children_map['n0'] = ast00
        root01.children_map['n1'] = ast01
        forrest01.next_nonterminal_num = 2

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        return01 = reducer01.reduce_best_common_subtree()

        self.assertEqual( return01,  True )
        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_2 |_28
            S_1:N2_3 |_4 N2_5
            |_4:T4_12 S_13
            S_13:T5_14 T6_15
            S_2:N2_6 |_7
            |_7:T4_24 S_25
            S_25:T5_26 T6_27
            |_28:T1_8 S_9
            S_9:T2_10 T3_11
        '''

        self.assertEqual( return01,  True )
        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        self.assertEqual( len(forrest01.root.children_map), 3 )

        self.assertEqual( forrest01.root.children_map['n0'], ast00 )
        self.assertEqual( forrest01.root.children_map['n1'], ast01 )

        ast02 = self.helper.get_node( forrest01, 28)
        self.assertEqual( forrest01.root.children_map['n2'], ast02 )


    def test_reduce_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            S_0:|_1 |_2
            |_1:T3_3 S_4
            |_2:T3_5 S_6
            S_4:T7_7 T8_8
            S_6:T7_9 T8_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )

        forrest01.prepare_for_reduction()

        root02 = self.helper.get_node( forrest01, 2)

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )

        reducer01.reduce()

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_11:S_0 |_12
            S_0:N1_1 N1_2
            |_12:T3_3 S_4
            S_4:T7_7 T8_8
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        self.assertEqual( len(forrest01.root.children_map), 2 )
        self.assertEqual( forrest01.root.children_map['n0'], root01 )

        root03 = self.helper.get_node( forrest01, 12)
        self.assertEqual( forrest01.root.children_map['n1'], root03 )


    def test_reduce_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1 S_2
            S_1:|_3 |_4 |_5
            S_2:|_6 |_7
            |_3:T1_8 S_9
            S_9:T2_10 T3_11
            |_4:T4_12 S_13
            S_13:T5_14 T6_15
            |_5:T1_16 S_17
            S_17:T2_18 T3_19
            |_6:T1_20 S_21
            S_21:T2_22 T3_23
            |_7:T4_24 S_25
            S_25:T5_26 T6_27
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )
        ast00 = self.helper.get_node( forrest01, 1)
        ast01 = self.helper.get_node( forrest01, 2)

        root01.children_map['n0'] = ast00
        root01.children_map['n1'] = ast01
        forrest01.next_nonterminal_num = 2

        reducer01 = nlpregex.regular_language.common_subtree_reducer.CommonSubtreeReducer( forrest01 )
        reducer01.reduce()

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_2 |_28 |_29
            S_1:N2_3 N3_4 N2_5
            S_2:N2_6 N3_7
            |_28:T1_8 S_9
            S_9:T2_10 T3_11
            |_29:T4_12 S_13
            S_13:T5_14 T6_15
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        self.assertEqual( len(forrest01.root.children_map), 4 )

        self.assertEqual( forrest01.root.children_map['n0'], ast00 )
        self.assertEqual( forrest01.root.children_map['n1'], ast01 )

        ast02 = self.helper.get_node( forrest01, 28)
        self.assertEqual( forrest01.root.children_map['n2'], ast02 )

        ast03 = self.helper.get_node( forrest01, 29)
        self.assertEqual( forrest01.root.children_map['n3'], ast03 )




if __name__ == '__main__':
    unittest.main()

