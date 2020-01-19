#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for sse_forrest.sseASTNode """

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.sse_forrest

class test_sseASTNode( unittest.TestCase ):


    def test_constructor_0001(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 't0' )
        
        self.assertEqual( node01.ast_node_type, 't0' )
        self.assertEqual( node01.regex,         't0' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,     -1    )      


    def test_clone_0001(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )

        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )

        node01.regex              = 't1 t2 t3'
        node01.children_map['t1'] = node02
        node01.children_map['t2'] = node03
        node01.children_map['t3'] = node04
        node01.num_terms          = 3
        node01.height             = 4
        node01.node_id            = 5


        node05 = node01.clone()

        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2 t3' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     3    )
        self.assertEqual( node05.height,        4    )
        self.assertEqual( node05.node_id ,     -1    )
        

    def test_clone_0002(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )

        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )

        node01.regex              = 't1 t2 t3'
        node01.children_map['t1'] = node02
        node01.children_map['t2'] = node03
        node01.children_map['t3'] = node04
        node01.num_terms          = 3
        node01.height             = 4
        node01.node_id            = 5

        node05 = node01.clone()

        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2 t3' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     3    )
        self.assertEqual( node05.height,        4    )
        self.assertEqual( node05.node_id ,     -1    )
        

    def test_clone_0003(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )

        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )

        node01.regex              = 't1 t2 t3'
        node01.children_map['t1'] = node02
        node01.children_map['t2'] = node03
        node01.children_map['t3'] = node04
        node01.num_terms          = 3
        node01.height             = 4
        node01.node_id            = 5

        node05 = node01.clone()

        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2 t3' )
        self.assertEqual( len(node05.children_map.keys()),  0   ) # 2020-01-14 clone no longer copies it.
        #self.assertEqual( node05.children_map['t1'],  node02 )
        #self.assertEqual( node05.children_map['t2'],  node03 )
        #self.assertEqual( node05.children_map['t3'],  node04 )
        self.assertEqual( node05.num_terms,     3    )
        self.assertEqual( node05.height,        4    )
        self.assertEqual( node05.node_id ,     -1    )
        

    def test_hash_eq_ne_0001(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 't0' )
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )

        node01.node_id            = 4
        node02.node_id            = 3
        node03.node_id            = 2
        node04.node_id            = 1

        set01 = set()
        set01.add( node01 )
        set01.add( node02 )
        set01.add( node03 )
        set01.add( node04 )

        list01 = list(set01)        
        self.assertEqual( list01[0] ,node04 )
        self.assertEqual( list01[1] ,node03 )
        self.assertEqual( list01[2] ,node02 )
        self.assertEqual( list01[3] ,node01 )


    def test_reset_0001(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 't0' )

        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )

        node01.regex              = 't1 t2 t3'
        node01.children_map['t1'] = node02
        node01.children_map['t2'] = node03
        node01.children_map['t3'] = node04
        node01.num_terms          = 3
        node01.height             = 4
        node01.node_id            = 5

        node01.reset('t10')

        self.assertEqual( node01.ast_node_type, 't10' )
        self.assertEqual( node01.regex,         't10' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,      5     )


    def test_generate_children_map_for_union_0001(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 't0' )
        node01.add_to_graph(forrest01)

        node01.generate_children_map_for_union()

        self.assertEqual( node01.ast_node_type, 't0' )
        self.assertEqual( node01.regex,         't0' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_children_map_for_union_0002(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'n1' )
        node01.add_to_graph(forrest01)

        node01.generate_children_map_for_union()

        self.assertEqual( node01.ast_node_type, 'n1' )
        self.assertEqual( node01.regex,         'n1' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_children_map_for_union_0003(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 't4' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_children_map_for_union()

        self.assertEqual( node01.ast_node_type, 's' )
        self.assertEqual( node01.regex,         's' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_children_map_for_union_0004(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'e' )
        node01.add_to_graph(forrest01)

        node01.generate_children_map_for_union()

        self.assertEqual( node01.ast_node_type, 'e' )
        self.assertEqual( node01.regex,         'e' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_children_map_for_union_0005(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '*' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node01.generate_children_map_for_union()

        self.assertEqual( node01.ast_node_type, '*' )
        self.assertEqual( node01.regex,         '*' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )
 

    def test_generate_children_map_for_union_0006(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'u' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 't4' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_children_map_for_union()

        self.assertEqual( node01.ast_node_type,       'u'    )
        self.assertEqual( node01.regex,               'u'    )
        self.assertEqual( len(node01.children_map),   5      )
        self.assertEqual( node01.children_map['t1'],  node02 )
        self.assertEqual( node01.children_map['t2'],  node03 )
        self.assertEqual( node01.children_map['t3'],  node04 )
        self.assertEqual( node01.children_map['t4'],  node05 )
        self.assertEqual( node01.children_map['t5'],  node06 )
        self.assertEqual( node01.num_terms,           0      )
        self.assertEqual( node01.height,              0      )
        self.assertEqual( node01.node_id ,            -1     )


    # each type
    #     depth 1
    #     depth 2
    #     depth 3


    def test_generate_regex_0001(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 't1' )
        self.assertEqual( node01.regex,         't1' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0002(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'n1' )

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 'n1' )
        self.assertEqual( node01.regex,         'n1' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0003(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'e' )

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 'e' )
        self.assertEqual( node01.regex,         'e' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0004(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'u' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 't4' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 'u' )
        self.assertEqual( node01.regex,         '( t1 | t2 | t3 | t4 | t5 )' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0005(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'u' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 'u' )
        self.assertEqual( node01.regex,         '( t1 )' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0006(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 's'   )
        self.assertEqual( node01.regex,         't3 t1 t5 t2 t3' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,      -1    )


    def test_generate_regex_0007(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 's' )
        self.assertEqual( node01.regex,         't1' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0008(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '*' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, '*' )
        self.assertEqual( node01.regex,         't1 *' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0009(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '*' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't01' )
        node03.add_to_graph(forrest01)
        edge02_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge02_03.add_to_graph(forrest01, node02, node03, "directed")

        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't02' )
        node04.add_to_graph(forrest01)
        edge02_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge02_04.add_to_graph(forrest01, node02, node04, "directed")

        node02.generate_regex()
        node01.generate_regex()


        self.assertEqual( node01.ast_node_type, '*' )
        self.assertEqual( node01.regex,         '( t01 t02 ) *' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0010(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '*' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't01' )
        node03.add_to_graph(forrest01)
        edge02_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge02_03.add_to_graph(forrest01, node02, node03, "directed")

        node02.generate_regex()
        node01.generate_regex()


        self.assertEqual( node01.ast_node_type, '*' )
        self.assertEqual( node01.regex,         't01 *' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0011(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '?' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't01' )
        node03.add_to_graph(forrest01)
        edge02_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge02_03.add_to_graph(forrest01, node02, node03, "directed")

        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't02' )
        node04.add_to_graph(forrest01)
        edge02_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge02_04.add_to_graph(forrest01, node02, node04, "directed")

        node02.generate_regex()
        node01.generate_regex()


        self.assertEqual( node01.ast_node_type, '?' )
        self.assertEqual( node01.regex,         '( t01 t02 ) ?' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0012(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '?' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't01' )
        node03.add_to_graph(forrest01)
        edge02_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge02_03.add_to_graph(forrest01, node02, node03, "directed")

        node02.generate_regex()
        node01.generate_regex()


        self.assertEqual( node01.ast_node_type, '?' )
        self.assertEqual( node01.regex,         't01 ?' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_generate_regex_0013(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'r' )

        node01.generate_regex()

        self.assertEqual( node01.ast_node_type, 'r' )
        self.assertEqual( node01.regex,         'r' )
        self.assertEqual( node01.children_map,  {}    )
        self.assertEqual( node01.num_terms,     0     )
        self.assertEqual( node01.height,        0     )
        self.assertEqual( node01.node_id ,     -1     )


    def test_has_epsilon_child_0001(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'r' )

        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, False )


    def test_has_epsilon_child_0002(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 't0' )

        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, False )


    def test_has_epsilon_child_0003(self):

        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'n0' )

        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, False )


    def test_has_epsilon_child_0004(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_regex()

        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, False )


    def test_has_epsilon_child_0005(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 'e' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 't2' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_regex()

        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, True )


    def test_has_epsilon_child_0006(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 's' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 'e' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 'e' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_regex()

        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, True )


    def test_has_epsilon_child_0007(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'u' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 'e' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_regex()
        node01.generate_children_map_for_union()


        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, True )


    def test_has_epsilon_child_0008(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( 'u' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")
        node03 = nlpregex.regular_language.sse_forrest.sseASTNode( 't1' )
        node03.add_to_graph(forrest01)
        edge01_03 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_03.add_to_graph(forrest01, node01, node03, "directed")
        node04 = nlpregex.regular_language.sse_forrest.sseASTNode( 't5' )
        node04.add_to_graph(forrest01)
        edge01_04 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_04.add_to_graph(forrest01, node01, node04, "directed")
        node05 = nlpregex.regular_language.sse_forrest.sseASTNode( 't4' )
        node05.add_to_graph(forrest01)
        edge01_05 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_05.add_to_graph(forrest01, node01, node05, "directed")
        node06 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node06.add_to_graph(forrest01)
        edge01_06 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_06.add_to_graph(forrest01, node01, node06, "directed")

        node01.generate_regex()
        node01.generate_children_map_for_union()


        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, False )


    def test_has_epsilon_child_0009(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '*' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node01.generate_regex()
        node01.generate_children_map_for_union()


        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, False )



    def test_has_epsilon_child_0010(self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()
        node01 = nlpregex.regular_language.sse_forrest.sseASTNode( '?' )
        node01.add_to_graph(forrest01)
        node02 = nlpregex.regular_language.sse_forrest.sseASTNode( 't3' )
        node02.add_to_graph(forrest01)
        edge01_02 = nlpregex.regular_language.sse_forrest.sseASTEdge()
        edge01_02.add_to_graph(forrest01, node01, node02, "directed")

        node01.generate_regex()
        node01.generate_children_map_for_union()


        res01 = node01.has_epsilon_child()

        self.assertEqual( res01, False )



if __name__ == '__main__':
    unittest.main()
