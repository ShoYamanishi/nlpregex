#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for sse_solver.py """

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.sse_forrest
import nlpregex.regular_language.sse_solver

from nlpregex.regular_language.unit_tests.test_sse_asforrest_helper import test_sse_ASForrest_helper

class test_SymbolicEquation( unittest.TestCase ):


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

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 123, forrest01 )

        self.assertEqual( equation01.lhs,     123 )
        self.assertEqual( equation01.rhs,     {} )
        self.assertEqual( equation01.forrest, forrest01 )


    def test_add_coeff_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = 'E_0'

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 2, ['e'])
        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     'e' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    def test_add_coeff_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = 'T1_0'

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 2, ['t1'])
        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     't1' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    def test_add_coeff_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '|_0:T1_1 T2_2'

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 2, ['t1', 't2'])
        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     '( t1 | t2 )' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    def test_add_coeff_0003( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '|_0:E_1 T1_2'

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 2, ['t1', 'e'])
        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     '( e | t1 )' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    def test_add_coeff_0004( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '|_0:T1_1 T2_2 T3_3'

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 2, ['t1', 't3', 't2'])
        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     '( t1 | t2 | t3 )' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    # (1) = t1 (1) | t2 (2)
    def test_remove_self_recursion_0001( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '''
            S_6:*_4 T2_1
            *_4:T1_5
        '''

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 1, ['t1'])
        equation01.add_coeff( 2, ['t2'])

        equation01.remove_self_recursion()

        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     't1 * t2' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    # (1) = t2 (2)
    def test_remove_self_recursion_0002( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '''
            T2_0
        '''

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 2, ['t2'])

        equation01.remove_self_recursion()

        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     't2' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    # (1) = e (1) | t2 (2)
    def test_remove_self_recursion_0003( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '''
            T2_1
        '''

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 1, ['e'])
        equation01.add_coeff( 2, ['t2'])

        equation01.remove_self_recursion()

        self.assertEqual( len(equation01.rhs),     1 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     't2' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    # (1) = t1 (1) | t2 (2) | t3 (3)
    def test_remove_self_recursion_0004( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '''
            S_6:*_4 T2_1
            *_4:T1_5
        '''
        term_expected03 = '''
            S_9:*_7 T3_2
            *_7:T1_8
        '''

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 1, ['t1'])
        equation01.add_coeff( 2, ['t2'])
        equation01.add_coeff( 3, ['t3'])

        equation01.remove_self_recursion()

        self.assertEqual( len(equation01.rhs),     2 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     't1 * t2' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex,     't1 * t3' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )


    # (1) = (t1 | t2) (1) | (t3 | t4) (2) | (t5 | t6) (3)
    def test_remove_self_recursion_0004( self ):

        forrest01  = nlpregex.regular_language.sse_forrest.sseASForrest()
        term_expected02 = '''
            S_17:*_13 |_3
            *_13:|_14
            |_14:T1_15 T2_16
            |_3:T3_4 T4_5
        '''
        term_expected03 = '''
            S_22:*_18 |_6
            *_18:|_19
            |_19:T1_20 T2_21
            |_6:T5_7 T6_8
        '''

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.add_coeff( 1, ['t1', 't2'])
        equation01.add_coeff( 2, ['t3', 't4'])
        equation01.add_coeff( 3, ['t5', 't6'])

        equation01.remove_self_recursion()

        self.assertEqual( len(equation01.rhs),     2 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     '( t1 | t2 ) * ( t3 | t4 )' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex,     '( t1 | t2 ) * ( t5 | t6 )' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    # (1) = t1 t2 (1) | t3 t4 (2) | t5 t6 (3)
    def test_remove_self_recursion_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2
        '''
        spec02 = '''
            S_3:T3_4 T4_5
        '''
        spec03 = '''
            S_6:T5_7 T6_8
        '''

        term_expected02 = '''
            S_17:*_13 T3_4 T4_5
            *_13:S_14
            S_14:T1_15 T2_16
        '''

        term_expected03 = '''
            S_22:*_18 T5_7 T6_8
            *_18:S_19
            S_19:T1_20 T2_21
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = self.helper.construct_ast_from_spec( forrest01, spec02 )
        root03  = self.helper.construct_ast_from_spec( forrest01, spec03 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[1] = root01
        equation01.rhs[2] = root02
        equation01.rhs[3] = root03

        equation01.remove_self_recursion()

        self.assertEqual( len(equation01.rhs),     2 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     '( t1 t2 ) * t3 t4' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex,     '( t1 t2 ) * t5 t6' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    # (1) =  t1 * (1) | t3 t4 (2) | t5 t6 (3)
    def test_remove_self_recursion_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            *_0:T1_1
        '''
        spec02 = '''
            S_3:T3_4 T4_5
        '''
        spec03 = '''
            S_6:T5_7 T6_8
        '''

        term_expected02 = '''
            S_12:*_10 T3_4 T4_5
            *_10:T1_11
        '''

        term_expected03 = '''
            S_15:*_13 T5_7 T6_8
            *_13:T1_14
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = self.helper.construct_ast_from_spec( forrest01, spec02 )
        root03  = self.helper.construct_ast_from_spec( forrest01, spec03 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[1] = root01
        equation01.rhs[2] = root02
        equation01.rhs[3] = root03

        equation01.remove_self_recursion()

        self.assertEqual( len(equation01.rhs),     2 )
        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex,     't1 * t3 t4' )
        spec02 = self.helper.display_tree( term02 )

        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex,     't1 * t5 t6' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    def test_prepend_coeff_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01 = '''
            T1_1
        '''

        spec02 = '''
            T2_2
        '''

        spec03 = '''
            T3_3
        '''

        spec04 = '''
            T4_4
        '''

        term_expected02 = '''
            S_5:T4_4 T1_1
        '''

        term_expected03 = '''
            S_7:T4_6 T2_2
        '''

        term_expected04 = '''
            S_9:T4_8 T3_3
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = self.helper.construct_ast_from_spec( forrest01, spec02 )
        root03  = self.helper.construct_ast_from_spec( forrest01, spec03 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01
        equation01.rhs[3] = root02
        equation01.rhs[4] = root03

        root04  = self.helper.construct_ast_from_spec( forrest01, spec04 )

        equation01.prepend_coeff(root04)

        self.assertEqual( len(equation01.rhs),     3 )

        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex, 't4 t1' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex, 't4 t2' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )

        term04 = equation01.rhs[4]
        self.assertEqual( term04.regex, 't4 t3' )
        spec04 = self.helper.display_tree( term04 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    def test_prepend_coeff_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01 = '''
            T1_1
        '''

        spec02 = '''
            T2_2
        '''

        spec03 = '''
            T3_3
        '''

        spec04 = '''
            S_4:T5_5 T6_6
        '''

        term_expected02 = '''
            S_9:T5_7 T6_8 T1_1
        '''

        term_expected03 = '''
            S_13:T5_11 T6_12 T2_2
        '''

        term_expected04 = '''
            S_17:T5_15 T6_16 T3_3

        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = self.helper.construct_ast_from_spec( forrest01, spec02 )
        root03  = self.helper.construct_ast_from_spec( forrest01, spec03 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01
        equation01.rhs[3] = root02
        equation01.rhs[4] = root03

        root04  = self.helper.construct_ast_from_spec( forrest01, spec04 )

        equation01.prepend_coeff(root04)

        self.assertEqual( len(equation01.rhs),     3 )

        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex, 't5 t6 t1' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex, 't5 t6 t2' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )

        term04 = equation01.rhs[4]
        self.assertEqual( term04.regex, 't5 t6 t3' )
        spec04 = self.helper.display_tree( term04 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    def test_prepend_coeff_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01 = '''
            S_1:T2_2 T3_3
        '''

        spec02 = '''
            S_4:T5_5 T6_6
        '''

        spec03 = '''
            S_7:T8_8 T9_9
        '''

        spec04 = '''
            T10_10
        '''

        term_expected02 = '''
            S_11:T10_10 T2_2 T3_3
        '''


        term_expected03 = '''
            S_13:T10_12 T5_5 T6_6
        '''

        term_expected04 = '''
            S_15:T10_14 T8_8 T9_9
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = self.helper.construct_ast_from_spec( forrest01, spec02 )
        root03  = self.helper.construct_ast_from_spec( forrest01, spec03 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01
        equation01.rhs[3] = root02
        equation01.rhs[4] = root03

        root04  = self.helper.construct_ast_from_spec( forrest01, spec04 )

        equation01.prepend_coeff(root04)

        self.assertEqual( len(equation01.rhs),     3 )

        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex, 't10 t2 t3' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex, 't10 t5 t6' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )

        term04 = equation01.rhs[4]
        self.assertEqual( term04.regex, 't10 t8 t9' )
        spec04 = self.helper.display_tree( term04 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    def test_prepend_coeff_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01 = '''
            S_1:T2_2 T3_3
        '''

        spec02 = '''
            S_4:T5_5 T6_6
        '''

        spec03 = '''
            S_7:T8_8 T9_9
        '''

        spec04 = '''
            S_10:T11_11 T12_12
        '''

        term_expected02 = '''
            S_15:T11_13 T12_14 T2_2 T3_3
        '''


        term_expected03 = '''
            S_19:T11_17 T12_18 T5_5 T6_6
        '''

        term_expected04 = '''
            S_23:T11_21 T12_22 T8_8 T9_9
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = self.helper.construct_ast_from_spec( forrest01, spec02 )
        root03  = self.helper.construct_ast_from_spec( forrest01, spec03 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01
        equation01.rhs[3] = root02
        equation01.rhs[4] = root03

        root04  = self.helper.construct_ast_from_spec( forrest01, spec04 )

        equation01.prepend_coeff(root04)

        self.assertEqual( len(equation01.rhs),     3 )

        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex, 't11 t12 t2 t3' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex, 't11 t12 t5 t6' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )

        term04 = equation01.rhs[4]
        self.assertEqual( term04.regex, 't11 t12 t8 t9' )
        spec04 = self.helper.display_tree( term04 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    def test_prepend_coeff_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01 = '''
            S_1:T2_2 T3_3
        '''

        spec02 = '''
            |_4:T5_5 T6_6
        '''

        spec03 = '''
            *_7:S_8
            S_8:T9_9 T10_10
        '''

        spec04 = '''
            *_11:S_12
            S_12:T13_13 T14_14
        '''

        term_expected02 = '''
            S_18:*_14 T2_2 T3_3
            *_14:S_15
            S_15:T13_16 T14_17
        '''

        term_expected03 = '''
            S_23:*_19 |_4
            *_19:S_20
            S_20:T13_21 T14_22
            |_4:T5_5 T6_6
        '''

        term_expected04 = '''
            S_28:*_24 *_7
            *_24:S_25
            S_25:T13_26 T14_27
            *_7:S_8
            S_8:T9_9 T10_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = self.helper.construct_ast_from_spec( forrest01, spec02 )
        root03  = self.helper.construct_ast_from_spec( forrest01, spec03 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01
        equation01.rhs[3] = root02
        equation01.rhs[4] = root03

        root04  = self.helper.construct_ast_from_spec( forrest01, spec04 )

        equation01.prepend_coeff(root04)

        self.assertEqual( len(equation01.rhs),     3 )

        term02 = equation01.rhs[2]
        self.assertEqual( term02.regex, '( t13 t14 ) * t2 t3' )
        spec02 = self.helper.display_tree( term02 )
        self.assertEqual( self.helper.compare_specs( spec02, term_expected02 ), True )

        term03 = equation01.rhs[3]
        self.assertEqual( term03.regex, '( t13 t14 ) * ( t5 | t6 )' )
        spec03 = self.helper.display_tree( term03 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )

        term04 = equation01.rhs[4]
        self.assertEqual( term04.regex, '( t13 t14 ) * ( t9 t10 ) *' )
        spec04 = self.helper.display_tree( term04 )
        self.assertEqual( self.helper.compare_specs( spec03, term_expected03 ), True )


    def test_merge_into_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            E_1
        '''

        spec02_01 = '''
            E_2
        '''

        term_expected01 = '''
            E_1
        '''


        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            E_1
        '''

        spec02_01 = '''
            T1_2
        '''

        term_expected01 = '''
            |_2:E_1 T1_2
        '''


        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            T1_1
        '''

        spec02_01 = '''
            T1_2
        '''

        term_expected01 = '''
            T1_1
        '''


        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            T1_0
        '''

        spec02_01 = '''
            T2_1
        '''

        term_expected01 = '''
            |_2:T1_0 T2_1
        '''


        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            S_0:T1_1 T2_2
        '''

        spec02_01 = '''
            S_3:T4_4 T5_5
        '''

        term_expected01 = '''
            |_6:S_0 S_3
            S_0:T1_1 T2_2
            S_3:T4_4 T5_5
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )


    def test_merge_into_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2
        '''

        spec02_01 = '''
            S_3:T4_4 T5_5
        '''

        term_expected01 = '''
            |_6:T1_1 T2_2 S_3
            S_3:T4_4 T5_5
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0007( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            S_0:T1_1 T2_2
        '''

        spec02_01 = '''
            |_3:T4_4 T5_5
        '''

        term_expected01 = '''
            |_6:S_0 T4_4 T5_5
            S_0:T1_1 T2_2
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0008( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2
        '''

        spec02_01 = '''
            |_3:T4_4 T5_5
        '''

        term_expected01 = '''
            |_6:T1_1 T2_2 T4_4 T5_5
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0009( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2 T3_3
        '''

        spec02_01 = '''
            |_3:T4_4 T5_5 T6_6
        '''

        term_expected01 = '''
            |_8:T1_1 T2_2 T3_3 T4_4 T5_5 T6_6
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0010( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2 S_3
            S_3:T4_4 T5_5
        '''

        spec02_01 = '''
            |_3:T4_4 T5_5 T6_6
        '''

        term_expected01 = '''
            |_10:T1_1 T2_2 T4_4 S_3 T5_5 T6_6
            S_3:T4_4 T5_5
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0011( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2 S_3
            S_3:T4_4 T5_5
        '''

        spec02_01 = '''
            |_3:T4_4 T5_5 S_6 T7_7
            S_6:T8_8 T9_9
        '''

        term_expected01 = '''
            |_13:T1_1 T2_2 T4_4 S_3 T5_5 T7_7 S_6
            S_3:T4_4 T5_5
            S_6:T8_8 T9_9
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root02_01  = self.helper.construct_ast_from_spec( forrest01, spec02_01 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[2] = root01_01

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_01

        equation01.merge_into( equation02 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[2] )
#        print(spec01_01_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
 

    def test_merge_into_0012( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            S_0:T1_1 T2_2
        '''

        spec01_02 = '''
            S_3:T4_4 T5_5
        '''

        spec01_03 = '''
            S_6:T7_7 T8_8
        '''

        spec02_02 = '''
            S_9:T10_10 T11_11
        '''

        spec02_03 = '''
            S_12:T13_13 T14_14
        '''

        spec02_04 = '''
            S_15:T16_16 T17_17
        '''

        term_expected01 = '''
            S_0:T1_1 T2_2
        '''

        term_expected02 = '''
            |_18:S_9 S_3
            S_9:T10_10 T11_11
            S_3:T4_4 T5_5
        '''

        term_expected03 = '''
            |_19:S_12 S_6
            S_12:T13_13 T14_14
            S_6:T7_7 T8_8
        '''

        term_expected04 = '''
            S_15:T16_16 T17_17
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root01_02  = self.helper.construct_ast_from_spec( forrest01, spec01_02 )
        root01_03  = self.helper.construct_ast_from_spec( forrest01, spec01_03 )

        root02_02  = self.helper.construct_ast_from_spec( forrest01, spec02_02 )
        root02_03  = self.helper.construct_ast_from_spec( forrest01, spec02_03 )
        root02_04  = self.helper.construct_ast_from_spec( forrest01, spec02_04 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation01.rhs[1] = root01_01
        equation01.rhs[2] = root01_02
        equation01.rhs[3] = root01_03

        equation02 = nlpregex.regular_language.sse_solver.SymbolicEquation( 1, forrest01 )
        equation02.rhs[2] = root02_02
        equation02.rhs[3] = root02_03
        equation02.rhs[4] = root02_04

        equation01.merge_into( equation02 )

        self.assertEqual( len(equation01.rhs), 4 )

        spec01_01_after = self.helper.display_tree( equation01.rhs[1] )
        spec01_02_after = self.helper.display_tree( equation01.rhs[2] )
        spec01_03_after = self.helper.display_tree( equation01.rhs[3] )
        spec01_04_after = self.helper.display_tree( equation01.rhs[4] )
#        print(spec01_04_after)
        self.assertEqual( self.helper.compare_specs( spec01_01_after, term_expected01 ), True )
        self.assertEqual( self.helper.compare_specs( spec01_02_after, term_expected02 ), True )
        self.assertEqual( self.helper.compare_specs( spec01_03_after, term_expected03 ), True ) 
        self.assertEqual( self.helper.compare_specs( spec01_04_after, term_expected04 ), True ) 


    def test_clone_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2 S_3
            S_3:T4_4 T5_5
        '''

        spec01_02 = '''
            S_3:T6_6 T7_7
        '''

        spec01_03 = '''
            S_8:T9_9 T10_10
        '''

        spec01_04 = '''
            S_11:T12_12 T13_13
        '''

        spec02_01_expected = '''
            |_15:T1_16 T2_17 S_18
            S_18:T4_19 T5_20
        '''

        spec02_02_expected = '''
            S_21:T6_22 T7_23
        '''

        spec02_03_expected = '''
            S_24:T9_25 T10_26
        '''

        spec02_04_expected = '''
            S_27:T12_28 T13_29
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root01_02  = self.helper.construct_ast_from_spec( forrest01, spec01_02 )
        root01_03  = self.helper.construct_ast_from_spec( forrest01, spec01_03 )
        root01_04  = self.helper.construct_ast_from_spec( forrest01, spec01_04 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 11, forrest01 )
        equation01.rhs[1] = root01_01
        equation01.rhs[2] = root01_02
        equation01.rhs[3] = root01_03
        equation01.rhs[4] = root01_04


        
        equation02 = equation01.clone()

        self.assertEqual( len(equation02.rhs), 4 )

        spec02_01 = self.helper.display_tree( equation02.rhs[1] )
        spec02_02 = self.helper.display_tree( equation02.rhs[2] )
        spec02_03 = self.helper.display_tree( equation02.rhs[3] )
        spec02_04 = self.helper.display_tree( equation02.rhs[4] )

        self.assertEqual( equation02.lhs, 11 )
        self.assertEqual( self.helper.compare_specs( spec02_01, spec02_01_expected ), True )
        self.assertEqual( self.helper.compare_specs( spec02_02, spec02_02_expected ), True )
        self.assertEqual( self.helper.compare_specs( spec02_03, spec02_03_expected ), True )
        self.assertEqual( self.helper.compare_specs( spec02_04, spec02_04_expected ), True )


    def test_clean_RHS_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2 S_3
            S_3:T4_4 T5_5
        '''

        spec01_02 = '''
            S_3:T6_6 T7_7
        '''

        spec01_03 = '''
            S_8:T9_9 T10_10
        '''

        spec01_04 = '''
            S_11:T12_12 T13_13
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root01_02  = self.helper.construct_ast_from_spec( forrest01, spec01_02 )
        root01_03  = self.helper.construct_ast_from_spec( forrest01, spec01_03 )
        root01_04  = self.helper.construct_ast_from_spec( forrest01, spec01_04 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 11, forrest01 )
        equation01.rhs[1] = root01_01
        equation01.rhs[2] = root01_02
        equation01.rhs[3] = root01_03
        equation01.rhs[4] = root01_04

        
        equation01.clean_RHS()

        self.assertEqual( len(equation01.rhs),   0 )
        self.assertEqual( forrest01.num_nodes(), 0 )
        self.assertEqual( forrest01.num_edges(), 0 )


    def test_remove_term_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             

        spec01_01 = '''
            |_0:T1_1 T2_2 S_3
            S_3:T4_4 T5_5
        '''

        spec01_02 = '''
            S_3:T6_6 T7_7
        '''

        spec01_03 = '''
            S_8:T9_9 T10_10
        '''

        spec01_04 = '''
            S_11:T12_12 T13_13
        '''

        root01_01  = self.helper.construct_ast_from_spec( forrest01, spec01_01 )
        root01_02  = self.helper.construct_ast_from_spec( forrest01, spec01_02 )
        root01_03  = self.helper.construct_ast_from_spec( forrest01, spec01_03 )
        root01_04  = self.helper.construct_ast_from_spec( forrest01, spec01_04 )

        equation01 = nlpregex.regular_language.sse_solver.SymbolicEquation( 11, forrest01 )
        equation01.rhs[1] = root01_01
        equation01.rhs[2] = root01_02
        equation01.rhs[3] = root01_03
        equation01.rhs[4] = root01_04

        
        equation01.remove_term(2)

        self.assertEqual( len(equation01.rhs),    3 )
        self.assertEqual( forrest01.num_nodes(), 12 )
        self.assertEqual( forrest01.num_edges(),  9 )


class test_SymbolicSimultaneousEquations( unittest.TestCase ):


    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.helper = test_sse_ASForrest_helper()


    def test_constructor_0001( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        self.assertEqual  ( len(equations01.rows),            0 )
        self.assertEqual  ( equations01.start_state,         -1 )
        self.assertEqual  ( equations01.final_state,         -1 )
        self.assertEqual  ( equations01.forrest.num_nodes(),  0 )
        self.assertEqual  ( equations01.forrest.num_edges(),  0 )
        self.assertIsNone ( equations01.forrest.root            )
        self.assertEqual  ( equations01.diag,             False )


    def test_add_coeff_0001( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['t0'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            T0_0
        '''
#        print(spec_02_03)

        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )
        self.assertEqual( len(equation_03.rhs) , 0 )
        self.assertEqual  ( equations01.forrest.num_nodes(),  1 )
        self.assertEqual  ( equations01.forrest.num_edges(),  0 )


    def test_add_coeff_0002( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['t0'] )
        equations01.add_coeff( 2, 3, ['t0'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            T0_0
        '''
#        print(spec_02_03)

        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )
        self.assertEqual( len(equation_03.rhs) , 0 )
        self.assertEqual  ( equations01.forrest.num_nodes(),  1 )
        self.assertEqual  ( equations01.forrest.num_edges(),  0 )


    def test_add_coeff_0003( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['e'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            E_0
        '''
#        print(spec_02_03)

        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )
        self.assertEqual( len(equation_03.rhs) , 0 )
        self.assertEqual  ( equations01.forrest.num_nodes(),  1 )
        self.assertEqual  ( equations01.forrest.num_edges(),  0 )


    def test_add_coeff_0004( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['t0', 't1'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            |_0:T0_1 T1_2
        '''
#        print(spec_02_03)

        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )
        self.assertEqual( len(equation_03.rhs) , 0 )
        self.assertEqual  ( equations01.forrest.num_nodes(),  3 )
        self.assertEqual  ( equations01.forrest.num_edges(),  2 )


    def test_add_coeff_0005( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['e', 't0'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            |_0:E_1 T0_2
        '''
#        print(spec_02_03)

        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )
        self.assertEqual( len(equation_03.rhs) , 0 )
        self.assertEqual  ( equations01.forrest.num_nodes(),  3 )
        self.assertEqual  ( equations01.forrest.num_edges(),  2 )


    def test_add_coeff_0006( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['t0', 't1'] )
        equations01.add_coeff( 2, 3, ['t1', 't2'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            |_6:T0_1 T1_2 T2_5
        '''
#        print(spec_02_03)

        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )
        self.assertEqual( len(equation_03.rhs) , 0 )
        self.assertEqual  ( equations01.forrest.num_nodes(),  4 )
        self.assertEqual  ( equations01.forrest.num_edges(),  3 )


    def test_add_coeff_0007( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['t0', 't1'] )
        equations01.add_coeff( 3, 2, ['t1', 't2'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            |_0:T0_1 T1_2
        '''
#        print(spec_02_03)
        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )

        self.assertEqual  ( len(equation_03.rhs) , 1 )
        coeff_03_02 = equation_03.rhs[2]
        spec_03_02 = self.helper.display_tree( coeff_03_02 )
        expected_spec_03_02 = '''
            |_3:T1_4 T2_5
        '''
#        print(spec_03_02)
        self.assertEqual( self.helper.compare_specs( spec_03_02, expected_spec_03_02 ), True )


    def test_add_coeff_0007( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, ['t0', 't1'] )
        equations01.add_coeff( 3, 2, ['t1', 't2'] )

        self.assertEqual  ( len(equations01.rows),            2 )
        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 1 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03 = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            |_0:T0_1 T1_2
        '''
#        print(spec_02_03)
        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )

        self.assertEqual  ( len(equation_03.rhs) , 1 )
        coeff_03_02 = equation_03.rhs[2]
        spec_03_02 = self.helper.display_tree( coeff_03_02 )
        expected_spec_03_02 = '''
            |_3:T1_4 T2_5
        '''
#        print(spec_03_02)
        self.assertEqual( self.helper.compare_specs( spec_03_02, expected_spec_03_02 ), True )


    def test_substitute_0001( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 3, [ 't0',  't1'] )
        equations01.add_coeff( 2, 4, [ 't2',  't3'] )
        equations01.add_coeff( 2, 5, [ 't4',  't5'] )

        equations01.add_coeff( 3, 2, [ 't6',  't7'] )
        equations01.add_coeff( 3, 3, [ 't8',  't9'] )
        equations01.add_coeff( 3, 4, ['t10', 't11'] )
        equations01.add_coeff( 3, 5, ['t12', 't13'] )

        equations01.substitute(2, 3)

        self.assertEqual  ( len(equations01.rows),  4 )

        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
        equation_04 = equations01.rows[4]
        equation_05 = equations01.rows[5]
      
        self.assertEqual  ( len(equation_02.rhs) , 3 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03  = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            |_0:T0_1 T1_2
        '''
#        print(spec_02_03)
        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )

        coeff_02_04 = equation_02.rhs[4]
        spec_02_04  = self.helper.display_tree( coeff_02_04 )
        expected_spec_02_04 = '''
            |_3:T2_4 T3_5
        '''
#        print(spec_02_04)
        self.assertEqual( self.helper.compare_specs( spec_02_04, expected_spec_02_04 ), True )

        coeff_02_05 = equation_02.rhs[5]
        spec_02_05  = self.helper.display_tree( coeff_02_05 )
        expected_spec_02_05 = '''
           |_6:T4_7 T5_8
        '''
#        print(spec_02_05)
        self.assertEqual( self.helper.compare_specs( spec_02_05, expected_spec_02_05 ), True )

        self.assertEqual  ( len(equation_03.rhs) , 3 )

        coeff_03_03 = equation_03.rhs[3]
        spec_03_03  = self.helper.display_tree( coeff_03_03 )
        expected_spec_03_03 = '''
            |_42:S_33 T8_13 T9_14
            S_33:|_30 |_21
            |_30:T6_31 T7_32
            |_21:T0_22 T1_23
        '''
#        print(spec_03_03)
        self.assertEqual( self.helper.compare_specs( spec_03_03, expected_spec_03_03 ), True )

        coeff_03_04 = equation_03.rhs[4]
        spec_03_04  = self.helper.display_tree( coeff_03_04 )
        expected_spec_03_04 = '''
            |_43:S_37 T10_16 T11_17
            S_37:|_34 |_24
            |_34:T6_35 T7_36
            |_24:T2_25 T3_26
        '''
#        print(spec_03_04)
        self.assertEqual( self.helper.compare_specs( spec_03_04, expected_spec_03_04 ), True )

        coeff_03_05 = equation_03.rhs[5]
        spec_03_05  = self.helper.display_tree( coeff_03_05 )
        expected_spec_03_05 = '''
            |_44:S_41 T12_19 T13_20
            S_41:|_38 |_27
            |_38:T6_39 T7_40
            |_27:T4_28 T5_29
        '''
#        print(spec_03_05)
        self.assertEqual( self.helper.compare_specs( spec_03_05, expected_spec_03_05 ), True )


    def test_substitute_0002( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 2, 2, [ 't0'] )
        equations01.add_coeff( 2, 3, [ 't1'] )
        equations01.add_coeff( 2, 4, [ 't2'] )
        equations01.add_coeff( 2, 5, [ 't3'] )

        equations01.add_coeff( 3, 2, [ 't4'] )
        equations01.add_coeff( 3, 3, [ 't5'] )
        equations01.add_coeff( 3, 4, [ 't6'] )

        equations01.rows[2].remove_self_recursion()
        equations01.substitute(2, 3)

        self.assertEqual  ( len(equations01.rows),  4 )

        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
        equation_04 = equations01.rows[4]
        equation_05 = equations01.rows[5]
      
        self.assertEqual  ( len(equation_02.rhs) , 3 )
        coeff_02_03 = equation_02.rhs[3]
        spec_02_03  = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            S_11:*_9 T1_1
            *_9:T0_10
        '''
#        print(spec_02_03)
        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )

        coeff_02_04 = equation_02.rhs[4]
        spec_02_04  = self.helper.display_tree( coeff_02_04 )
        expected_spec_02_04 = '''
            S_14:*_12 T2_2
            *_12:T0_13
        '''
#        print(spec_02_04)
        self.assertEqual( self.helper.compare_specs( spec_02_04, expected_spec_02_04 ), True )

        coeff_02_05 = equation_02.rhs[5]
        spec_02_05  = self.helper.display_tree( coeff_02_05 )
        expected_spec_02_05 = '''
            S_17:*_15 T3_3
            *_15:T0_16
        '''
#        print(spec_02_05)
        self.assertEqual( self.helper.compare_specs( spec_02_05, expected_spec_02_05 ), True )

        self.assertEqual  ( len(equation_03.rhs) , 3 )

        coeff_03_03 = equation_03.rhs[3]
        spec_03_03  = self.helper.display_tree( coeff_03_03 )
        expected_spec_03_03 = '''
            |_36:S_31 T5_5
            S_31:T4_30 *_19 T1_21
            *_19:T0_20
        '''
#        print(spec_03_03)
        self.assertEqual( self.helper.compare_specs( spec_03_03, expected_spec_03_03 ), True )

        coeff_03_04 = equation_03.rhs[4]
        spec_03_04  = self.helper.display_tree( coeff_03_04 )
        expected_spec_03_04 = '''
            |_37:S_33 T6_6
            S_33:T4_32 *_23 T2_25
            *_23:T0_24
        '''
#        print(spec_03_04)
        self.assertEqual( self.helper.compare_specs( spec_03_04, expected_spec_03_04 ), True )

        coeff_03_05 = equation_03.rhs[5]
        spec_03_05  = self.helper.display_tree( coeff_03_05 )
        expected_spec_03_05 = '''
            S_35:T4_34 *_27 T3_29
            *_27:T0_28
        '''
#        print(spec_03_05)
        self.assertEqual( self.helper.compare_specs( spec_03_05, expected_spec_03_05 ), True )


    def test_eliminate_row_0001( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 1, 1, [ 't0'] )
        equations01.add_coeff( 1, 2, [ 't1'] )
        equations01.add_coeff( 1, 3, [ 't2'] )
        equations01.add_coeff( 2, 1, [ 't3'] )
        equations01.add_coeff( 2, 2, [ 't4'] )
        equations01.add_coeff( 2, 3, [ 't5'] )
        equations01.add_coeff( 3, 1, [ 't6'] )
        equations01.add_coeff( 3, 2, [ 't7'] )
        equations01.add_coeff( 3, 3, [ 't8'] )

        equations01.eliminate_row(1)

        self.assertEqual  ( len(equations01.rows),  2 )

        equation_02 = equations01.rows[2]
        equation_03 = equations01.rows[3]
      
        self.assertEqual  ( len(equation_02.rhs) , 2 )
        coeff_02_02 = equation_02.rhs[2]
        spec_02_02  = self.helper.display_tree( coeff_02_02 )
        expected_spec_02_02 = '''
            |_29:S_26 T4_4
            S_26:T3_25 *_18 T1_20
            *_18:T0_19
        '''
#        print(spec_02_02)
        self.assertEqual( self.helper.compare_specs( spec_02_02, expected_spec_02_02 ), True )

        coeff_02_03 = equation_02.rhs[3]
        spec_02_03  = self.helper.display_tree( coeff_02_03 )
        expected_spec_02_03 = '''
            |_30:S_28 T5_5
            S_28:T3_27 *_22 T2_24
            *_22:T0_23
        '''
#        print(spec_02_03)
        self.assertEqual( self.helper.compare_specs( spec_02_03, expected_spec_02_03 ), True )

        self.assertEqual  ( len(equation_03.rhs) , 2 )
        coeff_03_02 = equation_03.rhs[2]
        spec_03_02  = self.helper.display_tree( coeff_03_02 )
        expected_spec_03_02 = '''
            |_43:S_40 T7_7
            S_40:T6_39 *_32 T1_34
            *_32:T0_33
        '''
#        print(spec_03_02)
        self.assertEqual( self.helper.compare_specs( spec_03_02, expected_spec_03_02 ), True )

        coeff_03_03 = equation_03.rhs[3]
        spec_03_03  = self.helper.display_tree( coeff_03_03 )
        expected_spec_03_03 = '''
            |_44:S_42 T8_8
            S_42:T6_41 *_36 T2_38
            *_36:T0_37
        '''
#        print(spec_03_03)
        self.assertEqual( self.helper.compare_specs( spec_03_03, expected_spec_03_03 ), True )


    def test_solve_0001( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 1, 1, [ 't0'] )
        equations01.add_coeff( 1, 2, [ 't1'] )
        equations01.add_coeff( 1, 3, [ 't2'] )
        equations01.add_coeff( 2, 1, [ 't3'] )
        equations01.add_coeff( 2, 2, [ 't4'] )
        equations01.add_coeff( 2, 3, [ 't5'] )
        equations01.add_coeff( 3, 1, [ 't6'] )
        equations01.add_coeff( 3, 2, [ 't7'] )
        equations01.add_coeff( 3, 3, [ 't8'] )

        forrest01 = equations01.solve(1, [2,3])
        root01 = forrest01.root
        ast01 = root01.children_map['n0']
#        print(ast01.regex)
        expected_spec_01 = '''
            |_296:S_295 S_156
            S_295:|_271 *_222 ?_253
            |_271:S_272 S_291
            S_272:*_273 T1_275 *_276 |_284
            *_273:T0_274
            *_276:|_277
            |_277:S_278 T4_283
            S_278:T3_279 *_280 T1_282
            *_280:T0_281
            |_284:S_285 T5_290
            S_285:T3_286 *_287 T2_289
            *_287:T0_288
            S_291:*_292 T2_294
            *_292:T0_293
            *_222:|_223
            |_223:S_224 S_247 T8_252
            S_224:|_225 *_232 |_240
            |_225:S_226 T7_231
            S_226:T6_227 *_228 T1_230
            *_228:T0_229
            *_232:|_233
            |_233:S_234 T4_239
            S_234:T3_235 *_236 T1_238
            *_236:T0_237
            |_240:S_241 T5_246
            S_241:T3_242 *_243 T2_245
            *_243:T0_244
            S_247:T6_248 *_249 T2_251
            *_249:T0_250
            ?_253:S_297
            S_297:|_255 *_262
            |_255:S_256 T7_261
            S_256:T6_257 *_258 T1_260
            *_258:T0_259
            *_262:|_263
            |_263:S_264 T4_269
            S_264:T3_265 *_266 T1_268
            *_266:T0_267
            S_156:*_153 T1_155 *_139
            *_153:T0_154
            *_139:|_140
            |_140:S_141 T4_146
            S_141:T3_142 *_143 T1_145
            *_143:T0_144
        '''

        spec_01 = self.helper.display_tree( ast01 )
#        print(spec_01)
        self.assertEqual( self.helper.compare_specs( spec_01, expected_spec_01 ), True )


    def test_solve_0002( self ):

        equations01 = nlpregex.regular_language.sse_solver.SymbolicSimultaneousEquations(False)

        equations01.add_coeff( 1, 2, [ 't0'] )
        equations01.add_coeff( 2, 2, [ 't1'] )
        equations01.add_coeff( 2, 3, [ 't2'] )

        forrest01 = equations01.solve(1, [3])
        root01 = forrest01.root
        ast01 = root01.children_map['n0']
#        print(ast01.regex)
        expected_spec_01 = '''
            S_18:T0_19 *_20 T2_22
            *_20:T1_21
        '''

        spec_01 = self.helper.display_tree( ast01 )
#        print(spec_01)
        self.assertEqual( self.helper.compare_specs( spec_01, expected_spec_01 ), True )


if __name__ == '__main__':
    unittest.main()

