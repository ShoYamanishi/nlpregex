#!/usr/bin/env python                                                                                                                                  
# -*- coding: utf-8 -*-                                                                                                                                

""" Regular Expression Decoder."""
import argparse
import sys

import nlpregex.regular_language.lark_parser
import nlpregex.regular_language.ast
import nlpregex.regular_language.fa

def parse_commandline():

    arg_parser = argparse.ArgumentParser( description
        = 'decode regular language with output attributes' )

    arg_parser.add_argument( 'infile',                nargs = '?',     type = argparse.FileType('r'), default = sys.stdin,  
        help = 'input file'  )

    arg_parser.add_argument( 'outfile',               nargs = '?',     type = argparse.FileType('w'), default = sys.stdout, 
        help = 'output file' )

    arg_parser.add_argument( '-rulefile',             nargs = 1,       type = argparse.FileType('r'), default = None,
        help = 'regular expression rule file' )

    arg_parser.add_argument( '-rule',                 nargs = 1,       metavar = '<nonterminal>',  
        help = 'rule to expand' )

    arg_parser.add_argument( '-expand',               nargs = '*',     metavar = '<list of nonterminals>',  
        help = 'tries to expand the given nontermals (default NONE)' )

    arg_parser.add_argument( '-expand_all_nt',        action = "store_true",  
        help = 'tries to expand all the nonterminals for the specified rule' )

    return arg_parser


def main():

    comm_parser = parse_commandline()
    comm_args   = comm_parser.parse_args()

#    print (comm_args)

    if not comm_args.rulefile:
        comm_parser.print_help( sys.stdout )
        sys.exit(1)

    rules_content = comm_args.rulefile[0].read()
    
    lp   = nlpregex.regular_language.lark_parser.LarkParser()
    ASTs = lp.parse_rules( rules_content )


    if ( not comm_args.rule ) or ( comm_args.rule[0] not in ASTs ):

        comm_parser.print_help( sys.stdout )
        sys.exit(1)

    ast = ASTs[ comm_args.rule[0] ]

    ast.clean_epsilon()

    if comm_args.expand_all_nt:
        all_nt = list(ASTs.keys())
        all_nt.remove( comm_args.rule[0] )

        ast.expand_nonterminals( list( all_nt ), ASTs )

    elif comm_args.expand:
        ast.expand_nonterminals( comm_args.expand, ASTs )

    nfa = ast.generate_fst( generate_out_tokens = True )
    dfa = nlpregex.regular_language.fa.DFA_from_NFA( nfa )

    for line in comm_args.infile:    

        in_tokens = line.strip().split(' ')
        out_tokens = nlpregex.regular_language.fa.decode(dfa, in_tokens)
        if out_tokens:
            if len(out_tokens) == 0:
                out_tokens.append('__ACCEPTED__')
        else:
            out_tokens = [ '__NOT_ACCEPTED__' ]

        comm_args.outfile.write( ' '.join(out_tokens) + '\n' )

        
if __name__ == "__main__":
    main()
