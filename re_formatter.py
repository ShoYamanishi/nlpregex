#!/usr/bin/env python                                                                                                                                  
# -*- coding: utf-8 -*-                                                                                                                                

""" Regular Expression Formatter."""
import argparse
import sys

import nlpregex.regular_language.lark_parser
import nlpregex.regular_language.ast

def parse_commandline():

    arg_parser = argparse.ArgumentParser( description
        = 'reformat regular expression with the specified nonterminals replaced with sub-expressions' )

    arg_parser.add_argument( 'infile',                nargs = '?', type = argparse.FileType('r'), default = sys.stdin,  
        help = 'input file'  )

    arg_parser.add_argument( 'outfile',               nargs = '?', type = argparse.FileType('w'), default = sys.stdout, 
        help = 'output file' )

    arg_parser.add_argument( '-rules',                nargs = '*', metavar = '<list of nonterminals>',  
        help = 'rules to reformat (default ALL)' )

    arg_parser.add_argument( '-expand',               nargs = '*', metavar = '<list of nonterminals>',  
        help = 'tries to expand the given nontermals (default NONE)' )

    arg_parser.add_argument( '-expand_all_nt',        action = "store_true",  
        help = 'tries to expand all the nonterminals for the specified rule' )

    arg_parser.add_argument( '-expand_finite_repeat', action = "store_true",
        help = 'expands finite repeats' )

    arg_parser.add_argument( '-width_hint',           nargs = '?', type = int, default = 60,
        help = 'max width at which this tool tries to fold the selection expression into multiple lines' )

    arg_parser.add_argument( '-indent',               nargs = '?', type = int, default = 4,
        help = 'number of spaces for a single indentation' )

    return arg_parser


def main():

    comm_parser = parse_commandline()
    comm_args   = comm_parser.parse_args()

    input_content = comm_args.infile.read()

#    print (comm_args)

    lp   = nlpregex.regular_language.lark_parser.LarkParser()
    ASTs = lp.parse_rules( input_content )

    if comm_args.rules:
        rules_to_display = comm_args.rules

    else:
        rules_to_display = list( ASTs.keys() )

    for rule in rules_to_display:

        ast = ASTs[rule]

        if comm_args.expand_all_nt:
            all_nt = list(ASTs.keys())

            ast.expand_nonterminals( list( all_nt ), ASTs )

        elif comm_args.expand:
            ast.expand_nonterminals( comm_args.expand, ASTs )

        ast.clean_epsilon()

        if comm_args.expand_finite_repeat:
            ast.replace_finite_repeat_with_union()

        output_rhs = ast.emit_formatted_text( comm_args.width_hint, comm_args.indent )

        comm_args.outfile.write( rule + ' : ' + output_rhs + ' ;\n' )


if __name__ == "__main__":
    main()
