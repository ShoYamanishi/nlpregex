#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for lark_parser.py."""

import unittest
import nlpregex.regular_language.lark_parser
from nlpregex.regular_language.fa import DFA_from_NFA

class test_lark_parser( unittest.TestCase ):

    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)


    def test_0001(self):

        spec01 = ''
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        self.assertEqual( len(ASTs), 0 )


    def test_0002(self):

        spec01 = '<nt01>:t02;'
        spec_expected = 't02'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        

    def test_0002b(self):

        spec01 = '<nt01>:t02 [token01 token02];'
        spec_expected = 't02 [ token01 token02 ]'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0003(self):

        spec01 = '<nt01>:t02;'
        spec_expected = 't02'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0004(self):

        spec01 = '<nt01>:t02 t03;'
        spec_expected = 't02 t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0004b(self):

        spec01 = '<nt01>:t02 [token01 token02] t03;'
        spec_expected = 't02 [ token01 token02 ] t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0004c(self):

        spec01 = '<nt01>:t02 t03[token01 token02];'
        spec_expected = 't02 t03 [ token01 token02 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0004d(self):

        spec01 = '<nt01>:t02 [token01 token02] t03 [token03 token04];'
        spec_expected = 't02 [ token01 token02 ] t03 [ token03 token04 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0005(self):

        spec01 = '<nt01>:<nt02>;'
        spec_expected = '<nt02>'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0005a(self):

        spec01 = '<nt01>:<nt02> [token01];'
        spec_expected = '<nt02> [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0006(self):

        spec01 = '<nt01>:<nt02> <nt03>;'
        spec_expected = '<nt02> <nt03>'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0006b(self):

        spec01 = '<nt01>:<nt02> [token01]<nt03>;'
        spec_expected = '<nt02> [ token01 ] <nt03>'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0006c(self):

        spec01 = '<nt01>:<nt02> <nt03>[token01];'
        spec_expected = '<nt02> <nt03> [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0006d(self):

        spec01 = '<nt01>:<nt02> [token01]<nt03>[token02];'
        spec_expected = '<nt02> [ token01 ] <nt03> [ token02 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0006e(self):

        spec01 = '<nt01>:(<nt02> <nt03>)[token02];'
        spec_expected = '( <nt02> <nt03> ) [ token02 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0006f(self):

        spec01 = '<nt01>:(<nt02> [token01]<nt03>[token02])[token03];'
        spec_expected = '( <nt02> [ token01 ] <nt03> [ token02 ] ) [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0007(self):

        spec01 = '<nt01>:<nt02> <nt03>;'
        spec_expected = '<nt02> <nt03>'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0008(self):

        spec01 = '<nt01>:( <nt02> | <nt03> );'
        spec_expected = '( <nt02> | <nt03> )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0008b(self):

        spec01 = '<nt01>:( <nt02>[token01] | <nt03> );'
        spec_expected = '( <nt02> [ token01 ] | <nt03> )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0008c(self):

        spec01 = '<nt01>:( <nt02> | <nt03> [token01]);'
        spec_expected = '( <nt02> | <nt03> [ token01 ] )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0008d(self):

        spec01 = '<nt01>:( <nt02> [token01]| <nt03> [token02]);'
        spec_expected = '( <nt02> [ token01 ] | <nt03> [ token02 ] )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        
        fst03 = DFA_from_NFA(fst01, True)
#        fst03.draw('dfa2', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0008e(self):

        spec01 = '<nt01>:( <nt02> [token01]| <nt03> [token02])[token03];'
        spec_expected = '( <nt02> [ token01 ] | <nt03> [ token02 ] ) [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        
        fst03 = DFA_from_NFA(fst01, True)
#        fst03.draw('dfa2', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0009(self):

        spec01 = '<nt01>:( t02 | t03 );'
        spec_expected = '( t02 | t03 )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0009b(self):

        spec01 = '<nt01>:( t02[token01] | t03 );'
        spec_expected = '( t02 [ token01 ] | t03 )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0009c(self):

        spec01 = '<nt01>:( t02 | t03 [token01]);'
        spec_expected = '( t02 | t03 [ token01 ] )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0009e(self):

        spec01 = '<nt01>:( t02 | t03) [token01];'
        spec_expected = '( t02 | t03 ) [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0009f(self):

        spec01 = '<nt01>:( t02 [token01]| t03[token02]) [token03];'
        spec_expected = '( t02 [ token01 ] | t03 [ token02 ] ) [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0010(self):

        spec01 = '<nt01>:t02? t03;'
        spec_expected = 't02? t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0010b(self):

        spec01 = '<nt01>:(t02 [token01])? t03;'
        spec_expected = '( t02 [ token01 ] )? t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0010c(self):

        spec01 = '<nt01>:(t02?)[token01] t03;'
        spec_expected = '( t02? ) [ token01 ] t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0010d(self):

        spec01 = '<nt01>:t02? t03 [token01];'
        spec_expected = 't02? t03 [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0010e(self):

        spec01 = '<nt01>:(t02? t03 )[token01];'
        spec_expected = '( t02? t03 ) [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0010f(self):

        spec01 = '<nt01>:(((t02 [token01])?)[token02] t03 [token03])[token04];'
        spec_expected = '( ( ( t02 [ token01 ] )? ) [ token02 ] t03 [ token03 ] ) [ token04 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0011(self):

        spec01 = '<nt01>:t02{0,1} t03;'
        spec_expected = 't02? t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0011b(self):

        spec01 = '<nt01>:(t02[token01]){0,1} t03;'
        spec_expected = '( t02 [ token01 ] )? t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0012(self):

        spec01 = '<nt01>:( t02 t03 )?;'
        spec_expected = '( t02 t03 )?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0012b(self):

        spec01 = '<nt01>:( t02 [token01] t03 )?;'
        spec_expected = '( t02 [ token01 ] t03 )?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0012c(self):

        spec01 = '<nt01>:( t02 [token01] t03 [token02] )?;'
        spec_expected = '( t02 [ token01 ] t03 [ token02 ] )?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0012d(self):

        spec01 = '<nt01>:(( t02 t03 ) [token01])?;'
        spec_expected = '( ( t02 t03 ) [ token01 ] )?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0012e(self):

        spec01 = '<nt01>:((( t02[token01] t03[token02] ) [token03])?)[token04];'
        spec_expected = '( ( ( t02 [ token01 ] t03 [ token02 ] ) [ token03 ] )? ) [ token04 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0013(self):

        spec01 = '<nt01>:( t02 t03 ){0,1};'
        spec_expected = '( t02 t03 )?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0013b(self):

        spec01 = '<nt01>:((( t02[token01] t03[token02] ) [token03]){0,1})[token04];'
        spec_expected = '( ( ( t02 [ token01 ] t03 [ token02 ] ) [ token03 ] )? ) [ token04 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0014(self):

        spec01 = '<nt01>:t02* t03;'
        spec_expected = 't02* t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0014b(self):

        spec01 = '<nt01>:(t02 [token01])* t03;'
        spec_expected = '( t02 [ token01 ] )* t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0014c(self):

        spec01 = '<nt01>:t02* t03[token01];'
        spec_expected = 't02* t03 [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0014d(self):

        spec01 = '<nt01>:(t02[token01])* t03[token02];'
        spec_expected = '( t02 [ token01 ] )* t03 [ token02 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0014e(self):

        spec01 = '<nt01>:((t02[token01])*)[token02] t03[token03];'
        spec_expected = '( ( t02 [ token01 ] )* ) [ token02 ] t03 [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0014f(self):

        spec01 = '<nt01>:[token04](((t02[token01])*)[token02] t03[token03])[token05];'
        spec_expected = '[ token04 ] ( ( ( t02 [ token01 ] )* ) [ token02 ] t03 [ token03 ] ) [ token05 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0014z(self):

        spec01 = '<nt01>:t02* ((t03 [token01])[token02])[token03];'
        spec_expected = 't02* t03 [ token01 token02 token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0015(self):

        spec01 = '<nt01>:t02 t03*;'
        spec_expected = 't02 t03*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0015b(self):

        spec01 = '<nt01>:t02 [token01]t03*;'
        spec_expected = 't02 [ token01 ] t03*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0015c(self):

        spec01 = '<nt01>:t02 (t03[token01])*;'
        spec_expected = 't02 ( t03 [ token01 ] )*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0015d(self):

        spec01 = '<nt01>:t02 (t03*)[token01];'
        spec_expected = 't02 ( t03* ) [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0015e(self):

        spec01 = '<nt01>:t02 [token01] (t03[token02])*;'
        spec_expected = 't02 [ token01 ] ( t03 [ token02 ] )*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0015f(self):

        spec01 = '<nt01>:t02 [token01] ((t03[token02])*)[token03];'
        spec_expected = 't02 [ token01 ] ( ( t03 [ token02 ] )* ) [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0015g(self):

        spec01 = '<nt01>:[token04](t02 [token01] ((t03[token02])*)[token03])[token05];'
        spec_expected = '[ token04 ] ( t02 [ token01 ] ( ( t03 [ token02 ] )* ) [ token03 ] ) [ token05 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0016(self):

        spec01 = '<nt01>:(t02 t03)*;'
        spec_expected = '( t02 t03 )*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0016b(self):

        spec01 = '<nt01>:(t02[token01] t03)*;'
        spec_expected = '( t02 [ token01 ] t03 )*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0016c(self):

        spec01 = '<nt01>:(t02 t03[token01])*;'
        spec_expected = '( t02 t03 [ token01 ] )*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0016d(self):

        spec01 = '<nt01>:(t02[token01] t03[token02])*;'
        spec_expected = '( t02 [ token01 ] t03 [ token02 ] )*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0016e(self):

        spec01 = '<nt01>:((t02[token01] t03[token02])*)[token03];'
        spec_expected = '( ( t02 [ token01 ] t03 [ token02 ] )* ) [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0017(self):

        spec01 = '<nt01>:t02+ t03;'
        spec_expected = 't02+ t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0017b(self):

        spec01 = '<nt01>:(t02 [token01])+ t03;'
        spec_expected = '( t02 [ token01 ] )+ t03'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0017c(self):

        spec01 = '<nt01>:t02+ t03 [token01];'
        spec_expected = 't02+ t03 [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0017d(self):

        spec01 = '<nt01>:(t02[token01])+ t03 [token02];'
        spec_expected = '( t02 [ token01 ] )+ t03 [ token02 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0017e(self):

        spec01 = '<nt01>:[token05]((t02[token01])+ t03 [token02])[token04];'
        spec_expected = '[ token05 ] ( ( t02 [ token01 ] )+ t03 [ token02 ] ) [ token04 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0018(self):

        spec01 = '<nt01>:t02 t03+;'
        spec_expected = 't02 t03+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0018b(self):

        spec01 = '<nt01>:t02 [token01]t03+;'
        spec_expected = 't02 [ token01 ] t03+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    def test_0018c(self):

        spec01 = '<nt01>:t02 (t03 [token01])+;'
        spec_expected = 't02 ( t03 [ token01 ] )+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0018d(self):

        spec01 = '<nt01>:t02 [token01] (t03 [token02])+;'
        spec_expected = 't02 [ token01 ] ( t03 [ token02 ] )+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0018e(self):

        spec01 = '<nt01>:t02 [token01] ((t03 [token02])+)[token03];'
        spec_expected = 't02 [ token01 ] ( ( t03 [ token02 ] )+ ) [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0018f(self):

        spec01 = '<nt01>:[token05](t02 [token01] ((t03 [token02])+)[token03])[token04];'
        spec_expected = '[ token05 ] ( t02 [ token01 ] ( ( t03 [ token02 ] )+ ) [ token03 ] ) [ token04 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0019(self):

        spec01 = '<nt01>:(t02 t03)+;'
        spec_expected = '( t02 t03 )+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0019b(self):

        spec01 = '<nt01>:(t02 [token01] t03)+;'
        spec_expected = '( t02 [ token01 ] t03 )+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0019c(self):

        spec01 = '<nt01>:(t02 t03 [token01])+;'
        spec_expected = '( t02 t03 [ token01 ] )+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0019d(self):

        spec01 = '<nt01>:(t02 [token01] t03 [token02])+;'
        spec_expected = '( t02 [ token01 ] t03 [ token02 ] )+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    def test_0019e(self):

        spec01 = '<nt01>:[token04]( (t02 [token01] t03 [token02])+)[token03] ;'
        spec_expected = '[ token04 ] ( ( t02 [ token01 ] t03 [ token02 ] )+ ) [ token03 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )

        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL
    #
    def test_rules_0001(self):

        spec01 = '<nt01>:t02;'
        spec_expected = 't02'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL PLUS
    #
    def test_rules_0002(self):

        spec01 = '<nt01>:t02+;'
        spec_expected = 't02+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL STAR
    #
    def test_rules_0003(self):

        spec01 = '<nt01>:t02*;'
        spec_expected = 't02*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL QUESTION
    #
    def test_rules_0004(self):

        spec01 = '<nt01>:t02?;'
        spec_expected = 't02?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL finite_repeat
    def test_rules_0005(self):

        spec01 = '<nt01>:t02{3,7};'
        spec_expected = 't02{ 3, 7 }'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
        ast01.replace_finite_repeat_with_union()
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL out_token
    def test_rules_0006(self):

        spec01 = '<nt01>:t02 [token01];'
        spec_expected = 't02 [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> NONTERMINAL
    def test_rules_0007(self):

        spec01 = '<nt01>:<nt02>;'
        spec_expected = '<nt02>'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> NONTERMINAL PLUS
    def test_rules_0008(self):

        spec01 = '<nt01>:<nt02>+;'
        spec_expected = '<nt02>+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> NONTERMINAL STAR
    def test_rules_0009(self):

        spec01 = '<nt01>:<nt02>*;'
        spec_expected = '<nt02>*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> NONTERMINAL QUESTION
    def test_rules_0010(self):

        spec01 = '<nt01>:<nt02>?;'
        spec_expected = '<nt02>?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> NONTERMINAL finite_repeat
    def test_rules_0011(self):

        spec01 = '<nt01>:<nt02>{6,11};'
        spec_expected = '<nt02>{ 6, 11 }'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        ast01.replace_finite_repeat_with_union()
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> NONTERMINAL out_token
    def test_rules_0012(self):

        spec01 = '<nt01>:<nt02>[token01];'
        spec_expected = '<nt02> [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> PAREN_L expression PAREN_R
    #                                                                                        expression -> factors
    #                                                                                                      factors -> factor factors
    #                                                                                                                 factor -> TERMINAL
    #                                                                                                                        factors -> factor
    #                                                                                                                                   factor -> TERMINAL
    def test_rules_0013(self):

        spec01 = '<nt01>:( t01 t02 );'
        spec_expected = 't01 t02'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> PAREN_L expression PAREN_R PLUS
    #                                                                                        expression -> factors
    #                                                                                                      factors -> factor factors
    #                                                                                                                 factor -> TERMINAL
    #                                                                                                                        factors -> factor
    #                                                                                                                                   factor -> TERMINAL
    def test_rules_0014(self):

        spec01 = '<nt01>:( t01 t02 )+;'
        spec_expected = '( t01 t02 )+'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> PAREN_L expression PAREN_R STAR
    #                                                                                        expression -> factors
    #                                                                                                      factors -> factor factors
    #                                                                                                                 factor -> TERMINAL
    #                                                                                                                        factors -> factor
    #                                                                                                                                   factor -> TERMINAL
    def test_rules_0015(self):

        spec01 = '<nt01>:( t01 t02 )*;'
        spec_expected = '( t01 t02 )*'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> PAREN_L expression PAREN_R QUESTION
    #                                                                                        expression -> factors
    #                                                                                                      factors -> factor factors
    #                                                                                                                 factor -> TERMINAL
    #                                                                                                                        factors -> factor
    #                                                                                                                                   factor -> TERMINAL
    def test_rules_0016(self):

        spec01 = '<nt01>:( t01 t02 )?;'
        spec_expected = '( t01 t02 )?'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> PAREN_L expression PAREN_R finite_repeat
    #                                                                                        expression -> factors
    #                                                                                                      factors -> factor factors
    #                                                                                                                 factor -> TERMINAL
    #                                                                                                                        factors -> factor
    #                                                                                                                                   factor -> TERMINAL
    def test_rules_0017(self):

        spec01 = '<nt01>:( t01 t02 ){3,6};'
        spec_expected = '( t01 t02 ){ 3, 6 }'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
        ast01.replace_finite_repeat_with_union()
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> PAREN_L expression PAREN_R out_token
    #                                                                                        expression -> factors
    #                                                                                                      factors -> factor factors
    #                                                                                                                 factor -> TERMINAL
    #                                                                                                                        factors -> factor
    #                                                                                                                                   factor -> TERMINAL
    def test_rules_0018(self):

        spec01 = '<nt01>:( t01 t02 )[token01];'
        spec_expected = '( t01 t02 ) [ token01 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> out_token PAREN_L expression PAREN_R out_token
    #                                                                                                  expression -> factors
    #                                                                                                                factors -> factor factors
    #                                                                                                                           factor -> TERMINAL
    #                                                                                                                                  factors -> factor
    #                                                                                                                                             factor -> TERMINAL
    def test_rules_0019(self):

        spec01 = '<nt01>:[token01]( t01 t02 )[token02];'
        spec_expected = '[ token01 ] ( t01 t02 ) [ token02 ]'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        



    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor factors
    #                                                                      factor -> TERMINAL          
    #                                                                             factors -> factor
    #                                                                                        factor -> TERMINAL

    def test_rules_0020(self):

        spec01 = '<nt01>:t01 t02;'
        spec_expected = 't01 t02'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors PIPE expression
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL          
    #                                                                             factors -> factor
    #                                                                        expression -> factors
    #                                                                                      factors -> factor
    #                                                                                                 factor -> TERMINAL
    def test_rules_0021(self):

        spec01 = '<nt01>:t01 | t02;'
        spec_expected = '( t01 | t02 )'
        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('nfa', show_out_token = True, view_now = True, out_format = "pdf" )
        fst02 = DFA_from_NFA(fst01)
#        fst02.draw('dfa', show_out_token = True, view_now = True, out_format = "pdf" )        


    # start -> rules
    #          rules -> rule rules
    #                   rule -> NONTERMINAL COLON expression SEMICOLON
    #                                             expression -> factors
    #                                                           factors -> factor
    #                                                                      factor -> TERMINAL          
    #                        rules -> rule
    #                                 rule -> NONTERMINAL COLON expression SEMICOLON
    #                                                           expression -> factors
    #                                                                         factors -> factor
    #                                                                                    factor -> TERMINAL          
    def test_rules_0022(self):

        spec01 = '''
            <nt01>:t03;
            <nt03>:t04;
        '''
        spec_expected_01 = 't03'
        spec_expected_02 = 't04'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ASTs   = parser.parse_rules( spec01 )
        ast01 = ASTs['<nt01>']
        ast02 = ASTs['<nt03>']
        str01 = ast01.emit_formatted_text(80, 4, True)
        str02 = ast02.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected_01 )
        self.assertEqual( str02, spec_expected_02 )
#        ast01.draw('tmp1', True, 'pdf' )
#        ast02.draw('tmp2', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp1', show_out_token = True, view_now = True, out_format = "pdf" )

#        fst02 = ast02.generate_fst(True)
#        fst02.draw('tmp2', show_out_token = True, view_now = True, out_format = "pdf" )




    # start -> expression
    #          expression -> factors
    #                        factors -> factor
    #                                   factor -> TERMINAL          
    def test_lines_0001(self):

        spec01 = '''
            t01
        '''

        spec_expected = 't01'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )


    # start -> expression
    #          expression -> factors
    #                        factors -> factor
    #                                   factor -> TERMINAL          
    def test_lines_0002(self):

        spec01 = '''
            t01 t02
        '''

        spec_expected = 't01 t02'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )



    # start -> expression
    #          expression -> factors
    #                        factors -> factor
    #                                   factor -> TERMINAL          
    def test_lines_0003(self):

        spec01 = '''
            t01
            t02
            t03
        '''

        spec_expected = '( t01 | t02 | t03 )'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )


    # start -> expression
    #          expression -> factors
    #                        factors -> factor
    #                                   factor -> TERMINAL          
    def test_lines_0004(self):

        spec01 = '''
            t01 t02
            t03 t04
            t05 t06
        '''

        spec_expected = '( t01 t02 | t03 t04 | t05 t06 )'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )


    def test_lines_0005(self):

        spec01 = '''
            t01 [token01] t02[token02]
        '''

        spec_expected = 't01 [ token01 ] t02 [ token02 ]'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )


    def test_lines_0006(self):

        spec01 = '''
            [token03]( t01 [token01] t02[token02] ) [token04]
        '''

        spec_expected = '[ token03 ] ( t01 [ token01 ] t02 [ token02 ] ) [ token04 ]'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )


    def test_lines_0007(self):

        spec01 = '''
            [token03]( t01 [token01] | t02[token02] ) [token04]
        '''

        spec_expected = '[ token03 ] ( t01 [ token01 ] | t02 [ token02 ] ) [ token04 ]'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )


    def test_lines_0008(self):

        spec01 = '''
            [token03]( t01 [token01] | t02* ) [token04]
        '''

        spec_expected = '[ token03 ] ( t01 [ token01 ] | t02* ) [ token04 ]'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )



    def test_lines_0009(self):

        spec01 = '''
             ( t01 | t02 | <nt02> )+
        '''

        spec_expected = '( t01 | t02 | <nt02> )+'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
#        print (str01)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )

    def test_lines_0010(self):

        spec01 = '''
             ( t01  t02 <nt02> )+
        '''

        spec_expected = '( t01 t02 <nt02> )+'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
#        print (str01)
        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp', True, 'pdf' )
#        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp', show_out_token = True, view_now = True, out_format = "pdf" )


    def test_lines_0011(self):

        spec01 = '''
            ( T01 [ token03 token04 ] )
            ( N01 [ token03 token04 ] )
            ( [ token02 token01 ] ( T01 ) [ token03 token04 ] )
            ( T01 [ token03 token04 ] )
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] ) ) [ token03 token04 ] )
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] ) ( N02 [ token11 token12 ] ) ) [ token03 token04 ] )
            ( [ token02 token01 ] ( T01 [ token07 token08 ] ) [ token03 token04 ] )
            ( [ token02 token01 ] ( T02 [ token11 token12 ] ) [ token03 token04 ] )
            ( __EPS__ [ token03 token04 ] )
            ( [ token02 token01 ] ( T01 [ token07 token08 ] ) [ token03 token04 ] )
            ( [ token02 token01 ] ( T01{ 0, 3 } ) [ token03 token04 ] )
            ( [ token02 token01 ] ( T01{ 2, 7 } ) [ token03 token04 ] )
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] ){ 0, 3 } ) [ token03 token04 ] )
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] ){ 2, 7 } ) [ token03 token04 ] )
            ( [ token02 token01 ] ( T01* ) [ token03 token04 ] )
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] )* ) [ token03 token04 ] )
            ( [ token02 token01 ] ( T01+ ) [ token03 token04 ] )
            ( [ token02 token01 ] ( ( T01 [ token07 token08 ] )+ ) [ token03 token04 ] )
        '''

        spec_expected = '( t01 t02 <nt02> )+'

        parser = nlpregex.regular_language.lark_parser.LarkParser()
        ast01   = parser.parse_lines( spec01 )
        str01 = ast01.emit_formatted_text(80, 4, True)
#        self.assertEqual( str01, spec_expected )
#        ast01.draw('tmp_ast', True, 'pdf' )
        fst01 = ast01.generate_fst(True)
#        fst01.draw('tmp_fst', show_out_token = True, view_now = True, out_format = "pdf" )
        fst01 = ast01.generate_fst(True)
        dfa01 = DFA_from_NFA(fst01)
#        dfa01.draw('tmp_fst', show_out_token = True, view_now = True, out_format = "pdf" )


if __name__ == '__main__':
    unittest.main()
