#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for common_union_subexpression_reducer.py."""

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.sse_forrest
import nlpregex.regular_language.common_union_subexpression_reducer

from nlpregex.regular_language.unit_tests.test_sse_asforrest_helper import test_sse_ASForrest_helper

class test_CommonUnionSubexpressionReducer( unittest.TestCase ):

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

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )

        self.assertEqual( len(reducer01.map_regex_to_node_set),  0 )
        self.assertEqual( len(reducer01.unions),                 0 )
        self.assertEqual( reducer01.min_num_subtrees,            2 )
        self.assertEqual( reducer01.min_num_terms,               2 )


    def test_find_unions_0001( self ):

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

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.find_unions()

        self.assertEqual( len(reducer01.unions),  5 )

        union03 = self.helper.get_node( forrest01, 3)
        union04 = self.helper.get_node( forrest01, 4)
        union05 = self.helper.get_node( forrest01, 5)
        union06 = self.helper.get_node( forrest01, 6)
        union07 = self.helper.get_node( forrest01, 7)

        sorted_unions = sorted( reducer01.unions )
        self.assertEqual( sorted_unions[0],  union03 )
        self.assertEqual( sorted_unions[1],  union04 )
        self.assertEqual( sorted_unions[2],  union05 )
        self.assertEqual( sorted_unions[3],  union06 )
        self.assertEqual( sorted_unions[4],  union07 )


    def test_find_unions_0002( self ):

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

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.find_unions()

        self.assertEqual( len(reducer01.unions),  5 )

        union03 = self.helper.get_node( forrest01, 3)
        union04 = self.helper.get_node( forrest01, 4)
        union05 = self.helper.get_node( forrest01, 5)
        union06 = self.helper.get_node( forrest01, 6)
        union07 = self.helper.get_node( forrest01, 7)

        sorted_unions = sorted( reducer01.unions )
        self.assertEqual( sorted_unions[0],  union03 )
        self.assertEqual( sorted_unions[1],  union04 )
        self.assertEqual( sorted_unions[2],  union05 )
        self.assertEqual( sorted_unions[3],  union06 )
        self.assertEqual( sorted_unions[4],  union07 )


    def test_this_node_includes_regex_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1)

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )

        union01  = self.helper.get_node( forrest01, 1)
        return01 = reducer01.this_node_includes_regex( union01, 't3%t4%t5%t6')
        self.assertEqual( return01,  True )   

        return02 = reducer01.this_node_includes_regex( union01, 't3%t4%t5')
        self.assertEqual( return02,  True )   

        return03 = reducer01.this_node_includes_regex( union01, 't3%t5')
        self.assertEqual( return03,  True )   

        return04 = reducer01.this_node_includes_regex( union01, 't4')
        self.assertEqual( return04,  True )   

        return05 = reducer01.this_node_includes_regex( union01, 't2%t3%t4%t5%t6')
        self.assertEqual( return05,  False )   

        return06 = reducer01.this_node_includes_regex( union01, 't3%t4%t5%t6%t7')
        self.assertEqual( return06,  False )   

        return07 = reducer01.this_node_includes_regex( union01, 't1%t2%t3%t4%t7')
        self.assertEqual( return07,  False )   

        return08 = reducer01.this_node_includes_regex( union01, 't10%t11%t12%t13%t14')
        self.assertEqual( return08,  False )   

        return09 = reducer01.this_node_includes_regex( union01, 't4%t6%t3%t5')
        self.assertEqual( return09,  True )   

        return10 = reducer01.this_node_includes_regex( union01, 't3%t5%t4')
        self.assertEqual( return10,  True )   

        return11 = reducer01.this_node_includes_regex( union01, 't3%t5%t2%t6%t4')
        self.assertEqual( return11,  False )   


    def test_this_node_includes_regex_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T3_3 S_4 T5_5 S_6
            S_4:T7_7 T8_8 
            S_6:T9_9 |_11 T10_10
            |_11:T12_12 T13_13
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1)

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )

        union01  = self.helper.get_node( forrest01, 1)

        return01 = reducer01.this_node_includes_regex( union01, 't3%t7 t8%t5%t9 ( t12 | t13 ) t10')
        self.assertEqual( return01,  True )   

        return02 = reducer01.this_node_includes_regex( union01, 't3%t9 ( t12 | t13 ) t10%t7 t8%t5')
        self.assertEqual( return02,  True )   

        return03 = reducer01.this_node_includes_regex( union01, 't9 ( t12 | t13 ) t10%t7 t8')
        self.assertEqual( return03,  True )

        return04 = reducer01.this_node_includes_regex( union01, 't9 ( t12 | t13 ) t10%t5%t7 t8')
        self.assertEqual( return04,  True )

        return05 = reducer01.this_node_includes_regex( union01, 't9 ( t12 | t13 ) t10%t5%t7 t8%t1')
        self.assertEqual( return05,  False )

        return06 = reducer01.this_node_includes_regex( union01, 't11%t9 ( t12 | t13 ) t10%t5%t7 t8')
        self.assertEqual( return06,  False )


    def test_construct_map_union_pairs_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:|_2 |_3 |_4 |_5
            |_2:T6_6 T7_7 T8_8 T9_9 
            |_3:T7_10 T8_11 T9_12 T10_13
            |_4:T8_14 T9_15 T10_16 T11_17
            |_5:T9_18 T10_19 T11_20 T12_21
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1)

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.find_unions()
        reducer01.construct_map_union_pairs()
#        print (reducer01.map_regex_to_node_set )

        union02 = self.helper.get_node( forrest01, 2 )
        union03 = self.helper.get_node( forrest01, 3 )
        union04 = self.helper.get_node( forrest01, 4 )
        union05 = self.helper.get_node( forrest01, 5 )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t7%t8%t9']), 2 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t7%t8%t9'], True )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t7%t8%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t10%t8%t9']), 2 )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t10%t8%t9'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t10%t8%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t10%t11%t9']), 2 )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t10%t11%t9'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t10%t11%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t8%t9']), 2 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t8%t9'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t8%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t10%t9']), 2 )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t10%t9'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t10%t9'], True )


    def test_augment_map_regex_pairs_0001(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:|_2 |_3 |_4 |_5
            |_2:T6_6 T7_7 T8_8 T9_9 
            |_3:T7_10 T8_11 T9_12 T10_13
            |_4:T8_14 T9_15 T10_16 T11_17
            |_5:T9_18 T10_19 T11_20 T12_21
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1)

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.find_unions()
        reducer01.construct_map_union_pairs()
        reducer01.augment_map_regex_pairs()

#        print (reducer01.map_regex_to_node_set )

        union02 = self.helper.get_node( forrest01, 2 )
        union03 = self.helper.get_node( forrest01, 3 )
        union04 = self.helper.get_node( forrest01, 4 )
        union05 = self.helper.get_node( forrest01, 5 )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t7%t8%t9']), 2 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t7%t8%t9'], True )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t7%t8%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t10%t8%t9']), 2 )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t10%t8%t9'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t10%t8%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t10%t11%t9']), 2 )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t10%t11%t9'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t10%t11%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t8%t9']), 3 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t8%t9'], True )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t8%t9'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t8%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t10%t9']), 3 )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t10%t9'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t10%t9'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t10%t9'], True )


    def test_augment_map_regex_pairs_0002(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:|_2 |_3 |_4 |_5
            |_2:T1_6 T2_7 T3_8 T4_9 T5_10 T6_11
            |_3:T2_12 T3_13 T4_14 T5_15 T6_16 T7_17
            |_4:T1_18 T2_19 T8_20 T4_21 T9_22 T6_23
            |_5:T2_24 T8_25 T4_26 T9_27 T6_28 T7_29
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1)

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.find_unions()
        reducer01.construct_map_union_pairs()
#        print (reducer01.map_regex_to_node_set.keys())
        reducer01.augment_map_regex_pairs()

#        print (reducer01.map_regex_to_node_set )

        union02 = self.helper.get_node( forrest01, 2 )
        union03 = self.helper.get_node( forrest01, 3 )
        union04 = self.helper.get_node( forrest01, 4 )
        union05 = self.helper.get_node( forrest01, 5 )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t2%t3%t4%t5%t6']), 2 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t2%t3%t4%t5%t6'], True )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t2%t3%t4%t5%t6'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t1%t2%t4%t6']), 2 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t1%t2%t4%t6'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t1%t2%t4%t6'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t2%t4%t6']), 4 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t2%t4%t6%t7']), 2 )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t2%t4%t6%t7'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t2%t4%t6%t7'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t2%t4%t6%t8%t9']), 2 )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t2%t4%t6%t8%t9'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t2%t4%t6%t8%t9'], True )


    def test_augment_map_regex_pairs_0003(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:|_2 |_3 |_4 |_5
            |_2:T1_6 T2_7 T3_8 T4_9 T5_10 T6_11
            |_3:T2_12 T3_13 T4_14 T5_15 T6_16 T7_17
            |_4:T10_18 T2_19 T8_20 T4_21 T9_22 T6_23
            |_5:T2_24 T8_25 T4_26 T9_27 T6_28 T11_29
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1)

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.find_unions()
        reducer01.construct_map_union_pairs()

        del reducer01.map_regex_to_node_set['t2%t4%t6'] # Artificially remove the common expression

        reducer01.augment_map_regex_pairs()

#        print (reducer01.map_regex_to_node_set )

        union02 = self.helper.get_node( forrest01, 2 )
        union03 = self.helper.get_node( forrest01, 3 )
        union04 = self.helper.get_node( forrest01, 4 )
        union05 = self.helper.get_node( forrest01, 5 )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t2%t3%t4%t5%t6']),  2 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t2%t3%t4%t5%t6'], True )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t2%t3%t4%t5%t6'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t2%t4%t6%t8%t9']), 2 )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t2%t4%t6%t8%t9'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t2%t4%t6%t8%t9'], True )

        self.assertEqual( len(reducer01.map_regex_to_node_set['t2%t4%t6']), 4 )
        self.assertEqual( union02 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )
        self.assertEqual( union03 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )
        self.assertEqual( union04 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )
        self.assertEqual( union05 in reducer01.map_regex_to_node_set['t2%t4%t6'], True )


    def test_find_best_regex_0001(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:S_1
            S_1:|_2 |_3 |_4 |_5
            |_2:T6_6 T7_7 T8_8 T9_9 
            |_3:T7_10 T8_11 T9_12 T10_13
            |_4:T8_14 T9_15 T10_16 T11_17
            |_5:T9_18 T10_19 T11_20 T12_21
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1)

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.find_unions()
        reducer01.construct_map_union_pairs()
        reducer01.augment_map_regex_pairs()
        regex01 = reducer01.find_best_regex()

#        print (regex01)

        self.assertEqual( regex01, 't10%t9' )


    def test_remove_children_and_replace_with_nonterminal_0001(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        regex01 = 't2%t4'
        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n01', regex01 )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:|_1
            |_1:T3_3 T5_5 T6_6 N01_7
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0002(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        regex01 = 't2%t4%t6'
        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n01', regex01 )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:|_1
            |_1:T3_3 T5_5 N01_7
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_remove_children_and_replace_with_nonterminal_0003(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        regex01 = 't2%t4%t6%t3%t5'
        reducer01.remove_children_and_replace_with_nonterminal( ast00, 'n01', regex01 )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:N01_1
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )


    def test_move_children_to_new_tree_0001(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        regex01 = 't2%t4'
        reducer01.move_children_to_new_tree( ast00, 'n1', regex01 )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:|_1 |_8
            |_1:T3_3 T5_5 T6_6 N1_7
            |_8:T2_2 T4_4
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )
        self.assertEqual( len(root01.children_map), 2 )
        ast01 = self.helper.get_node( forrest01, 8 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0002(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        regex01 = 't2%t4%t6'
        reducer01.move_children_to_new_tree( ast00, 'n1', regex01 )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:|_1 |_8
            |_1:T3_3 T5_5 N1_7
            |_8:T2_2 T4_4 T6_6
        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )
        self.assertEqual( len(root01.children_map), 2 )
        ast01 = self.helper.get_node( forrest01, 8 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_move_children_to_new_tree_0003(self):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()

        spec01= '''
            R_0:|_1
            |_1:T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01 = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.add_root(root01)
        forrest01.visit_and_prepare_for_reduction( root01 )

        ast00 = self.helper.get_node( forrest01, 1 )

        root01.children_map['n0'] = ast00
        forrest01.next_nonterminal_num = 1

        reducer01 = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        regex01 = 't2%t4%t6%t3%t5'
        reducer01.move_children_to_new_tree( ast00, 'n1', regex01 )

        spec02 = self.helper.display_tree( forrest01.root )
#        print (spec02)
        spec02_expected = '''
            R_0:N1_1 |_7
            |_7:T2_2 T3_3 T4_4 T5_5 T6_6

        '''

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )
        self.assertEqual( len(root01.children_map), 2 )
        ast01 = self.helper.get_node( forrest01, 7 )
        self.assertEqual( ast01, root01.children_map['n1'] )


    def test_reduce_best_common_subexpression_0001( self ):

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

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
        reducer01.reduce_best_common_subexpression()


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

        self.assertEqual( self.helper.compare_specs( spec02, spec02_expected ), True )
        self.assertEqual( len(root01.children_map), 3 )
        ast02 = self.helper.get_node( forrest01, 28 )
        self.assertEqual( ast02, root01.children_map['n2'] )


    def test_reduce_best_common_subexpression_0002( self ):

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

        reducer01  = nlpregex.regular_language.common_union_subexpression_reducer.CommonUnionSubexpressionReducer( forrest01 )
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
        self.assertEqual( len(root01.children_map), 4 )
        ast02 = self.helper.get_node( forrest01, 28 )
        self.assertEqual( ast02, root01.children_map['n2'] )
        ast03 = self.helper.get_node( forrest01, 29 )
        self.assertEqual( ast03, root01.children_map['n3'] )



if __name__ == '__main__':
    unittest.main()

