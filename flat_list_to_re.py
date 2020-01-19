#!/usr/bin/env python                                                                                                                                  
# -*- coding: utf-8 -*-                                                                                                                                

""" Regular Expression Generator From A Flat List."""
import argparse
import sys

import nlpregex.regular_language.lark_parser
import nlpregex.regular_language.ast
import nlpregex.regular_language.fa
import nlpregex.regular_language.fa_to_ast

def parse_commandline():

    arg_parser = argparse.ArgumentParser( description
        = 'generate regular expression from a flat list' )

    arg_parser.add_argument( 'infile',                nargs = '?',     type = argparse.FileType('r'), default = sys.stdin,  
        help = 'input file'  )

    arg_parser.add_argument( 'outfile',               nargs = '?',     type = argparse.FileType('w'), default = sys.stdout, 
        help = 'output file' )

    arg_parser.add_argument( '-reduce',               action="store_true", 
        help = 'tries to reduce the common subexpressions' )

    arg_parser.add_argument( '-min_num_occurrences',  nargs = '?',     type = int, default = 2,
        help = 'min number of occurrences of a common subexpression to be considered for reduction' )

    arg_parser.add_argument( '-min_num_terms',        nargs = '?',     type = int, default = 2,
        help = 'min number of terminals in a common subexpression to be considered for reduction' )

    arg_parser.add_argument( '-width_hint',           nargs = '?',     type = int, default = 60,
        help = 'max width at which this tool tries to fold the selection expression into multiple lines' )

    arg_parser.add_argument( '-indent',               nargs = '?',     type = int, default = 4,
        help = 'number of spaces for a single indentation' )

    return arg_parser


def main():

    comm_parser = parse_commandline()
    comm_args   = comm_parser.parse_args()

#    print (comm_args)

    lines_content = comm_args.infile.read()
    
    lp  = nlpregex.regular_language.lark_parser.LarkParser()
    ast = lp.parse_lines( lines_content )

    nfa = ast.generate_fst( generate_out_tokens = True )
    dfa = nlpregex.regular_language.fa.DFA_from_NFA( nfa )

    converter = nlpregex.regular_language.fa_to_ast.FAtoAST( dfa, comm_args.min_num_occurrences, comm_args.min_num_terms )

    converter.convert( reduceCommonSubtree = comm_args.reduce, reduceCommonUnionSubexpression = comm_args.reduce, reduceCommonSubstring = comm_args.reduce )
    for nt in converter.ASTs:

        ast = converter.ASTs[nt]
        ast.clean_epsilon()
        output_rhs = ast.emit_formatted_text( comm_args.width_hint, comm_args.indent )
        comm_args.outfile.write ( nt + ' : ' + output_rhs + ';\n' )

        
if __name__ == "__main__":
    main()
