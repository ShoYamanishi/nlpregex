#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for fa.py."""

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.fa
import nlpregex.regular_language.sse_forrest

class test_FA( unittest.TestCase ):


    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)


    def _test_0001( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_epsilon()

#        fa01.draw('test_0001', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa01.to_open_fst()
        print (five_strs01[0])
        print (five_strs01[1])
        print (five_strs01[2])
        print (five_strs01[3])
        print (five_strs01[4])

        fa02 = nlpregex.regular_language.fa.FA()
        fa02.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
#        fa02.draw('test_0001', show_out_token = True, view_now = True, out_format = "pdf" )

        da01 = nlpregex.regular_language.fa.DFA_from_NFA( fa01 )
        da01.draw('test_0001', show_out_token = True, view_now = True, out_format = "pdf" )                


    def _test_0002( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_01', '' )

#        fa01.draw('test_0002', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa01.to_open_fst()
        print (five_strs01[0])
        print (five_strs01[1])
        print (five_strs01[2])
        print (five_strs01[3])
        print (five_strs01[4])

        fa02 = nlpregex.regular_language.fa.FA()
        fa02.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
#        fa02.draw('test_0002', show_out_token = True, view_now = True, out_format = "pdf" )

        da01 = nlpregex.regular_language.fa.DFA_from_NFA( fa01 )
        da01.draw('test_0002', show_out_token = True, view_now = True, out_format = "pdf" )                


    def _test_0003( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_01', 'out_token_01' )

#        fa01.draw('test_0003', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa01.to_open_fst()
#        print (five_strs01[0])
#        print (five_strs01[1])
#        print (five_strs01[2])
#        print (five_strs01[3])
#        print (five_strs01[4])

        fa02 = nlpregex.regular_language.fa.FA()
        fa02.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
#        fa02.draw('test_0003', show_out_token = True, view_now = True, out_format = "pdf" )

        da01 = nlpregex.regular_language.fa.DFA_from_NFA( fa01 )
#        da01.draw('test_0003_da01', show_out_token = True, view_now = True, out_format = "pdf" )

        da02 = nlpregex.regular_language.fa.decode( da01, ['in_token_01'] )
        print ( 'decoded: [' + str(da02) + ']' )


    def _test_0004( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_01', 'out_token_01' )

#        fa01.draw('test_0001', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa01.to_open_fst()
#        print (five_strs01[0])
#        print (five_strs01[1])
#        print (five_strs01[2])
#        print (five_strs01[3])
#        print (five_strs01[4])

        fa02 = nlpregex.regular_language.fa.FA()
        fa02.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
#        fa02.draw('test_0004', show_out_token = True, view_now = True, out_format = "pdf" )

        da01 = nlpregex.regular_language.fa.DFA_from_NFA( fa01 )
#        da01.draw('test_0004_da01', show_out_token = True, view_now = True, out_format = "pdf" )

        str01 = nlpregex.regular_language.fa.decode( da01, ['in_token_non_existent'] )
        print ( 'decoded: [' + str(str01) + ']' )


    def _test_0005( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_01', 'out_token_01' )
        fa02 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_02', 'out_token_02' )
        fa03 = nlpregex.regular_language.fa.ttsp_concatenate( [fa01, fa02] )

#        fa03.draw('test_0005', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa03.to_open_fst()
        print (five_strs01[0])
        print (five_strs01[1])
        print (five_strs01[2])
        print (five_strs01[3])
        print (five_strs01[4])

        fa04 = nlpregex.regular_language.fa.FA()
        fa04.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
        fa04.draw('test_0005_fa04', show_out_token = True, view_now = True, out_format = "pdf" )

        da04 = nlpregex.regular_language.fa.DFA_from_NFA( fa04 )
        da04.draw('test_0005_da04', show_out_token = True, view_now = True, out_format = "pdf" )

        str01 = nlpregex.regular_language.fa.decode( da04, ['in_token_01', 'in_token_02'] )
        print ( 'decoded: [' + str( str01 ) + ']' )


    def _test_0006( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_01', 'out_token_01' )
        fa02 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_02', 'out_token_02' )
        fa03 = nlpregex.regular_language.fa.ttsp_concatenate( [fa01, fa02] )

#        fa03.draw('test_0006', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa03.to_open_fst()
        print (five_strs01[0])
        print (five_strs01[1])
        print (five_strs01[2])
        print (five_strs01[3])
        print (five_strs01[4])

        fa04 = nlpregex.regular_language.fa.FA()
        fa04.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
        fa04.draw('test_0006_fa04', show_out_token = True, view_now = True, out_format = "pdf" )

        da04 = nlpregex.regular_language.fa.DFA_from_NFA( fa04 )
        da04.draw('test_0006_da04', show_out_token = True, view_now = True, out_format = "pdf" )

        str01 = nlpregex.regular_language.fa.decode( da04, ['in_token_01'] )
        print ( 'decoded: [' + str( str01 ) + ']' )



    def _test_0007( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_01', 'out_token_01' )
        fa02 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_02', 'out_token_02' )
        fa03 = nlpregex.regular_language.fa.ttsp_concatenate( [fa01, fa02] )
        fa04 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_03', 'out_token_03' )
        fa05 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_04', 'out_token_04' )
        fa06 = nlpregex.regular_language.fa.ttsp_concatenate( [fa04, fa05] )
        fa07 = nlpregex.regular_language.fa.ttsp_bundle( [fa03, fa06] )

#        fa07.draw('test_0007', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa07.to_open_fst()
        print (five_strs01[0])
        print (five_strs01[1])
        print (five_strs01[2])
        print (five_strs01[3])
        print (five_strs01[4])

        fa08 = nlpregex.regular_language.fa.FA()
        fa08.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
        fa08.draw('test_0007_fa08', show_out_token = True, view_now = True, out_format = "pdf" )

        da08 = nlpregex.regular_language.fa.DFA_from_NFA( fa08 )
        da08.draw('test_0007_da08', show_out_token = True, view_now = True, out_format = "pdf" )

        str01 = nlpregex.regular_language.fa.decode( da08, ['in_token_03','in_token_04' ] )
        print ( 'decoded: [' + str( str01 ) + ']' )


    def test_0008( self ):

        fa01 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_01', '' )
        fa02 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_02', '' )
        fa03 = nlpregex.regular_language.fa.ttsp_concatenate( [fa01, fa02] )
        fa04 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_03', '' )
        fa05 = nlpregex.regular_language.fa.make_unit_transition( 'in_token_04', '' )
        fa06 = nlpregex.regular_language.fa.ttsp_concatenate( [fa04, fa05] )
        fa07 = nlpregex.regular_language.fa.ttsp_bundle( [fa03, fa06] )
        fa08 = nlpregex.regular_language.fa.enclose_in_cycle( fa07, '*' )

#        fa08.draw('test_0008', show_out_token = True, view_now = True, out_format = "pdf" )
        five_strs01 = fa08.to_open_fst()
        print (five_strs01[0])
        print (five_strs01[1])
        print (five_strs01[2])
        print (five_strs01[3])
        print (five_strs01[4])

        fa09 = nlpregex.regular_language.fa.FA()
        fa09.from_open_fst( five_strs01[0], five_strs01[3],  five_strs01[4] )
        fa09.draw('test_0008_fa08', show_out_token = True, view_now = True, out_format = "pdf" )

        da09 = nlpregex.regular_language.fa.DFA_from_NFA( fa09 )
        da09.draw('test_0008_da08', show_out_token = True, view_now = True, out_format = "pdf" )

        str01 = nlpregex.regular_language.fa.decode( da09, [ 'in_token_03','in_token_04', 'in_token_01','in_token_02',  'in_token_03','in_token_04', 'in_token_01','in_token_02' ] )

        print ( 'decoded: [' + str( str01 ) + ']' )







if __name__ == '__main__':
    unittest.main()
