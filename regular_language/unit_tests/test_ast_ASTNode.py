#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for ast.ASTNode """

import unittest
import nlpregex.regular_language.ast


class test_ASTNode( unittest.TestCase ):


    def test_constructor_0001(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )
        
        self.assertEqual( node01.ast_node_type, 'abcd' )
        self.assertEqual( node01.content,       'efgh' )
        self.assertEqual( node01.repeat_min,    1      )
        self.assertEqual( node01.repeat_max,    1      )
        self.assertEqual( node01.phrase_count,  1      )
        self.assertEqual( node01.text_width,    0      )
        self.assertEqual( len(node01.out_token_pre),   0 )
        self.assertEqual( len(node01.out_token_post),  0 )



    def test_set_repeat_0001(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )
        node01.set_repeat(123, 456)
        
        self.assertEqual( node01.ast_node_type, 'abcd' )
        self.assertEqual( node01.content,       'efgh' )
        self.assertEqual( node01.repeat_min,    123    )
        self.assertEqual( node01.repeat_max,    456    )
        self.assertEqual( node01.phrase_count,  1      )
        self.assertEqual( node01.text_width,    0      )
        self.assertEqual( len(node01.out_token_pre),   0 )
        self.assertEqual( len(node01.out_token_post),  0 )



    def test_append_out_token_pre_0001(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )
        node01.append_out_token_pre('token1')
        
        self.assertEqual( node01.ast_node_type, 'abcd' )
        self.assertEqual( node01.content,       'efgh' )
        self.assertEqual( node01.repeat_min,    1      )
        self.assertEqual( node01.repeat_max,    1      )
        self.assertEqual( node01.phrase_count,  1      )
        self.assertEqual( node01.text_width,    0      )
        self.assertEqual( len(node01.out_token_pre),   1 )
        self.assertEqual( node01.out_token_pre[0],   'token1' )
        self.assertEqual( len(node01.out_token_post),  0 )



    def test_append_out_token_pre_0002(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )
        node01.append_out_token_pre('token1')
        node01.append_out_token_pre('token2')
        node01.append_out_token_pre('token3')
        
        self.assertEqual( node01.ast_node_type, 'abcd' )
        self.assertEqual( node01.content,       'efgh' )
        self.assertEqual( node01.repeat_min,    1      )
        self.assertEqual( node01.repeat_max,    1      )
        self.assertEqual( node01.phrase_count,  1      )
        self.assertEqual( node01.text_width,    0      )
        self.assertEqual( len(node01.out_token_pre),   3 )
        self.assertEqual( node01.out_token_pre[0],   'token1' )
        self.assertEqual( node01.out_token_pre[1],   'token2' )
        self.assertEqual( node01.out_token_pre[2],   'token3' )
        self.assertEqual( len(node01.out_token_post),  0 )


    def test_append_out_token_post_0001(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )
        node01.append_out_token_post('token1')
        
        self.assertEqual( node01.ast_node_type, 'abcd' )
        self.assertEqual( node01.content,       'efgh' )
        self.assertEqual( node01.repeat_min,    1      )
        self.assertEqual( node01.repeat_max,    1      )
        self.assertEqual( node01.phrase_count,  1      )
        self.assertEqual( node01.text_width,    0      )
        self.assertEqual( len(node01.out_token_pre),  0 )
        self.assertEqual( len(node01.out_token_post),   1 )
        self.assertEqual( node01.out_token_post[0],   'token1' )


    def test_append_out_token_post_0002(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )
        node01.append_out_token_post('token1')
        node01.append_out_token_post('token2')
        node01.append_out_token_post('token3')
        
        self.assertEqual( node01.ast_node_type, 'abcd' )
        self.assertEqual( node01.content,       'efgh' )
        self.assertEqual( node01.repeat_min,    1      )
        self.assertEqual( node01.repeat_max,    1      )
        self.assertEqual( node01.phrase_count,  1      )
        self.assertEqual( node01.text_width,    0      )
        self.assertEqual( len(node01.out_token_pre),  0 )
        self.assertEqual( len(node01.out_token_post),   3 )
        self.assertEqual( node01.out_token_post[0],   'token1' )
        self.assertEqual( node01.out_token_post[1],   'token2' )
        self.assertEqual( node01.out_token_post[2],   'token3' )


    def test_copy_from_0001(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )
        node01.set_repeat(123, 456)

        node01.phrase_count = 789
        node01.text_width   = 1023

        node01.append_out_token_pre('token1')
        node01.append_out_token_pre('token2')
        node01.append_out_token_pre('token3')

        node01.append_out_token_post('token4')
        node01.append_out_token_post('token5')
        node01.append_out_token_post('token6')

        node02 = nlpregex.regular_language.ast.ASTNode( '', '' )
        node02.copy_from(node01)

        node01.out_token_pre.append('token11')
        node01.out_token_post.append('token12')

        self.assertEqual( node02.ast_node_type, 'abcd' )
        self.assertEqual( node02.content,       'efgh' )
        self.assertEqual( node02.repeat_min,    123      )
        self.assertEqual( node02.repeat_max,    456      )
        self.assertEqual( node02.phrase_count,  789      )
        self.assertEqual( node02.text_width,    1023     )
        self.assertEqual( len(node02.out_token_pre),    3 )
        self.assertEqual( node02.out_token_pre[0],   'token1' )
        self.assertEqual( node02.out_token_pre[1],   'token2' )
        self.assertEqual( node02.out_token_pre[2],   'token3' )
        self.assertEqual( len(node02.out_token_pre),   3 )
        self.assertEqual( node02.out_token_post[0],   'token4' )
        self.assertEqual( node02.out_token_post[1],   'token5' )
        self.assertEqual( node02.out_token_post[2],   'token6' )


    def test_get_children_0001(self):

        node01 = nlpregex.regular_language.ast.ASTNode( 'abcd', 'efgh' )

        list01 = node01.get_children()
        self.assertEqual( len(list01),    0 )


    def test_get_children_0002(self):

        ast01  = nlpregex.regular_language.ast.AST()

        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'node03' )

        node01.add_to_graph(ast01)
        node02.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )

        list01 = node01.get_children()
        self.assertEqual( len(list01),   1      )
        self.assertEqual( list01[0],     node02 )


    def test_get_children_0003(self):

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

        list01 = node01.get_children()
        self.assertEqual( len(list01),   4      )
        self.assertEqual( list01[0],     node02 )
        self.assertEqual( list01[1],     node03 )
        self.assertEqual( list01[2],     node04 )
        self.assertEqual( list01[3],     node05 )



    def test_get_parentn0001(self):

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

        node06 = node01.get_parent()
        node07 = node02.get_parent()
        node08 = node03.get_parent()
        node09 = node04.get_parent()
        node10 = node05.get_parent()

        self.assertIsNone( node06 )
        self.assertEqual( node07,     node01 )
        self.assertEqual( node08,     node01 )
        self.assertEqual( node09,     node01 )
        self.assertEqual( node10,     node01 )


    def test_can_be_flattened_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node01.add_to_graph(ast01)
        res01 = node01.can_be_flattened()
        self.assertEqual( res01,  True )


    def test_can_be_flattened_0002(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token1')

        res01 = node01.can_be_flattened()
        self.assertEqual( res01,  False )


    def test_can_be_flattened_0003(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_post('token1')

        res01 = node01.can_be_flattened()
        self.assertEqual( res01,  False )


    def test_can_be_flattened_0004(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token1')
        node01.append_out_token_post('token1')

        res01 = node01.can_be_flattened()
        self.assertEqual( res01,  False )


    def test_attribute_for_expansion_before_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        str01 = node01.attribute_for_expansion_before( 1234 )
        self.assertEqual( str01,  '' )


    def test_attribute_for_expansion_after_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        str01 = node01.attribute_for_expansion_after( 1234 )
        self.assertEqual( str01,  '' )


    def test_prologue_for_formatted_text_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)
        str01 = node01.prologue_for_formatted_text()

        self.assertEqual( str01,  '' )


    def test_prologue_for_formatted_text_0002(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token1')

        str01 = node01.prologue_for_formatted_text()

        self.assertEqual( str01,  '[ token1 ]' )


    def test_prologue_for_formatted_text_0003(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token1')
        node01.append_out_token_pre('token2')

        str01 = node01.prologue_for_formatted_text()

        self.assertEqual( str01,  '[ token2 token1 ]' )


    def test_epilogue_for_formatted_text_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)
        str01 = node01.epilogue_for_formatted_text()

        self.assertEqual( str01,  '' )


    def test_epilogue_for_formatted_text_0002(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_post('token1')

        str01 = node01.epilogue_for_formatted_text()

        self.assertEqual( str01,  '[ token1 ]' )


    def test_epilogue_for_formatted_text_0003(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_post('token1')
        node01.append_out_token_post('token2')

        str01 = node01.epilogue_for_formatted_text()

        self.assertEqual( str01,  '[ token1 token2 ]' )


    def test_extra_epsilon_nodes_before_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        list01 = node01.extra_epsilon_nodes_before( )

        self.assertEqual( len(list01),  0 )


    def test_extra_epsilon_nodes_before_0002(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token1')

        str01 = node01.extra_epsilon_nodes_before( )

        self.assertEqual( str01,    'token1' )


    def test_extra_epsilon_nodes_before_0003(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token1')
        node01.append_out_token_pre('token2')

        str01 = node01.extra_epsilon_nodes_before( )

        self.assertEqual( str01,    'token2 token1' )


    def test_extra_epsilon_nodes_after_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        list01 = node01.extra_epsilon_nodes_after( )

        self.assertEqual( len(list01),  0 )


    def test_extra_epsilon_nodes_after_0002(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_post('token1')

        str01 = node01.extra_epsilon_nodes_after( )

        self.assertEqual( str01,    'token1' )


    def test_extra_epsilon_nodes_after_0003(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_post('token1')
        node01.append_out_token_post('token2')

        str01 = node01.extra_epsilon_nodes_after( )

        self.assertEqual( str01,    'token1 token2' )


    def test_node_content_for_fst_main_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        pair01 = node01.node_content_for_fst_main( 1234 )


        self.assertEqual( pair01,  ('node01', '') )


    def test_save_attributes_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token1')
        node01.append_out_token_pre('token2')
        node01.append_out_token_pre('token3')

        node01.append_out_token_post('token4')
        node01.append_out_token_post('token5')
        node01.append_out_token_post('token6')

        (attr01, attr02) = node01.save_attributes()
        
        self.assertEqual( len(attr01),  3 )
        self.assertEqual( len(attr02),  3 )
        
        self.assertEqual( attr01[0],  'token1' )
        self.assertEqual( attr01[1],  'token2' )
        self.assertEqual( attr01[2],  'token3' )

        self.assertEqual( attr02[0],  'token4' )
        self.assertEqual( attr02[1],  'token5' )
        self.assertEqual( attr02[2],  'token6' )


    def test_merge_attributes_0001(self):

        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'node02' )
        node02.add_to_graph(ast01)

        node02.append_out_token_pre('token11')
        node02.append_out_token_pre('token12')
        node02.append_out_token_pre('token13')

        node02.append_out_token_post('token14')
        node02.append_out_token_post('token15')
        node02.append_out_token_post('token16')


        attr01 = node01.save_attributes()
        node02.merge_attributes(attr01)

        self.assertEqual( len(node02.out_token_pre),    6 )
        self.assertEqual( node02.out_token_pre[0],   'token11' )
        self.assertEqual( node02.out_token_pre[1],   'token12' )
        self.assertEqual( node02.out_token_pre[2],   'token13' )
        self.assertEqual( node02.out_token_pre[3],   'token01' )
        self.assertEqual( node02.out_token_pre[4],   'token02' )
        self.assertEqual( node02.out_token_pre[5],   'token03' )

        self.assertEqual( len(node02.out_token_pre),   6 )

        self.assertEqual( node02.out_token_post[0],   'token14' )
        self.assertEqual( node02.out_token_post[1],   'token15' )
        self.assertEqual( node02.out_token_post[2],   'token16' )
        self.assertEqual( node02.out_token_post[3],   'token04' )
        self.assertEqual( node02.out_token_post[4],   'token05' )
        self.assertEqual( node02.out_token_post[5],   'token06' )


    def test_generate_string_for_drawing_0001(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'terminal',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"string01"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] string01 [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0002(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'nonterminal',    '<string01>' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"<string01>"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] <string01> [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0002(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'epsilon',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        str01, res01 = node01.generate_string_for_drawing( False )
        str02, res02 = node01.generate_string_for_drawing( True  )

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"ε"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] ε [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0003(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"SEQ"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] SEQ [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0004(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )

        node02.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )

        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  False )
        self.assertEqual( res02,  False )
        self.assertEqual( str01,  '"term01"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] term01 [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0005(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term03' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )

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


        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  False )
        self.assertEqual( res02,  False )
        self.assertEqual( str01,  '"term01 term02 term03 term04"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] term01 term02 term03 term04 [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0006(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term03' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )

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


        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"|"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] | [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0007(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'infinite repeat',    'string01' )
        node01.add_to_graph(ast01)
        node01.set_repeat(1, -1)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )

        node02.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )

        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"+"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] + [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0008(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'infinite repeat',    'string01' )
        node01.add_to_graph(ast01)
        node01.set_repeat(0, -1)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )

        node02.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )

        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"*"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] * [ token04 token05 token06 ]"' )


    def test_generate_string_for_drawing_0009(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'finite repeat',    'string01' )
        node01.add_to_graph(ast01)
        node01.set_repeat(12345, 67890)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )

        node02.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )

        str01, res01 = node01.generate_string_for_drawing(False)
        str02, res02 = node01.generate_string_for_drawing(True)

        self.assertEqual( res01,  True )
        self.assertEqual( res02,  True )
        self.assertEqual( str01,  '"{ 12345, 67890 }"' )
        self.assertEqual( str02,  '"[ token03 token02 token01 ] { 12345, 67890 } [ token04 token05 token06 ]"' )


    def test_are_children_all_terminals_0001(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        res01 = node01.are_children_all_terminals(False)
        self.assertEqual( res01,  False )


    def test_are_children_all_terminals_0002(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term03' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )

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

        res01 = node01.are_children_all_terminals(False)
        self.assertEqual( res01,  True )


    def test_are_children_all_terminals_0003(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm03>' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )

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

        res01 = node01.are_children_all_terminals(False)
        self.assertEqual( res01,  False )


    def test_are_children_all_terminals_0004(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm01>' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm02>' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm03>' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm04>' )

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

        res01 = node01.are_children_all_terminals(False)
        self.assertEqual( res01,  False )


    def test_are_children_all_terminals_0005(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        res01 = node01.are_children_all_terminals(True)
        self.assertEqual( res01,  False )


    def test_are_children_all_terminals_0006(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term03' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )

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

        res01 = node01.are_children_all_terminals(True)
        self.assertEqual( res01,  True )


    def test_are_children_all_terminals_0007(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm03>' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )

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

        res01 = node01.are_children_all_terminals(True)
        self.assertEqual( res01,  False )


    def test_are_children_all_terminals_0008(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term03' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )


        node03.append_out_token_pre('token07')
        node03.append_out_token_pre('token08')
        node03.append_out_token_pre('token09')

        node03.append_out_token_post('token10')
        node03.append_out_token_post('token11')
        node03.append_out_token_post('token12')


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

        res01 = node01.are_children_all_terminals(True)
        self.assertEqual( res01,  False )


    def test_are_children_all_terminals_0009(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'union',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm01>' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm02>' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm03>' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'nonterminal', '<nonterm04>' )

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

        res01 = node01.are_children_all_terminals(True)
        self.assertEqual( res01,  False )


    def test_aggregate_child_labels_0001(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        str01 = node01.aggregate_child_labels()
        self.assertEqual( str01,  '' )


    def test_aggregate_child_labels_0002(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )

        node02.add_to_graph(ast01)

        edge01 = nlpregex.regular_language.ast.ASTEdge()

        edge01.add_to_graph( ast01, node01, node02, "directed" )

        str01 = node01.aggregate_child_labels()
        self.assertEqual( str01,  'term01' )


    def test_aggregate_child_labels_0003(self):
        
        ast01  = nlpregex.regular_language.ast.AST()
        node01 = nlpregex.regular_language.ast.ASTNode( 'sequence',    'string01' )
        node01.add_to_graph(ast01)

        node01.append_out_token_pre('token01')
        node01.append_out_token_pre('token02')
        node01.append_out_token_pre('token03')

        node01.append_out_token_post('token04')
        node01.append_out_token_post('token05')
        node01.append_out_token_post('token06')

        node02 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term01' )
        node03 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term02' )
        node04 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term03' )
        node05 = nlpregex.regular_language.ast.ASTNode( 'terminal', 'term04' )

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

        str01 = node01.aggregate_child_labels()
        self.assertEqual( str01,  'term01 term02 term03 term04' )



if __name__ == '__main__':
    unittest.main()
