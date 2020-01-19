#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.py."""

import unittest
import nlpregex.regular_language.ast


class test_cross_product( unittest.TestCase ):


    def test_cross_product_0_0(self):

        list01 = []
        list02 = []
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 0 )


    def test_cross_product_0_1(self):

        list01 = []
        list02 = ['a']
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 1 )
        self.assertEqual( list03[0], 'a' )


    def test_cross_product_0_2(self):

        list01 = []
        list02 = ['a', 'b']
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 2 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )


    def test_cross_product_0_5(self):

        list01 = []
        list02 = ['a', 'b', 'c', 'd', 'e' ]
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 5 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )
        self.assertEqual( list03[2], 'c' )
        self.assertEqual( list03[3], 'd' )
        self.assertEqual( list03[4], 'e' )


    def test_cross_product_1_0(self):

        list01 = ['a']
        list02 = []

        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 1 )
        self.assertEqual( list03[0], 'a' )


    def test_cross_product_2_0(self):

        list01 = ['a', 'b']
        list02 = []
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 2 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )


    def test_cross_product_5_0(self):

        list01 = ['a', 'b', 'c', 'd', 'e' ]
        list02 = []
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 5 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )
        self.assertEqual( list03[2], 'c' )
        self.assertEqual( list03[3], 'd' )
        self.assertEqual( list03[4], 'e' )


    def test_cross_product_1_1(self):

        list01 = ['' ]
        list02 = ['a']
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 1 )
        self.assertEqual( list03[0], 'a' )


    def test_cross_product_1_2(self):

        list01 = ['' ]
        list02 = ['a', 'b']
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 2 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )


    def test_cross_product_1_5(self):

        list01 = ['' ]
        list02 = ['a', 'b', 'c', 'd', 'e']
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 5 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )
        self.assertEqual( list03[2], 'c' )
        self.assertEqual( list03[3], 'd' )
        self.assertEqual( list03[4], 'e' )


    def test_cross_product_1_1_p2(self):

        list01 = ['a']
        list02 = ['' ]
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 1 )
        self.assertEqual( list03[0], 'a' )


    def test_cross_product_2_1(self):

        list01 = ['a', 'b']
        list02 = ['' ]
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 2 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )


    def test_cross_product_5_1(self):

        list01 = ['a', 'b', 'c', 'd', 'e']
        list02 = ['' ]
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 5 )
        self.assertEqual( list03[0], 'a' )
        self.assertEqual( list03[1], 'b' )
        self.assertEqual( list03[2], 'c' )
        self.assertEqual( list03[3], 'd' )
        self.assertEqual( list03[4], 'e' )


    def test_cross_product_pattern_100(self):

        list01 = ['a', '']
        list02 = ['x', 'y', 'z' ]
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, '#' )
        
        self.assertEqual( len(list03), 6 )
        self.assertEqual( list03[0], 'a#x' )
        self.assertEqual( list03[1], 'a#y' )
        self.assertEqual( list03[2], 'a#z' )
        self.assertEqual( list03[3], 'x' )
        self.assertEqual( list03[4], 'y' )
        self.assertEqual( list03[5], 'z' )


    def test_cross_product_pattern_101(self):

        list01 = ['ab', 'cd', '456']
        list02 = ['mno', 'zyx', '', '123' ]
        list03 = nlpregex.regular_language.ast.cross_product( list01, list02, ' ' )
        
        self.assertEqual( len(list03), 12 )
        self.assertEqual( list03[0], 'ab mno' )
        self.assertEqual( list03[1], 'ab zyx' )
        self.assertEqual( list03[2], 'ab' )
        self.assertEqual( list03[3], 'ab 123' )
        self.assertEqual( list03[4], 'cd mno' )
        self.assertEqual( list03[5], 'cd zyx' )
        self.assertEqual( list03[6], 'cd' )
        self.assertEqual( list03[7], 'cd 123' )


        self.assertEqual( list03[0], 'ab mno' )
        self.assertEqual( list03[1], 'ab zyx' )
        self.assertEqual( list03[2], 'ab' )
        self.assertEqual( list03[3], 'ab 123' )


class test_create_sequence_subtree( unittest.TestCase ):

    def test_create_sequence_subtree_0000(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node02 = nlpregex.regular_language.ast.ASTNode( 'union',    'node02' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node03' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node04' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node05' )
        node06 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node06' )

        node01.add_to_graph(ast01)
        node02.add_to_graph(ast01)
        node03.add_to_graph(ast01)
        node04.add_to_graph(ast01)
        node05.add_to_graph(ast01)
        node06.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()
        edge02 = nlpregex.regular_language.ast.ASTEdge()
        edge03 = nlpregex.regular_language.ast.ASTEdge()
        edge04 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node03, "directed" )
        edge02.add_to_graph( ast01, node01, node04, "directed" )
        edge03.add_to_graph( ast01, node02, node05, "directed" )
        edge04.add_to_graph( ast01, node02, node06, "directed" )

        node07 = nlpregex.regular_language.ast.create_sequence_subtree( node01, node02, ast01 )

        self.assertEqual( node07.ast_node_type,        'sequence' )
        self.assertEqual( node07.content,              '' )
        self.assertEqual( node07.repeat_min,           1 )
        self.assertEqual( node07.repeat_max,           1 )
        self.assertEqual( node07.phrase_count,         1 )
        self.assertEqual( node07.text_width,           0 )
        self.assertEqual( len(node07.out_token_pre),   0 )
        self.assertEqual( len(node07.out_token_post),  0 )
        self.assertEqual( node07.out_degree(),         2 )
        self.assertEqual( node07.in_degree(),          0 )

        edge05 = node07.out_neighbors()[0]
        edge06 = node07.out_neighbors()[1]

        node08 = edge05.other_node_of(node07)
        node09 = edge06.other_node_of(node07)

        self.assertEqual( node01, node08 )
        self.assertEqual( node02, node09 )


class test_create_finite_repeat_subtree( unittest.TestCase ):

    def test_create_finite_repeat_subtree_0000(self):

        ast01  = nlpregex.regular_language.ast.AST()

        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node03' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node04' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node05' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node06' )

        node01.add_to_graph(ast01)
        node02.add_to_graph(ast01)
        node03.add_to_graph(ast01)
        node04.add_to_graph(ast01)
        node05.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()
        edge02 = nlpregex.regular_language.ast.ASTEdge()
        edge03 = nlpregex.regular_language.ast.ASTEdge()
        edge04 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )
        edge02.add_to_graph( ast01, node01, node03, "directed" )
        edge03.add_to_graph( ast01, node01, node04, "directed" )
        edge04.add_to_graph( ast01, node01, node05, "directed" )

        node06 = nlpregex.regular_language.ast.create_finite_repeat_subtree( node01, 2, 3, ast01 )

        self.assertEqual( node06.ast_node_type,        'finite repeat' )
        self.assertEqual( node06.content,              '' )
        self.assertEqual( node06.repeat_min,           2 )
        self.assertEqual( node06.repeat_max,           3 )
        self.assertEqual( node06.phrase_count,         1 )
        self.assertEqual( node06.text_width,           0 )
        self.assertEqual( len(node06.out_token_pre),   0 )
        self.assertEqual( len(node06.out_token_post),  0 )
        self.assertEqual( node06.out_degree(),         1 )
        self.assertEqual( node06.in_degree(),          0 )

        edge05 = node06.out_neighbors()[0]

        node07 = edge05.other_node_of(node06)

        self.assertEqual( node01, node07 )


class test_create_infinite_repeat_subtree( unittest.TestCase ):


    def test_create_infinite_repeat_subtree_0000(self):

        ast01  = nlpregex.regular_language.ast.AST()

        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node03' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node04' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node05' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node06' )

        node01.add_to_graph(ast01)
        node02.add_to_graph(ast01)
        node03.add_to_graph(ast01)
        node04.add_to_graph(ast01)
        node05.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()
        edge02 = nlpregex.regular_language.ast.ASTEdge()
        edge03 = nlpregex.regular_language.ast.ASTEdge()
        edge04 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )
        edge02.add_to_graph( ast01, node01, node03, "directed" )
        edge03.add_to_graph( ast01, node01, node04, "directed" )
        edge04.add_to_graph( ast01, node01, node05, "directed" )

        node06 = nlpregex.regular_language.ast.create_infinite_repeat_subtree( node01, 'PLUS', ast01 )

        self.assertEqual( node06.ast_node_type,        'infinite repeat' )
        self.assertEqual( node06.content,              '' )
        self.assertEqual( node06.repeat_min,           1 )
        self.assertEqual( node06.repeat_max,           -1 )
        self.assertEqual( node06.phrase_count,         1 )
        self.assertEqual( node06.text_width,           0 )
        self.assertEqual( len(node06.out_token_pre),   0 )
        self.assertEqual( len(node06.out_token_post),  0 )
        self.assertEqual( node06.out_degree(),         1 )
        self.assertEqual( node06.in_degree(),          0 )

        edge05 = node06.out_neighbors()[0]

        node07 = edge05.other_node_of(node06)

        self.assertEqual( node01, node07 )


    def test_create_infinite_repeat_subtree_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()

        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node03' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node04' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node05' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node06' )

        node01.add_to_graph(ast01)
        node02.add_to_graph(ast01)
        node03.add_to_graph(ast01)
        node04.add_to_graph(ast01)
        node05.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()
        edge02 = nlpregex.regular_language.ast.ASTEdge()
        edge03 = nlpregex.regular_language.ast.ASTEdge()
        edge04 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )
        edge02.add_to_graph( ast01, node01, node03, "directed" )
        edge03.add_to_graph( ast01, node01, node04, "directed" )
        edge04.add_to_graph( ast01, node01, node05, "directed" )

        node06 = nlpregex.regular_language.ast.create_infinite_repeat_subtree( node01, 'STAR', ast01 )

        self.assertEqual( node06.ast_node_type,        'infinite repeat' )
        self.assertEqual( node06.content,              '' )
        self.assertEqual( node06.repeat_min,           0 )
        self.assertEqual( node06.repeat_max,           -1 )
        self.assertEqual( node06.phrase_count,         1 )
        self.assertEqual( node06.text_width,           0 )
        self.assertEqual( len(node06.out_token_pre),   0 )
        self.assertEqual( len(node06.out_token_post),  0 )
        self.assertEqual( node06.out_degree(),         1 )
        self.assertEqual( node06.in_degree(),          0 )

        edge05 = node06.out_neighbors()[0]

        node07 = edge05.other_node_of(node06)

        self.assertEqual( node01, node07 )



if __name__ == '__main__':
    unittest.main()
