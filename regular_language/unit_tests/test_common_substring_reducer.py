#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for common_substring_reducer.py."""

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.sse_forrest
import nlpregex.regular_language.common_substring_reducer

from nlpregex.regular_language.unit_tests.test_sse_asforrest_helper import test_sse_ASForrest_helper


class test_CommonSubstringReducer( unittest.TestCase ):

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

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        self.assertEqual( len(reducer01.map_regex_to_node_set),  0 )
        self.assertEqual( len(reducer01.series_nodes),                     0 )
        self.assertEqual( reducer01.min_num_subtrees,            2 )
        self.assertEqual( reducer01.min_num_terms,               2 )


    def test_find_series_nodes_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

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

        reducer01.find_series_nodes()
        
        self.assertEqual( len(reducer01.series_nodes), 7)

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )
        series09 = self.helper.get_node( forrest01,  9 )
        series13 = self.helper.get_node( forrest01, 13 )
        series17 = self.helper.get_node( forrest01, 17 )
        series21 = self.helper.get_node( forrest01, 21 )
        series25 = self.helper.get_node( forrest01, 25 )

        sorted_unions = sorted( reducer01.series_nodes )
        self.assertEqual( sorted_unions[0],  series01 )
        self.assertEqual( sorted_unions[1],  series02 )
        self.assertEqual( sorted_unions[2],  series09 )
        self.assertEqual( sorted_unions[3],  series13 )
        self.assertEqual( sorted_unions[4],  series17 )
        self.assertEqual( sorted_unions[5],  series21 )
        self.assertEqual( sorted_unions[6],  series25 )


    def test_construct_map_series_pair_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T2_10 T3_11 T4_12 T8_13 T9_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 3)

        nodes01 = reducer01.map_regex_to_node_set['t2%t3%t4']
        self.assertEqual( len(nodes01), 2)
        positions01_01 = nodes01[series01]
        positions01_02 = nodes01[series02]
        self.assertEqual( len(positions01_01), 1)
        self.assertEqual( len(positions01_02), 1)
        self.assertEqual( 1 in positions01_01, True)
        self.assertEqual( 1 in positions01_02, True)

        nodes02 = reducer01.map_regex_to_node_set['t2%t3']
        self.assertEqual( len(nodes02), 2)
        positions02_01 = nodes02[series01]
        positions02_02 = nodes02[series02]
        self.assertEqual( len(positions02_01), 1)
        self.assertEqual( len(positions02_02), 1)
        self.assertEqual( 1 in positions02_01, True)
        self.assertEqual( 1 in positions02_02, True)

        nodes03 = reducer01.map_regex_to_node_set['t3%t4']
        self.assertEqual( len(nodes03), 2)
        positions03_01 = nodes03[series01]
        positions03_02 = nodes03[series02]
        self.assertEqual( len(positions03_01), 1)
        self.assertEqual( len(positions03_02), 1)
        self.assertEqual( 2 in positions03_01, True)
        self.assertEqual( 2 in positions03_02, True)


    def test_construct_map_series_pair_0002( self ):
 
        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
 
        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
 
        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T9_11 T10_12 T11_13 T12_14
        '''
 
        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )
 
        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
         
        self.assertEqual( len(reducer01.series_nodes), 2 )
 
        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )
 
        self.assertEqual( len(reducer01.map_regex_to_node_set), 0)
 

    def test_construct_map_series_pair_0003( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T1_9 T8_10 T3_11 T10_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 0)


    def test_construct_map_series_pair_0004( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T2_9 T1_10 T2_11 T8_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 1)

        nodes01 = reducer01.map_regex_to_node_set['t1%t2']
        self.assertEqual( len(nodes01), 2)
        positions01 = nodes01[series01]
        positions02 = nodes01[series02]
        self.assertEqual( len(positions01), 1)
        self.assertEqual( len(positions02), 1)

        self.assertEqual( 0 in positions01, True)
        self.assertEqual( 1 in positions02, True)


    def test_construct_map_series_pair_0005( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T2_9 T3_10 T2_11 T8_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 1)

        nodes01 = reducer01.map_regex_to_node_set['t2%t3']
        self.assertEqual( len(nodes01), 2)
        positions01 = nodes01[series01]
        positions02 = nodes01[series02]
        self.assertEqual( len(positions01), 1)
        self.assertEqual( len(positions02), 1)

        self.assertEqual( 1 in positions01, True)
        self.assertEqual( 0 in positions02, True)


    def test_construct_map_series_pair_0006( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T1_9 T2_10 T3_11 T8_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 3)

        nodes01 = reducer01.map_regex_to_node_set['t1%t2%t3']
        self.assertEqual( len(nodes01), 2)
        positions01_01 = nodes01[series01]
        positions01_02 = nodes01[series02]
        self.assertEqual( len(positions01_01), 1)
        self.assertEqual( len(positions01_02), 1)

        self.assertEqual( 0 in positions01_01, True)
        self.assertEqual( 0 in positions01_02, True)

        nodes02 = reducer01.map_regex_to_node_set['t1%t2']
        self.assertEqual( len(nodes02), 2)
        positions02_01 = nodes02[series01]
        positions02_02 = nodes02[series02]
        self.assertEqual( len(positions02_01), 1)
        self.assertEqual( len(positions02_02), 1)

        self.assertEqual( 0 in positions02_01, True)
        self.assertEqual( 0 in positions02_02, True)

        nodes03 = reducer01.map_regex_to_node_set['t2%t3']
        self.assertEqual( len(nodes03), 2)
        positions03_01 = nodes03[series01]
        positions03_02 = nodes03[series02]
        self.assertEqual( len(positions03_01), 1)
        self.assertEqual( len(positions03_02), 1)

        self.assertEqual( 1 in positions03_01, True)
        self.assertEqual( 1 in positions03_02, True)


    def test_construct_map_series_pair_0007( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T4_11 T5_12 T6_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 3)

        nodes01 = reducer01.map_regex_to_node_set['t4%t5%t6']
        self.assertEqual( len(nodes01), 2)
        positions01_01 = nodes01[series01]
        positions01_02 = nodes01[series02]
        self.assertEqual( len(positions01_01), 1)
        self.assertEqual( len(positions01_02), 1)

        self.assertEqual( 3 in positions01_01, True)
        self.assertEqual( 2 in positions01_02, True)

        nodes02 = reducer01.map_regex_to_node_set['t4%t5']
        self.assertEqual( len(nodes02), 2)
        positions02_01 = nodes02[series01]
        positions02_02 = nodes02[series02]
        self.assertEqual( len(positions02_01), 1)
        self.assertEqual( len(positions02_02), 1)

        self.assertEqual( 3 in positions02_01, True)
        self.assertEqual( 2 in positions02_02, True)

        nodes03 = reducer01.map_regex_to_node_set['t5%t6']
        self.assertEqual( len(nodes03), 2)
        positions03_01 = nodes03[series01]
        positions03_02 = nodes03[series02]
        self.assertEqual( len(positions03_01), 1)
        self.assertEqual( len(positions03_02), 1)

        self.assertEqual( 4 in positions03_01, True)
        self.assertEqual( 3 in positions03_02, True)


    def test_construct_map_series_pair_0008( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T9_11 T3_12 T4_13 T5_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 3)

        nodes01 = reducer01.map_regex_to_node_set['t3%t4%t5']
        self.assertEqual( len(nodes01), 2)
        positions01_01 = nodes01[series01]
        positions01_02 = nodes01[series02]
        self.assertEqual( len(positions01_01), 1)
        self.assertEqual( len(positions01_02), 1)
        self.assertEqual( 2 in positions01_01, True)
        self.assertEqual( 3 in positions01_02, True)

        nodes02 = reducer01.map_regex_to_node_set['t3%t4']
        self.assertEqual( len(nodes02), 2)
        positions02_01 = nodes02[series01]
        positions02_02 = nodes02[series02]
        self.assertEqual( len(positions02_01), 1)
        self.assertEqual( len(positions02_02), 1)
        self.assertEqual( 2 in positions02_01, True)
        self.assertEqual( 3 in positions02_02, True)

        nodes03 = reducer01.map_regex_to_node_set['t4%t5']
        self.assertEqual( len(nodes03), 2)
        positions03_01 = nodes03[series01]
        positions03_02 = nodes03[series02]
        self.assertEqual( len(positions03_01), 1)
        self.assertEqual( len(positions03_02), 1)
        self.assertEqual( 3 in positions03_01, True)
        self.assertEqual( 4 in positions03_02, True)


    def test_construct_map_series_pair_0009( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T9_11 T4_12 T5_13 T6_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 3)

        nodes01 = reducer01.map_regex_to_node_set['t4%t5%t6']
        self.assertEqual( len(nodes01), 2)
        positions01_01 = nodes01[series01]
        positions01_02 = nodes01[series02]
        self.assertEqual( len(positions01_01), 1)
        self.assertEqual( len(positions01_02), 1)
        self.assertEqual( 3 in positions01_01, True)
        self.assertEqual( 3 in positions01_02, True)

        nodes02 = reducer01.map_regex_to_node_set['t4%t5']
        self.assertEqual( len(nodes02), 2)
        positions02_01 = nodes02[series01]
        positions02_02 = nodes02[series02]
        self.assertEqual( len(positions02_01), 1)
        self.assertEqual( len(positions02_02), 1)
        self.assertEqual( 3 in positions02_01, True)
        self.assertEqual( 3 in positions02_02, True)

        nodes03 = reducer01.map_regex_to_node_set['t5%t6']
        self.assertEqual( len(nodes03), 2)
        positions03_01 = nodes03[series01]
        positions03_02 = nodes03[series02]
        self.assertEqual( len(positions03_01), 1)
        self.assertEqual( len(positions03_02), 1)
        self.assertEqual( 4 in positions03_01, True)
        self.assertEqual( 4 in positions03_02, True)


    def test_construct_map_series_pair_0010( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T1_6 T2_7 T3_8
            S_2:T1_9 T2_10 T3_11 T1_12 T2_13 T3_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 12)

        nodes01 = reducer01.map_regex_to_node_set['t1%t2']
        self.assertEqual( len(nodes01), 2)
        positions01_01 = nodes01[series01]
        positions01_02 = nodes01[series02]
        self.assertEqual( len(positions01_01), 2)
        self.assertEqual( len(positions01_02), 2)
        self.assertEqual( 0 in positions01_01, True)
        self.assertEqual( 3 in positions01_01, True)
        self.assertEqual( 0 in positions01_02, True)
        self.assertEqual( 3 in positions01_02, True)

        nodes02 = reducer01.map_regex_to_node_set['t1%t2%t3']
        self.assertEqual( len(nodes02), 2)
        positions02_01 = nodes02[series01]
        positions02_02 = nodes02[series02]
        self.assertEqual( len(positions02_01), 2)
        self.assertEqual( len(positions02_02), 2)
        self.assertEqual( 0 in positions02_01, True)
        self.assertEqual( 3 in positions02_01, True)
        self.assertEqual( 0 in positions02_02, True)
        self.assertEqual( 3 in positions02_02, True)

        nodes03 = reducer01.map_regex_to_node_set['t1%t2%t3%t1']
        self.assertEqual( len(nodes03), 2)
        positions03_01 = nodes03[series01]
        positions03_02 = nodes03[series02]
        self.assertEqual( len(positions03_01), 1)
        self.assertEqual( len(positions03_02), 1)
        self.assertEqual( 0 in positions03_01, True)
        self.assertEqual( 0 in positions03_02, True)

        nodes04 = reducer01.map_regex_to_node_set['t1%t2%t3%t1%t2']
        self.assertEqual( len(nodes04), 2)
        positions04_01 = nodes04[series01]
        positions04_02 = nodes04[series02]
        self.assertEqual( len(positions04_01), 1)
        self.assertEqual( len(positions04_02), 1)
        self.assertEqual( 0 in positions04_01, True)
        self.assertEqual( 0 in positions04_02, True)

        nodes05 = reducer01.map_regex_to_node_set['t1%t2%t3%t1%t2%t3']
        self.assertEqual( len(nodes05), 2)
        positions05_01 = nodes05[series01]
        positions05_02 = nodes05[series02]
        self.assertEqual( len(positions05_01), 1)
        self.assertEqual( len(positions05_02), 1)
        self.assertEqual( 0 in positions05_01, True)
        self.assertEqual( 0 in positions05_02, True)

        nodes06 = reducer01.map_regex_to_node_set['t2%t3']
        self.assertEqual( len(nodes06), 2)
        positions06_01 = nodes06[series01]
        positions06_02 = nodes06[series02]
        self.assertEqual( len(positions06_01), 2)
        self.assertEqual( len(positions06_02), 2)
        self.assertEqual( 1 in positions06_01, True)
        self.assertEqual( 4 in positions06_01, True)
        self.assertEqual( 1 in positions06_02, True)
        self.assertEqual( 4 in positions06_02, True)

        nodes07 = reducer01.map_regex_to_node_set['t2%t3%t1']
        self.assertEqual( len(nodes07), 2)
        positions07_01 = nodes07[series01]
        positions07_02 = nodes07[series02]
        self.assertEqual( len(positions07_01), 1)
        self.assertEqual( len(positions07_02), 1)
        self.assertEqual( 1 in positions07_01, True)
        self.assertEqual( 1 in positions07_02, True)

        nodes08 = reducer01.map_regex_to_node_set['t2%t3%t1%t2']
        self.assertEqual( len(nodes08), 2)
        positions08_01 = nodes08[series01]
        positions08_02 = nodes08[series02]
        self.assertEqual( len(positions08_01), 1)
        self.assertEqual( len(positions08_02), 1)
        self.assertEqual( 1 in positions08_01, True)
        self.assertEqual( 1 in positions08_02, True)

        nodes09 = reducer01.map_regex_to_node_set['t2%t3%t1%t2%t3']
        self.assertEqual( len(nodes09), 2)
        positions09_01 = nodes09[series01]
        positions09_02 = nodes09[series02]
        self.assertEqual( len(positions09_01), 1)
        self.assertEqual( len(positions09_02), 1)
        self.assertEqual( 1 in positions09_01, True)
        self.assertEqual( 1 in positions09_02, True)

        nodes10 = reducer01.map_regex_to_node_set['t3%t1']
        self.assertEqual( len(nodes10), 2)
        positions10_01 = nodes10[series01]
        positions10_02 = nodes10[series02]
        self.assertEqual( len(positions10_01), 1)
        self.assertEqual( len(positions10_02), 1)
        self.assertEqual( 2 in positions10_01, True)
        self.assertEqual( 2 in positions10_02, True)

        nodes11 = reducer01.map_regex_to_node_set['t3%t1%t2']
        self.assertEqual( len(nodes11), 2)
        positions11_01 = nodes11[series01]
        positions11_02 = nodes11[series02]
        self.assertEqual( len(positions11_01), 1)
        self.assertEqual( len(positions11_02), 1)
        self.assertEqual( 2 in positions11_01, True)
        self.assertEqual( 2 in positions11_02, True)

        nodes12 = reducer01.map_regex_to_node_set['t3%t1%t2%t3']
        self.assertEqual( len(nodes12), 2)
        positions12_01 = nodes12[series01]
        positions12_02 = nodes12[series02]
        self.assertEqual( len(positions12_01), 1)
        self.assertEqual( len(positions12_02), 1)
        self.assertEqual( 2 in positions12_01, True)
        self.assertEqual( 2 in positions12_02, True)

    # Self-overlap
    def test_construct_map_series_pair_0011( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1
            S_1:T1_3 T2_4 T3_5 T1_6 T2_7 T3_8
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 1 )

        series01 = self.helper.get_node( forrest01,  1 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 3)

        nodes01 = reducer01.map_regex_to_node_set['t1%t2']
        self.assertEqual( len(nodes01), 1)
        positions01_01 = nodes01[series01]
        self.assertEqual( len(positions01_01), 2)
        self.assertEqual( 0 in positions01_01, True)
        self.assertEqual( 3 in positions01_01, True)

        nodes02 = reducer01.map_regex_to_node_set['t1%t2%t3']
        self.assertEqual( len(nodes02), 1)
        positions02_01 = nodes02[series01]
        self.assertEqual( len(positions02_01), 2)
        self.assertEqual( 0 in positions02_01, True)
        self.assertEqual( 3 in positions02_01, True)

        nodes03 = reducer01.map_regex_to_node_set['t2%t3']
        self.assertEqual( len(nodes03), 1)
        positions03_01 = nodes03[series01]
        self.assertEqual( len(positions03_01), 2)
        self.assertEqual( 1 in positions03_01, True)
        self.assertEqual( 4 in positions03_01, True)


    def test_construct_map_series_pair_0012( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 |_4 T3_5 ?_6 T5_7 T6_8
            S_2:T7_9 T8_10 |_11 T3_12 ?_13 T9_14
            |_4:T10_15 T11_16
            ?_6:T12_17
            |_11:T10_18 T11_19
            ?_13:T12_20
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        self.assertEqual( len(reducer01.series_nodes), 2 )

        series01 = self.helper.get_node( forrest01,  1 )
        series02 = self.helper.get_node( forrest01,  2 )

        self.assertEqual( len(reducer01.map_regex_to_node_set), 3)

        nodes01 = reducer01.map_regex_to_node_set['( t10 | t11 )%t3']
        self.assertEqual( len(nodes01), 2)
        positions01_01 = nodes01[series01]
        positions01_02 = nodes01[series02]
        self.assertEqual( len(positions01_01), 1)
        self.assertEqual( len(positions01_02), 1)
        self.assertEqual( 1 in positions01_01, True)
        self.assertEqual( 2 in positions01_02, True)

        nodes02 = reducer01.map_regex_to_node_set['t3%t12 ?']
        self.assertEqual( len(nodes02), 2)
        positions02_01 = nodes02[series01]
        positions02_02 = nodes02[series02]
        self.assertEqual( len(positions02_01), 1)
        self.assertEqual( len(positions02_02), 1)
        self.assertEqual( 2 in positions02_01, True)
        self.assertEqual( 3 in positions02_02, True)

        nodes03 = reducer01.map_regex_to_node_set['( t10 | t11 )%t3%t12 ?']
        self.assertEqual( len(nodes03), 2)
        positions03_01 = nodes03[series01]
        positions03_02 = nodes03[series02]
        self.assertEqual( len(positions03_01), 1)
        self.assertEqual( len(positions03_02), 1)
        self.assertEqual( 1 in positions03_01, True)
        self.assertEqual( 2 in positions03_02, True)


    def test_find_best_regex_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T2_10 T3_11 T4_12 T8_13 T9_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
        self.assertEqual( regex01, 't2%t3%t4' )


    def test_find_best_regex_0002( self ):
 
        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
 
        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
 
        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T9_11 T10_12 T11_13 T12_14
        '''
 
        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )
 
        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
        self.assertEqual( regex01, '' )


    def test_find_best_regex_0003( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T1_9 T8_10 T3_11 T10_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, '' )
        

    def test_find_best_regex_0004( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T2_9 T1_10 T2_11 T8_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't1%t2' )


    def test_find_best_regex_0005( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T2_9 T3_10 T2_11 T8_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't2%t3' )
        

    def test_find_best_regex_0006( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T1_9 T2_10 T3_11 T8_12 T5_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't1%t2%t3' )
        

    def test_find_best_regex_0007( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T4_11 T5_12 T6_13 T12_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't4%t5%t6' )


    def test_find_best_regex_0008( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T9_11 T3_12 T4_13 T5_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()

        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't3%t4%t5' )
        

    def test_find_best_regex_0009( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T4_6 T5_7 T6_8
            S_2:T7_9 T8_10 T9_11 T4_12 T5_13 T6_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't4%t5%t6' )


    def test_find_best_regex_0010( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 T2_4 T3_5 T1_6 T2_7 T3_8
            S_2:T1_9 T2_10 T3_11 T1_12 T2_13 T3_14
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't1%t2%t3' )
        

    def test_find_best_regex_0011( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1
            S_1:T1_3 T2_4 T3_5 T1_6 T2_7 T3_8
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, 't1%t2%t3' )


    def test_find_best_regex_0012( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        reducer01  = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        spec01= '''
            R_0:S_1 S_2
            S_1:T1_3 |_4 T3_5 ?_6 T5_7 T6_8
            S_2:T7_9 T8_10 |_11 T3_12 ?_13 T9_14
            |_4:T10_15 T11_16
            ?_6:T12_17
            |_11:T10_18 T11_19
            ?_13:T12_20
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        reducer01.find_series_nodes()
        reducer01.construct_map_series_pairs()
        
        regex01 = reducer01.find_best_regex()
#        print (regex01)
        self.assertEqual( regex01, '( t10 | t11 )%t3%t12 ?' )


    def test_remove_children_and_replace_with_nonterminal_0001(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 3, [1] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:T2_2 N1_7 T6_6
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0002(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 3, [0] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:N1_7 T5_5 T6_6
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0003(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 3, [2] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:T2_2 T3_3 N1_7
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0004(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 5, [0] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:N1_1
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0005(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 3, [0, 3] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:N1_8 N1_9
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0006(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 2, [0, 2, 4] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:N1_8 N1_9 N1_10
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0007(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 2, [1, 3] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:T2_2 N1_8 N1_9 T4_7
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0008(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 2, [1, 4] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:T2_2 N1_8 T2_5 N1_9
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0009(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )

        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n1', 2, [0, 4] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1
            S_1:N1_8 T4_4 T2_5 N1_9
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_move_children_to_new_tree_0001(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 3, [1] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_8
            S_1:T2_2 N1_7 T6_6
            S_8:T3_3 T4_4 T5_5
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 8 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0002(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 3, [0] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_8
            S_1:N1_7 T5_5 T6_6
            S_8:T2_2 T3_3 T4_4
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 8 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0003(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 3, [2] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_8
            S_1:T2_2 T3_3 N1_7
            S_8:T4_4 T5_5 T6_6
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 8 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0004(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 5, [0] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:N1_1 S_8
            S_8:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 8 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0005(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 3, [0, 3] )

        spec02 = self.helper.display_tree( forrest01.root )
        spec02_expected = '''
            R_0:S_1 S_10
            S_1:N1_8 N1_9
            S_10:T2_2 T3_3 T4_4
        '''

#        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 10 )
#        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0006(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 2, [0, 2, 4] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_11
            S_1:N1_8 N1_9 N1_10
            S_11:T2_2 T3_3
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 11 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0007(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 2, [1, 3] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_10
            S_1:T2_2 N1_8 N1_9 T4_7
            S_10:T3_3 T4_4
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 10 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0008(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 2, [1, 4] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_10
            S_1:T2_2 N1_8 T2_5 N1_9
            S_10:T3_3 T4_4
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 10 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0009(self):


        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.move_children_to_new_tree( ast00, 'n1', 2, [0, 4] )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_10
            S_1:N1_8 T4_4 T2_5 N1_9
            S_10:T2_2 T3_3
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 10 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_reduce_best_common_substring_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:T2_2 T3_3 T4_4 T2_5 T3_6 T4_7
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.reduce_best_common_substring()

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:S_1 S_10
            S_1:N1_8 N1_9
            S_10:T2_2 T3_3 T4_4
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 10 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_reduce_best_common_substring_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:S_2 S_3
            S_2:T2_4 T3_5 T4_6 T2_7 T3_8 T4_9
            S_3:T2_10 T3_11 T4_12 T2_13 T3_14 T4_15
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.reduce_best_common_substring()

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:|_1 S_18
            |_1:S_2 S_3
            S_2:N1_16 N1_17
            S_3:N1_19 N1_20
            S_18:T2_4 T3_5 T4_6
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 18 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_reduce_best_common_substring_0003( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:S_2 S_3 S_4
            S_2:T5_5 T1_6 T2_7 T3_8
            S_3:T9_9 T1_10 T2_11 T3_12 T13_13 T14_14
            S_4:T1_15 T2_16 T3_17 T18_18 T19_19 T20_20
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.reduce_best_common_substring()

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:|_1 S_22
            |_1:S_2 S_3 S_4
            S_2:T5_5 N1_21
            S_3:T9_9 N1_23 T13_13 T14_14
            S_4:N1_24 T18_18 T19_19 T20_20
            S_22:T1_6 T2_7 T3_8
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 22 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_reduce_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:S_2 S_3 S_4
            S_2:T5_5 T1_6 T2_7 T3_8
            S_3:T9_9 T1_10 T2_11 T3_12 T4_13 T5_14
            S_4:T1_15 T2_16 T3_17 T4_18 T5_19 T20_20
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_substring_reducer.CommonSubstringReducer( forrest01 )
        reducer01.reduce()

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:|_1 S_22 S_26
            |_1:S_2 S_3 S_4
            S_2:T5_5 N1_21
            S_3:T9_9 N2_25
            S_4:N2_27 T20_20
            S_22:T1_6 T2_7 T3_8
            S_26:N1_23 T4_13 T5_14
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )

        ast01 = self.helper.get_node( forrest01, 22 )
        self.assertEqual( ast01, root01.children_map['n1'] )
        ast02 = self.helper.get_node( forrest01, 26 )
        self.assertEqual( ast02, root01.children_map['n2'] )


if __name__ == '__main__':
    unittest.main()

