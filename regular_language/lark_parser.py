#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# export PYTHONPATH=~/workarea

from lark import Lark

import re

# Use fully qualified name to avoid conflict with names in Lark parser,
# which uses the same names such as ast.
import nlpregex.regular_language.ast

# Grammar spec for Lark to parse NLPRegEx
# ---------------------------------------
#
# 1. Comments with /* */, //..., and #... 
#    are removed before parsing to avoid extra complications
#    in Lark's tokenizer  definitons.
#
# 2. Escapted char in the quoted string are not handled
#    to avoid extra complications in Lark's tokenizer 
#    definitons. Especially escapted double quote seems
#    impossible to handle.
#
# 3. Terminals are usual string with some symbols but without white spaces.
#    See TERMINAL in grammar_nlpregex_rules for definition.
#    Ex. abc a_d 1xy-234
#
# 4. Nonterminals are enclosed by angle brackets.
#    Ex. <nt1>
#
# 5. Following post-unary operators are defined.
#     * - zero or multiple repetitions (Kleene closure)
#     + - one or multiple repetitions  (positive closure)
#     ? - option
#    Ex. a* b+ ( c | d )?
#
# 6. Following binary operations are defined
#     <juxtaposition> - sequence
#     |               - union (selection)
#    Ex. a b c d e
#        a | b | c | d | e
#
# 7. Output tokens, which can be used to generate output by 
#    FST (finite state transducer), can be attached to after a terminal,
#    and before and after an expression.
#    Ex.  a [output_a]
#         a b c [output_before] ( d | e | f ) [output_after] g h
#
# 8. File organization
# 8.1. Rules mode
#     Rules mode defines a set of rules for a regular language as follows.
#     Ex.
#         <top> : a <nt1> <nt2> ( [out_token_1]( b ( d c* a ) | efg ) [out_token_2] );
#         <nt1> : abcd
#         <nt2> : efgh
#
# 8.2. Line mode
#     Line mode defines a language that consists of lines, in the sense that
#     each line represents a phrase, and those lines are joined with a single
#     union (selection) operator.
#     This way, the file in Line mode represents the entire set of phrases
#     accepted by the language.
#
# Usage
# -----
# 1. Import
# from nlpregex.regular_language.lark_parser import LarkParser
# 
# 2. Instantiate
# parser = LarkParser()
#
# 3. Parse 
# 3.1. Rules Mode
# asts = parser.parse_rules( input_string ) - parse file in Rule mode into ASTs
# # asts is a dictionary whose keys are the nonterminals on the LHS of the file, and values are
# # the corresponding ASTs in nlpregex.regular_language.AST.
#
# 3.2. Line Mode
# ast = parser.parse_lines( input_string ) - parse file in Line mode into an AST.
# # ast is the parsed AST in nlpregex.regular_language.AST, where the top
#   node is of type 'union' and its children represent the lines.
#

grammar_nlpregex_rules = """
    start                    : rules

    rules                    : rule | rule rules

    rule                     : NONTERMINAL COLON expression SEMICOLON

    expression               : factors | factors PIPE expression

    factors                  : factor | factor factors

    factor                   : TERMINAL |\
                               TERMINAL PLUS |\
                               TERMINAL STAR |\
                               TERMINAL QUESTION |\
                               TERMINAL finite_repeat |\
                               TERMINAL out_token |\
                               NONTERMINAL | \
                               NONTERMINAL PLUS | \
                               NONTERMINAL STAR | \
                               NONTERMINAL QUESTION |\
                               NONTERMINAL finite_repeat |\
                               NONTERMINAL out_token |\
                               PAREN_L expression PAREN_R |\
                               PAREN_L expression PAREN_R PLUS |\
                               PAREN_L expression PAREN_R STAR |\
                               PAREN_L expression PAREN_R QUESTION |\
                               PAREN_L expression PAREN_R finite_repeat |\
                               PAREN_L expression PAREN_R out_token |\
                               out_token PAREN_L expression PAREN_R out_token

    finite_repeat            : CUR_BRACKET_L DECIMAL_NUMBER COMMA DECIMAL_NUMBER CUR_BRACKET_R

    out_token                : SQ_BRACKET_L OUT_CONTENT SQ_BRACKET_R

    DECIMAL_NUMBER           : /[0-9]+/

    TERMINAL                 : /[a-zA-Z0-9\u00A0-\uFFFF$'&._\-]*[a-zA-Z\u00A0-\uFFFF'&._\-][a-zA-Z0-9\u00A0-\uFFFF'&._\-]*/

    NONTERMINAL              : /<[\\\[\]\^\- !#$%&"'()*+,.:;=?@_`{|}a-zA-Z0-9\u00A0-\u00FF]*>/

    QUOTED_STRING            : /"[\\\[\]\^\- !#$%&'()*+,.:;<=>?@_`{|}a-zA-Z0-9\u00A0-\uFFFF]*"/

    OUT_CONTENT              : /[\\\^\- !#$%&"'()*+,.:;=?@_`{|}a-zA-Z0-9\u00A0-\u00FF]+/

    PIPE                     : "|"
    QUESTION                 : "?"
    COLON                    : ":"
    SEMICOLON                : ";"
    COMMA                    : ","
    PLUS                     : "+"
    STAR                     : "*"
    PAREN_L                  : "("
    PAREN_R                  : ")"
    SQ_BRACKET_L             : "["
    SQ_BRACKET_R             : "]"
    CUR_BRACKET_L            : "{"
    CUR_BRACKET_R            : "}"
   

    WHITE_SPACE              : /[ \\t\\r\\n\\v]+/

    %ignore WHITE_SPACE
"""


grammar_nlpregex_expanded_line = """
    start                    : expression

    expression               : factors | factors PIPE expression

    factors                  : factor | factor factors

    factor                   : TERMINAL |\
                               TERMINAL PLUS |\
                               TERMINAL STAR |\
                               TERMINAL QUESTION |\
                               TERMINAL finite_repeat |\
                               TERMINAL out_token |\
                               NONTERMINAL | \
                               NONTERMINAL PLUS | \
                               NONTERMINAL STAR | \
                               NONTERMINAL QUESTION |\
                               NONTERMINAL finite_repeat |\
                               NONTERMINAL out_token |\
                               PAREN_L expression PAREN_R |\
                               PAREN_L expression PAREN_R PLUS |\
                               PAREN_L expression PAREN_R STAR |\
                               PAREN_L expression PAREN_R QUESTION |\
                               PAREN_L expression PAREN_R finite_repeat |\
                               PAREN_L expression PAREN_R out_token |\
                               out_token PAREN_L expression PAREN_R out_token

    finite_repeat            : CUR_BRACKET_L DECIMAL_NUMBER COMMA DECIMAL_NUMBER CUR_BRACKET_R

    out_token                : SQ_BRACKET_L OUT_CONTENT SQ_BRACKET_R

    DECIMAL_NUMBER           : /[0-9]+/

    TERMINAL                 : /[a-zA-Z0-9\u00A0-\uFFFF$'&._\-]*[a-zA-Z\u00A0-\uFFFF'&._\-][a-zA-Z0-9\u00A0-\uFFFF'&._\-]*/

    NONTERMINAL              : /<[\\\[\]\^\- !#$%&"'()*+,.:;=?@_`{|}a-zA-Z0-9\u00A0-\u00FF]*>/

    QUOTED_STRING            : /"[\\\[\]\^\- !#$%&'()*+,.:;<=>?@_`{|}a-zA-Z0-9\u00A0-\uFFFF]*"/

    OUT_CONTENT              : /[\\\^\- !#$%&"'()*+,.:;=?@_`{|}a-zA-Z0-9\u00A0-\u00FF]+/

    PIPE                     : "|"
    QUESTION                 : "?"
    COLON                    : ":"
    SEMICOLON                : ";"
    COMMA                    : ","
    PLUS                     : "+"
    STAR                     : "*"
    PAREN_L                  : "("
    PAREN_R                  : ")"
    SQ_BRACKET_L             : "["
    SQ_BRACKET_R             : "]"
    CUR_BRACKET_L            : "{"
    CUR_BRACKET_R            : "}"
   

    WHITE_SPACE              : /[ \\t\\r\\n\\v]+/

    %ignore WHITE_SPACE
"""


# Helper class to retrieve data from Lark's parsed tree.
class LarkUtil():

    def get_children( self, lark_node ):

        if hasattr( lark_node, 'children' ):
            return lark_node.children

        else:
            return []


    def get_type( self, lark_node ):

        if hasattr( lark_node, 'type' ):
            return lark_node.type

        else:
            return ""


    def get_data( self, lark_node ):

        if hasattr( lark_node, 'data' ):
            return lark_node.data

        else:
            return ""


    # Removes /**/, //... and #...
    # Comments can be best handled separately from the parser.
    def remove_python_and_cpp_style_comments( self, s ):

        def replacer(match):
            s = match.group(0)
            if s.startswith('/'):
                return " "
            elif s.startswith('#'):
                return ""
            else:
                return s

        pattern = re.compile(
            r'^#.*?$|//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        return re.sub(pattern, replacer, s)


class LarkParser():


    def __init__(self):

        self.util         = LarkUtil()
        self.ASTs         = {}


    # @public
    #
    # @brief parse a file content that consists of rules.
    #
    # @param input_string stirng that containt the rules prorably in multiple lines
    #
    # @return dictionary of ASTs indexed by the nonterminals on LHS.
    def parse_rules( self, input_string ): 
         
        stripped_string    = self.util.remove_python_and_cpp_style_comments( input_string )

        if stripped_string == '':
            return self.ASTs

        parser             = Lark( grammar_nlpregex_rules, parser='lalr' )

        lark_tree_top_node = parser.parse( stripped_string )        

        self.process_rule_start_rules( lark_tree_top_node )

        return self.ASTs


    # @public
    #
    # @brief parse a file content that consists of lines of phrases
    #
    # @param input_string stirng that containt the rules prorably in multiple lines
    #
    # @return an AST
    def parse_lines( self, input_string ): 
         

        stripped_string = self.util.remove_python_and_cpp_style_comments( input_string )
        lines = stripped_string.split('\n')

        parser = Lark( grammar_nlpregex_expanded_line, parser='lalr' )

        nlp_ast = nlpregex.regular_language.ast.AST()        

        first = True
        for line in lines:
            line = line.strip()
            if line == '':
                continue

            lark_tree_top_node = parser.parse( line )

            line_root = self.process_rule_start_expression( lark_tree_top_node, nlp_ast )

            if first:
                root = line_root
                nlp_ast.add_root(line_root)
                first = False
            else:
                new_root = nlpregex.regular_language.ast.create_union_subtree(nlp_ast.root, line_root, nlp_ast )
                nlp_ast.add_root(new_root)

        nlp_ast.flatten_children()

        return nlp_ast


    #
    # @section syntactic nodes processing
    #


    # start                    : rules
    def process_rule_start_rules( self, lark_node ):

        lark_children = self.util.get_children( lark_node )
        self.process_rule_rules( lark_children[0] )


    # rules                    : rule | rule rules
    def process_rule_rules( self, lark_node ):

        lark_children = self.util.get_children( lark_node )

        if len( lark_children ) == 1:
            self.process_rule_rule( lark_children[0] )

        elif len( lark_children ) == 2:
            self.process_rule_rule ( lark_children[0] )
            self.process_rule_rules( lark_children[1] )


    # rule                     : NONTERMINAL COLON expression SEMICOLON
    def process_rule_rule( self, lark_node ):

        lark_children  = self.util.get_children( lark_node )

        nt = self.process_lex_NONTERMINAL( lark_children[0] )

        nlp_ast = nlpregex.regular_language.ast.AST()

        nlp_root = self.process_rule_expression( lark_children[2], nlp_ast )

        nlp_ast.add_root(nlp_root)
        nlp_ast.flatten_children()

        self.ASTs[ nt ] = nlp_ast


    # start                    : expression
    def process_rule_start_expression( self, lark_node, nlp_ast ):

        lark_children = self.util.get_children( lark_node )

        nlp_node = self.process_rule_expression(lark_children[0], nlp_ast )
        return nlp_node


    # expression               : factors | factors PIPE expression
    def process_rule_expression( self, lark_node , nlp_ast):

        lark_children = self.util.get_children( lark_node )

        if len(lark_children) == 1:
            return self.process_rule_factors( lark_children[0], nlp_ast )

        elif len(lark_children) == 3:
            left_child  = self.process_rule_factors( lark_children[0], nlp_ast )
            right_child = self.process_rule_expression( lark_children[2], nlp_ast )
            return nlpregex.regular_language.ast.create_union_subtree( left_child, right_child, nlp_ast )

        else:
            return None


    # factors                  : factor | factor factors
    def process_rule_factors( self, lark_node, nlp_ast ):

        lark_children = self.util.get_children( lark_node )

        if len(lark_children) == 1:
            return self.process_rule_factor( C[0], nlp_ast )

        if len(lark_children) == 2:
            left_child  = self.process_rule_factor ( lark_children[0], nlp_ast )
            right_child = self.process_rule_factors( lark_children[1], nlp_ast )

        return self.create_sequence_subtree( left_child, right_child, nlp_ast )


    # factors                  : factor | factor factors
    def process_rule_factors( self, lark_node, nlp_ast ):

        lark_children = self.util.get_children( lark_node )

        if len(lark_children) == 1:
            return self.process_rule_factor( lark_children[0], nlp_ast )

        if len(lark_children) == 2:
            left_child  = self.process_rule_factor ( lark_children[0], nlp_ast )
            right_child = self.process_rule_factors( lark_children[1], nlp_ast )

        return nlpregex.regular_language.ast.create_sequence_subtree( left_child, right_child, nlp_ast )


    # factor                   : TERMINAL |\
    #                            NONTERMINAL | \
    #                            PAREN_L expression PAREN_R
    def process_rule_factor( self, lark_node, nlp_ast ):
    
        lark_children = self.util.get_children( lark_node )
        LC0type = self.util.get_type( lark_children[0] )
        LC0data = self.util.get_data( lark_children[0] )

        if LC0type == 'TERMINAL':
            return self.process_rule_factor_case_TERMINAL( lark_children, nlp_ast )

        elif LC0type == 'NONTERMINAL':
            return self.process_rule_factor_case_NONTERMINAL( lark_children, nlp_ast )

        elif LC0type == 'PAREN_L':
            return self.process_rule_factor_case_PARENs( lark_children, nlp_ast )

        elif LC0data == 'out_token':
            return self.process_rule_factor_case_out_token( lark_children, nlp_ast )

        else:
            return None


    #                           TERMINAL | \
    #                           TERMINAL PLUS | \
    #                           TERMINAL STAR | \
    #                           TERMINAL QUESTION |\
    #                           TERMINAL finite_repeat |\
    #                           TERMINAL out_token |\
    def process_rule_factor_case_TERMINAL( self, lark_children, nlp_ast ):
        content = self.process_lex_TERMINAL( lark_children[0] )
        new_node = nlpregex.regular_language.ast.ASTNode( 'terminal', content )
        new_node.add_to_graph( nlp_ast )

        if len(lark_children) == 2:
            LC1type = self.util.get_type( lark_children[1] )
            LC1data = self.util.get_data( lark_children[1] )
        
            if LC1type == 'PLUS':
                return nlpregex.regular_language.ast.create_infinite_repeat_subtree( new_node, 'PLUS', nlp_ast )

            elif LC1type == 'STAR':
                return nlpregex.regular_language.ast.create_infinite_repeat_subtree( new_node, 'STAR', nlp_ast )

            elif LC1type == 'QUESTION':
                return nlpregex.regular_language.ast.create_finite_repeat_subtree( new_node, 0, 1, nlp_ast )

            elif LC1data == 'finite_repeat':
                value_min, value_max = self.process_rule_finite_repeat( lark_children[1] )
                return nlpregex.regular_language.ast.create_finite_repeat_subtree( new_node, value_min, value_max, nlp_ast )

            elif LC1data == 'out_token':
                post_token = self.process_rule_out_token( lark_children[1] )
                if post_token != '':
                    new_node.append_out_token_post( post_token )
                return new_node

            else:
                return None

        else:
            return new_node


    #                           NONTERMINAL | \
    #                           NONTERMINAL PLUS | \
    #                           NONTERMINAL STAR | \
    #                           NONTERMINAL QUESTION |\
    #                           NONTERMINAL finite_repeat |\
    #                           NONTERMINAL out_token |\
    def process_rule_factor_case_NONTERMINAL( self, lark_children, nlp_ast ):

        content = self.process_lex_NONTERMINAL( lark_children[0] )
        new_node = nlpregex.regular_language.ast.ASTNode( 'nonterminal', content )
        new_node.add_to_graph( nlp_ast )

        if len(lark_children) == 2:
            LC1type = self.util.get_type( lark_children[1] )
            LC1data = self.util.get_data( lark_children[1] )
        
            if LC1type == 'PLUS':
                return nlpregex.regular_language.ast.create_infinite_repeat_subtree( new_node, 'PLUS', nlp_ast )

            elif LC1type == 'STAR':
                return nlpregex.regular_language.ast.create_infinite_repeat_subtree( new_node, 'STAR', nlp_ast )

            elif LC1type == 'QUESTION':
                return nlpregex.regular_language.ast.create_finite_repeat_subtree( new_node, 0, 1, nlp_ast )

            elif LC1data == 'finite_repeat':
                value_min, value_max = self.process_rule_finite_repeat( lark_children[1] )
                return nlpregex.regular_language.ast.create_finite_repeat_subtree( new_node, value_min, value_max, nlp_ast )

            elif LC1data == 'out_token':

                post_token = self.process_rule_out_token( lark_children[1] )
                if post_token != '':
                    new_node.append_out_token_post( post_token )
                return new_node

            else:
                return None

        else:
            return new_node


    #                           PAREN_L expression PAREN_R |\
    #                           PAREN_L expression PAREN_R PLUS |\
    #                           PAREN_L expression PAREN_R STAR |\
    #                           PAREN_L expression PAREN_R QUESTION |\
    #                           PAREN_L expression PAREN_R finite_repeat |\
    #                           PAREN_L expression PAREN_R out_token |\
    def process_rule_factor_case_PARENs( self, lark_children, nlp_ast ):
     
        LC0type = self.util.get_type( lark_children[0] )
        LC0data = self.util.get_data( lark_children[0] )
        
        if LC0type == 'PAREN_L':

            exp_node = self.process_rule_expression( lark_children[1], nlp_ast )

            if len(lark_children) == 4:

                LC3type = self.util.get_type( lark_children[3] )
                LC3data = self.util.get_data( lark_children[3] )

                if LC3type == 'PLUS':
                    return nlpregex.regular_language.ast.create_infinite_repeat_subtree( exp_node, 'PLUS', nlp_ast )

                elif LC3type == 'STAR':
                    return nlpregex.regular_language.ast.create_infinite_repeat_subtree( exp_node, 'STAR', nlp_ast )

                elif LC3type == 'QUESTION':
                    return nlpregex.regular_language.ast.create_finite_repeat_subtree( exp_node, 0, 1, nlp_ast )

                elif LC3data == 'finite_repeat':

                    value_min, value_max = self.process_rule_finite_repeat( lark_children[3] )
                    return  nlpregex.regular_language.ast.create_finite_repeat_subtree( exp_node, value_min, value_max, nlp_ast )

                elif LC3data == 'out_token':
                    post_token = self.process_rule_out_token( lark_children[3] )
                    if post_token != '':
                        exp_node.append_out_token_post( post_token )

                    return exp_node

                else:
                    return exp_node

            else:
                return exp_node


    #                           out_token PAREN_L expression PAREN_R out_token
    def process_rule_factor_case_out_token( self, lark_children, nlp_ast ):

        LC0data = self.util.get_data( lark_children[0] )
        if LC0data == 'out_token':

            exp_node   = self.process_rule_expression( lark_children[2], nlp_ast )
            pre_token  = self.process_rule_out_token( lark_children[0] )
            post_token = self.process_rule_out_token( lark_children[4] )

            if pre_token != '':
                exp_node.append_out_token_pre( pre_token )

            if post_token != '':
                exp_node.append_out_token_post( post_token )

            return exp_node

        else:
            return None


    # finite_repeat            : CUR_BRACKET_L DECIMAL_NUMBER COMMA DECIMAL_NUMBER CUR_BRACKET_R
    def process_rule_finite_repeat( self, lark_node ):

        C = self.util.get_children( lark_node )

        C1type = self.util.get_type( C[1] )
        C3type = self.util.get_type( C[3] )

        if C1type == 'DECIMAL_NUMBER' and C3type == 'DECIMAL_NUMBER':

            C1str = self.process_lex_DECIMAL_NUMBER( C[1] )
            C3str = self.process_lex_DECIMAL_NUMBER( C[3] )

            return ( int(C1str), int(C3str) )

        else:
            return (0,0)


    # out_token                : SQ_BRACKET_L OUT_CONTENT SQ_BRACKET_R
    def process_rule_out_token( self, lark_node ):
        C = self.util.get_children( lark_node )

        C1type = self.util.get_type( C[1] )

        if C1type == 'OUT_CONTENT':
            return self.process_lex_OUT_CONTENT( C[1] )

        else:
            return ""


    #
    # @section lexical nodes processing
    #


    # DECIMAL_NUMBER           : /[0-9]+/
    def process_lex_DECIMAL_NUMBER( self, lark_node ):
        if self.util.get_type( lark_node ) == 'DECIMAL_NUMBER':
            return lark_node.value
        else:
           return ""


    # TERMINAL                 : /[a-zA-Z0-9\u00A0-\uFFFF$'&._\-]*[a-zA-Z\u00A0-\uFFFF'&._\-][a-zA-Z0-9\u00A0-\uFFFF'&._\-]*/
    def process_lex_TERMINAL( self, lark_node ):
        if self.util.get_type( lark_node ) == 'TERMINAL':
            return lark_node.value
        else:
           return ""


    # NONTERMINAL              : /<[\\\[\]\^\- !#$%&"'()*+,.:;=?@_`{|}a-zA-Z0-9\u00A0-\u00FF]*>/
    def process_lex_NONTERMINAL( self, lark_node ):
        if self.util.get_type( lark_node ) == 'NONTERMINAL':
            return lark_node.value
        else:
           return ""


    # QUOTED_STRING            : /"[\\\[\]\^\- !#$%&'()*+,.:;<=>?@_`{|}a-zA-Z0-9\u00A0-\uFFFF]*"/
    def process_lex_QUOTED_STRING( self, lark_node ):
        if self.util.get_type( lark_node ) == 'QUOTED_STRING':
            return lark_node.value
        else:
           return ""


    # OUT_CONTENT              : /[\\\^\- !#$%&"'()*+,.:;=?@_`{|}a-zA-Z0-9\u00A0-\u00FF]+/
    def process_lex_OUT_CONTENT( self, lark_node ):
        if self.util.get_type( lark_node ) == 'OUT_CONTENT':
            return lark_node.value
        else:
           return ""
