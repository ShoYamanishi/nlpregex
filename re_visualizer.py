#!/usr/bin/env python                                                                                                                                  
# -*- coding: utf-8 -*-                                                                                                                                

""" Regular Expression Visualizer."""
import argparse
import sys

import nlpregex.regular_language.lark_parser
import nlpregex.regular_language.ast
import nlpregex.regular_language.fa

def parse_commandline():

    arg_parser = argparse.ArgumentParser( description
        = 'visualize regular expression in AST, NFA, and DFA' )

    arg_parser.add_argument( 'infile',                nargs = '?',     type = argparse.FileType('r'), default = sys.stdin,  
        help = 'input file'  )

    arg_parser.add_argument( 'outfile',               nargs = '?',     type = argparse.FileType('w'), default = sys.stdout, 
        help = 'output file' )

    arg_parser.add_argument( '-rule',                 nargs = 1,       metavar = '<nonterminal>',  
        help = 'rule to expand' )

    arg_parser.add_argument( '-expand',               nargs = '*',     metavar = '<list of nonterminals>',  
        help = 'tries to expand the given nontermals (default NONE)' )

    arg_parser.add_argument( '-ast',                  nargs = 1,       metavar = '<file name w/o ext>',
        help = 'draws abstract syntax tree to the file' )

    arg_parser.add_argument( '-nfa',                  nargs = 1,       metavar = '<file name w/o ext>',
        help = 'draws NFA to the file.' )

    arg_parser.add_argument( '-dfa',                  nargs = 1,       metavar = '<file name w/o ext>',
        help = 'draws DFA to the file.' )

    arg_parser.add_argument( '-t',                    nargs = '?',     default = "pdf", const = "pdf", metavar = 'pdf/svg', choices = [ 'pdf', 'svg' ],
        help = 'visual output file type. svg or pdf. default: pdf. Use svg if you have a unicode issue on Windows.' )

    arg_parser.add_argument( '-s',                    action="store_true", 
        help = 'tries to show the visual immediately' )

    arg_parser.add_argument( '-horizontal',           action="store_true", 
        help = 'draw AST horizontally' )


    return arg_parser


def main():

    comm_parser = parse_commandline()
    comm_args   = comm_parser.parse_args()

    input_content = comm_args.infile.read()

    
    print (comm_args)

    lp   = nlpregex.regular_language.lark_parser.LarkParser()
    ASTs = lp.parse_rules( input_content )

    if comm_args.rule[0] not in ASTs:

        comm_parser.print_help( sys.stdout )
        sys.exit(1)

    ast = ASTs[ comm_args.rule[0] ]

    ast.clean_epsilon()

    if comm_args.expand:
        ast.expand_nonterminals( comm_args.expand, ASTs )

    if comm_args.ast:
        if comm_args.horizontal:
            orientation = 'horizontal'
        else:
            orientation = 'vertical'
        ast.draw( comm_args.ast[0], comm_args.s, comm_args.t, orientation )


    if comm_args.nfa or comm_args.dfa:
        nfa = ast.generate_fst( generate_out_tokens = True )

        if comm_args.nfa:
            nfa.draw( comm_args.nfa[0], True, comm_args.s, comm_args.t )

        if comm_args.dfa:
            dfa = nlpregex.regular_language.fa.DFA_from_NFA( nfa )
            dfa.draw( comm_args.dfa[0], True, comm_args.s, comm_args.t )


if __name__ == "__main__":
    main()
