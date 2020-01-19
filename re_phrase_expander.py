#!/usr/bin/env python                                                                                                                                  
# -*- coding: utf-8 -*-                                                                                                                                

""" Regular Expression Phrase Expander."""
import argparse
import sys

import nlpregex.regular_language.lark_parser
import nlpregex.regular_language.ast

def parse_commandline():

    arg_parser = argparse.ArgumentParser( description
        = 'expand phrases of regular expression' )

    arg_parser.add_argument( 'infile',                nargs = '?', type = argparse.FileType('r'), default = sys.stdin,  
        help = 'input file'  )

    arg_parser.add_argument( 'outfile',               nargs = '?', type = argparse.FileType('w'), default = sys.stdout, 
        help = 'output file' )

    arg_parser.add_argument( '-rule',                 nargs = 1, metavar = '<nonterminal>',  
        help = 'rule to expand' )

    arg_parser.add_argument( '-expand',               nargs = '*', metavar = '<list of nonterminals>',  
        help = 'tries to expand the given nontermals (default NONE)' )

    arg_parser.add_argument( '-expand_finite_repeat', action = "store_true",
        help = 'expands finite repeats, otherwise, it will be replaced with a temporary token' )

    return arg_parser


def main():

    comm_parser = parse_commandline()
    comm_args   = comm_parser.parse_args()

    input_content = comm_args.infile.read()

#    print (comm_args)

    lp   = nlpregex.regular_language.lark_parser.LarkParser()
    ASTs = lp.parse_rules( input_content )

    if comm_args.rule[0] not in ASTs:

        comm_parser.print_help( sys.stdout )
        sys.exit(1)

    ast = ASTs[ comm_args.rule[0] ]

    ast.clean_epsilon()

    if comm_args.expand:
        ast.expand_nonterminals( comm_args.expand, ASTs )

    if comm_args.expand_finite_repeat:
        ast.replace_finite_repeat_with_union()

    output_content = ast.expand_phrases()

    for phrase in output_content:

        comm_args.outfile.write( phrase + '\n' )


if __name__ == "__main__":
    main()
