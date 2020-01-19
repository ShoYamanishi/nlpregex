#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for sse_forrest.sseASForrest """

import unittest
import nlpregex.regular_language.ast
import nlpregex.regular_language.sse_forrest

from nlpregex.regular_language.unit_tests.test_sse_asforrest_helper import test_sse_ASForrest_helper


class test_sseASForrest( unittest.TestCase ):


    def __init__( self, *args, **kwargs ):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.helper = test_sse_ASForrest_helper()


    def create_initial_serial_node( self, forrest, children ):

       if len( children ) == 0:
           return forrest.create_initial_node('e')

       if len( children )== 1:
           return forrest.create_initial_node( children[0] )

       r = forrest.create_initial_node('s' )

       for c in children:
           n = forrest.create_initial_node( c )
           e = nlpregex.regular_language.sse_forrest.sseASTEdge()
           e.add_to_graph( forrest, r, n, "directed" )

       r.generate_regex()

       return  r


    def add_question_node( self, forrest, n ):

       r = forrest.create_initial_node('?' )

       e = nlpregex.regular_language.sse_forrest.sseASTEdge()
       e.add_to_graph( forrest, r, n, "directed" )
       r.generate_regex()

       return  r


    def test_constructor_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        self.assertEqual( forrest01.next_nonterminal_num, 1 )
        self.assertEqual( forrest01.node_id_next,         0 )


    def test_next_node_id_allocation_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        id01 = forrest01.next_node_id_allocation()
        self.assertEqual( id01,                    0 )
        self.assertEqual( forrest01.node_id_next,  1 )

        id02 = forrest01.next_node_id_allocation()
        self.assertEqual( id02,                    1 )
        self.assertEqual( forrest01.node_id_next,  2 )

        id03 = forrest01.next_node_id_allocation()
        self.assertEqual( id03,                    2 )
        self.assertEqual( forrest01.node_id_next,  3 )


    def test_allocate_nonterminal_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        nt01 = forrest01.allocate_nonterminal()
        self.assertEqual( nt01,                           'n1' )
        self.assertEqual( forrest01.next_nonterminal_num,  2   )

        nt02 = forrest01.allocate_nonterminal()
        self.assertEqual( nt02,                           'n2' )
        self.assertEqual( forrest01.next_nonterminal_num,  3   )

        nt03 = forrest01.allocate_nonterminal()
        self.assertEqual( nt03,                           'n3' )
        self.assertEqual( forrest01.next_nonterminal_num,  4   )

        nt04 = forrest01.allocate_nonterminal()
        self.assertEqual( nt04,                           'n4' )
        self.assertEqual( forrest01.next_nonterminal_num,  5   )

        forrest01.reset_nonterminal_num_allocation()

        nt05 = forrest01.allocate_nonterminal()
        self.assertEqual( nt05,                           'n1' )
        self.assertEqual( forrest01.next_nonterminal_num,  2   )

        nt06 = forrest01.allocate_nonterminal()
        self.assertEqual( nt06,                           'n2' )
        self.assertEqual( forrest01.next_nonterminal_num,  3   )

        nt07 = forrest01.allocate_nonterminal()
        self.assertEqual( nt07,                           'n3' )
        self.assertEqual( forrest01.next_nonterminal_num,  4   )


    def test_remove_duplication_and_order_children_0001( self ): 

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()        
        list01    = forrest01.remove_duplication_and_order_children( ['e','t1','t2','t3', 'n4'] )
        self.assertEqual( list01, [ 'e','n4', 't1','t2','t3' ] )


    def test_remove_duplication_and_order_children_0002( self ): 

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()        
        list01    = forrest01.remove_duplication_and_order_children( ['t1','t1','t2','t2', 't1'] )
        self.assertEqual( list01, [ 't1','t2' ] )


    # 'e'
    def test_create_initial_node_0001( self ):
 
        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')
 
        self.assertEqual( node01.ast_node_type, 'e' )
        self.assertEqual( node01.regex,         'e' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # 't1'
    def test_create_initial_node_0002( self ):
 
        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')
 
        self.assertEqual( node01.ast_node_type, 't1' )
        self.assertEqual( node01.regex,         't1' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # 'n1'
    def test_create_initial_node_0003( self ):
 
        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')
 
        self.assertEqual( node01.ast_node_type, 'n1' )
        self.assertEqual( node01.regex,         'n1' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # 'u'
    def test_create_initial_node_0004( self ):
 
        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('u')
 
        self.assertEqual( node01.ast_node_type, 'u' )
        self.assertEqual( node01.regex,         'u' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # 's'
    def test_create_initial_node_0005( self ):
 
        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('s')
 
        self.assertEqual( node01.ast_node_type, 's' )
        self.assertEqual( node01.regex,         's' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # '*'
    def test_create_initial_node_0005( self ):
 
        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('*')
 
        self.assertEqual( node01.ast_node_type, '*' )
        self.assertEqual( node01.regex,         '*' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # '?'
    def test_create_initial_node_0006( self ):
 
        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('?')
 
        self.assertEqual( node01.ast_node_type, '?' )
        self.assertEqual( node01.regex,         '?' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # []
    def test_create_initial_union_node_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node([])
 
        self.assertEqual( node01, None )


    # ['e']
    def test_create_initial_union_node_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])
 
        self.assertEqual( node01.ast_node_type, 'e' )
        self.assertEqual( node01.regex,         'e' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # ['t1']
    def test_create_initial_union_node_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])
 
        self.assertEqual( node01.ast_node_type, 't1' )
        self.assertEqual( node01.regex,         't1' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # ['n1']
    def test_create_initial_union_node_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])
 
        self.assertEqual( node01.ast_node_type, 'n1' )
        self.assertEqual( node01.regex,         'n1' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # ['e', 't1']
    def test_create_initial_union_node_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e', 't1'])
 
        self.assertEqual( node01.ast_node_type, 'u' )
        self.assertEqual( node01.regex,         '( e | t1 )' )
        self.assertEqual( len(node01.children_map),  2   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      

        node02 = node01.children_map['e']
 
        self.assertEqual( node02.ast_node_type, 'e' )
        self.assertEqual( node02.regex,         'e' )
        self.assertEqual( node02.children_map,  {}   )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id ,      1    )

        node03 = node01.children_map['t1']
 
        self.assertEqual( node03.ast_node_type, 't1' )
        self.assertEqual( node03.regex,         't1' )
        self.assertEqual( node03.children_map,  {}   )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id ,      2    )      


    # ['t1', 't2']
    def test_create_initial_union_node_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])
 
        self.assertEqual( node01.ast_node_type, 'u' )
        self.assertEqual( node01.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node01.children_map),  2   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      

        node02 = node01.children_map['t1']
 
        self.assertEqual( node02.ast_node_type, 't1' )
        self.assertEqual( node02.regex,         't1' )
        self.assertEqual( node02.children_map,  {}   )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id ,      1    )

        node03 = node01.children_map['t2']
 
        self.assertEqual( node03.ast_node_type, 't2' )
        self.assertEqual( node03.regex,         't2' )
        self.assertEqual( node03.children_map,  {}   )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id ,      2    )      


    # ['t1', 't1']
    def test_create_initial_union_node_0007( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't1'])
 
        self.assertEqual( node01.ast_node_type, 't1' )
        self.assertEqual( node01.regex,         't1' )
        self.assertEqual( node01.children_map,  {}   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      


    # ['t1', 't1', 'e']
    def test_create_initial_union_node_0008( self ):


        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't1', 'e'])
 
        self.assertEqual( node01.ast_node_type, 'u' )
        self.assertEqual( node01.regex,         '( e | t1 )' )
        self.assertEqual( len(node01.children_map),  2   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      

        node02 = node01.children_map['e']
 
        self.assertEqual( node02.ast_node_type, 'e' )
        self.assertEqual( node02.regex,         'e' )
        self.assertEqual( node02.children_map,  {}   )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id ,      1    )

        node03 = node01.children_map['t1']
 
        self.assertEqual( node03.ast_node_type, 't1' )
        self.assertEqual( node03.regex,         't1' )
        self.assertEqual( node03.children_map,  {}   )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id ,      2    )      


    # ['t1', 't3', 't3', 't1']
    def test_create_initial_union_node_0009( self ):


        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't3', 't3', 't1'])
 
        self.assertEqual( node01.ast_node_type, 'u' )
        self.assertEqual( node01.regex,         '( t1 | t3 )' )
        self.assertEqual( len(node01.children_map),  2   )
        self.assertEqual( node01.num_terms,     0    )
        self.assertEqual( node01.height,        0    )
        self.assertEqual( node01.node_id ,      0    )      

        node02 = node01.children_map['t1']
 
        self.assertEqual( node02.ast_node_type, 't1' )
        self.assertEqual( node02.regex,         't1' )
        self.assertEqual( node02.children_map,  {}   )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id ,      1    )

        node03 = node01.children_map['t3']
 
        self.assertEqual( node03.ast_node_type, 't3' )
        self.assertEqual( node03.regex,         't3' )
        self.assertEqual( node03.children_map,  {}   )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id ,      2    )      


    # e   e
    def test_union_two_ASTs_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = forrest01.create_initial_union_node(['e'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'e' )
        self.assertEqual( node03.regex,         'e' )
        self.assertEqual( node03.children_map,  {}  )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       0   )


    # e   t1
    def test_union_two_ASTs_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = forrest01.create_initial_union_node(['t1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # e   t2
    def test_union_two_ASTs_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = forrest01.create_initial_union_node(['t2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # e   n1
    def test_union_two_ASTs_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = forrest01.create_initial_union_node(['n1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | n1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # e   n2
    def test_union_two_ASTs_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = forrest01.create_initial_union_node(['n2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | n2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # e   u
    def test_union_two_ASTs_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      2    )      


        node06 = node03.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )      


    # e   s
    def test_union_two_ASTs_0007( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # e   *
    def test_union_two_ASTs_0008( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | e )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['e']
 
        self.assertEqual( node05.ast_node_type, 'e' )
        self.assertEqual( node05.regex,         'e' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # e   ?
    def test_union_two_ASTs_0009( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['e'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | e )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['e']
 
        self.assertEqual( node05.ast_node_type, 'e' )
        self.assertEqual( node05.regex,         'e' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # t1   e
    def test_union_two_ASTs_0011( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = forrest01.create_initial_union_node(['e'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # t1   t1
    def test_union_two_ASTs_0012( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = forrest01.create_initial_union_node(['t1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 't1' )
        self.assertEqual( node03.regex,         't1' )
        self.assertEqual( node03.children_map,  {}  )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       0   )


    # t1   t2
    def test_union_two_ASTs_0013( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = forrest01.create_initial_union_node(['t2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # t1   n1
    def test_union_two_ASTs_0014( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = forrest01.create_initial_union_node(['n1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # t1   n2
    def test_union_two_ASTs_0015( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = forrest01.create_initial_union_node(['n2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # t1   u
    def test_union_two_ASTs_0016( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )


    # t1   s
    def test_union_two_ASTs_0017( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # t1   *
    def test_union_two_ASTs_0018( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # t1   ?
    def test_union_two_ASTs_0019( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # t2   e
    def test_union_two_ASTs_0021( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = forrest01.create_initial_union_node(['e'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # t2   t1
    def test_union_two_ASTs_0022( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = forrest01.create_initial_union_node(['t1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # t2   t2
    def test_union_two_ASTs_0023( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = forrest01.create_initial_union_node(['t2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 't2' )
        self.assertEqual( node03.regex,         't2' )
        self.assertEqual( node03.children_map,  {}  )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       0   )


    # t2   n1
    def test_union_two_ASTs_0024( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = forrest01.create_initial_union_node(['n1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t2']
 
        self.assertEqual( node04.ast_node_type, 't2' )
        self.assertEqual( node04.regex,         't2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # t2   n2
    def test_union_two_ASTs_0025( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = forrest01.create_initial_union_node(['n2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t2']
 
        self.assertEqual( node04.ast_node_type, 't2' )
        self.assertEqual( node04.regex,         't2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # t2   u
    def test_union_two_ASTs_0026( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      2    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )


    # t2   s
    def test_union_two_ASTs_0027( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 t2 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t2']
 
        self.assertEqual( node04.ast_node_type, 't2' )
        self.assertEqual( node04.regex,         't2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # t2   *
    def test_union_two_ASTs_0028( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # t2   ?
    def test_union_two_ASTs_0019( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # n1   e
    def test_union_two_ASTs_0031( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = forrest01.create_initial_union_node(['e'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | n1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # n1   t1
    def test_union_two_ASTs_0032( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = forrest01.create_initial_union_node(['t1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # n1   t2
    def test_union_two_ASTs_0033( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = forrest01.create_initial_union_node(['t2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t2']
 
        self.assertEqual( node04.ast_node_type, 't2' )
        self.assertEqual( node04.regex,         't2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # n1   n1
    def test_union_two_ASTs_0034( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = forrest01.create_initial_union_node(['n1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'n1' )
        self.assertEqual( node03.regex,         'n1' )
        self.assertEqual( node03.children_map,  {}  )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       0   )


    # n1   n2
    def test_union_two_ASTs_0035( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = forrest01.create_initial_union_node(['n2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | n2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['n1']
 
        self.assertEqual( node04.ast_node_type, 'n1' )
        self.assertEqual( node04.regex,         'n1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # n1   u
    def test_union_two_ASTs_0036( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      2    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )

        node06 = node03.children_map['n1']
 
        self.assertEqual( node06.ast_node_type, 'n1' )
        self.assertEqual( node06.regex,         'n1' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      0    )


    # n1   s
    def test_union_two_ASTs_0037( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['n1']
 
        self.assertEqual( node04.ast_node_type, 'n1' )
        self.assertEqual( node04.regex,         'n1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # n1   *
    def test_union_two_ASTs_0038( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | n1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # n1  ?
    def test_union_two_ASTs_0039( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n1'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | n1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # n2   e
    def test_union_two_ASTs_0041( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = forrest01.create_initial_union_node(['e'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | n2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # n2   t1
    def test_union_two_ASTs_0042( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = forrest01.create_initial_union_node(['t1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t1 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # n2   t2
    def test_union_two_ASTs_0043( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = forrest01.create_initial_union_node(['t2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['t2']
 
        self.assertEqual( node04.ast_node_type, 't2' )
        self.assertEqual( node04.regex,         't2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # n2   n1
    def test_union_two_ASTs_0044( self ):


        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = forrest01.create_initial_union_node(['n1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | n2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       2   )

        node04 = node03.children_map['n1']
 
        self.assertEqual( node04.ast_node_type, 'n1' )
        self.assertEqual( node04.regex,         'n1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )      


    # n2   n2
    def test_union_two_ASTs_0045( self ):


        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = forrest01.create_initial_union_node(['n2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'n2' )
        self.assertEqual( node03.regex,         'n2' )
        self.assertEqual( node03.children_map,  {}  )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       0   )


    # n2   u
    def test_union_two_ASTs_0046( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      2    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )

        node06 = node03.children_map['n2']
 
        self.assertEqual( node06.ast_node_type, 'n2' )
        self.assertEqual( node06.regex,         'n2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      0    )


    # n2   s
    def test_union_two_ASTs_0047( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['n2']
 
        self.assertEqual( node04.ast_node_type, 'n2' )
        self.assertEqual( node04.regex,         'n2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )      


    # n2   *
    def test_union_two_ASTs_0048( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | n2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # n2  ?
    def test_union_two_ASTs_0049( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['n2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | n2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )      


    # u   e
    def test_union_two_ASTs_0051( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_union_node(['e'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      3    )

        node05 = node03.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )

        node06 = node03.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      2    )


    # u   t1
    def test_union_two_ASTs_0052( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_union_node(['t1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      2    )      


    # u   t2
    def test_union_two_ASTs_0053( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't3'])

        node02 = forrest01.create_initial_union_node(['t2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 | t3 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )      

        node06 = node03.children_map['t3']
 
        self.assertEqual( node06.ast_node_type, 't3' )
        self.assertEqual( node06.regex,         't3' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      2    )      


    # u   n1
    def test_union_two_ASTs_0054( self ):


        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_union_node(['n1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['n1']
 
        self.assertEqual( node04.ast_node_type, 'n1' )
        self.assertEqual( node04.regex,         'n1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      3    )

        node05 = node03.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )

        node06 = node03.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      2    )      


    # u   n2
    def test_union_two_ASTs_0055( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_union_node(['n2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['n2']
 
        self.assertEqual( node04.ast_node_type, 'n2' )
        self.assertEqual( node04.regex,         'n2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      3    )

        node05 = node03.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )

        node06 = node03.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      2    )      


    # u   u
    def test_union_two_ASTs_0056( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       6   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      2    )


    # u   s
    def test_union_two_ASTs_0057( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t1 t2 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       6   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )      


        node06 = node03.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      2    )      


    # u   *
    def test_union_two_ASTs_0058( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t1 | t2 )' )
        self.assertEqual( len(node04.children_map), 3 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      6    )      


        node07 = node04.children_map['t2']
 
        self.assertEqual( node07.ast_node_type, 't2' )
        self.assertEqual( node07.regex,         't2' )
        self.assertEqual( node07.children_map,  {}   )
        self.assertEqual( node07.num_terms,     0    )
        self.assertEqual( node07.height,        0    )


    # u  ?
    def test_union_two_ASTs_0059( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t1 | t2 )' )
        self.assertEqual( len(node04.children_map), 3 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      1    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      6    )      

        node07 = node04.children_map['t2']
 
        self.assertEqual( node07.ast_node_type, 't2' )
        self.assertEqual( node07.regex,         't2' )
        self.assertEqual( node07.children_map,  {}   )
        self.assertEqual( node07.num_terms,     0    )
        self.assertEqual( node07.height,        0    )
        self.assertEqual( node07.node_id ,      2    )


    # s   e
    def test_union_two_ASTs_0061( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'])

        node02 = forrest01.create_initial_union_node(['e'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( e | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['e']
 
        self.assertEqual( node04.ast_node_type, 'e' )
        self.assertEqual( node04.regex,         'e' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      3    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )


    # s   t1
    def test_union_two_ASTs_0062( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_union_node(['t1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1 t2']
 
        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't1 t2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )      


    # s   t2
    def test_union_two_ASTs_0063( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't3'] )

        node02 = forrest01.create_initial_union_node(['t2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 t3 | t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['t1 t3']
 
        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't1 t3' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      0    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )      


    # s   n1
    def test_union_two_ASTs_0064( self ):


        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_union_node(['n1'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n1 | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['n1']
 
        self.assertEqual( node04.ast_node_type, 'n1' )
        self.assertEqual( node04.regex,         'n1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      3    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )


    # s   n2
    def test_union_two_ASTs_0065( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_union_node(['n2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( n2 | t1 t2 )' )
        self.assertEqual( len(node03.children_map), 2 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       4   )

        node04 = node03.children_map['n2']
 
        self.assertEqual( node04.ast_node_type, 'n2' )
        self.assertEqual( node04.regex,         'n2' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      3    )

        node05 = node03.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0   )


    # s   u
    def test_union_two_ASTs_0066( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t1 t2 | t2 )' )
        self.assertEqual( len(node03.children_map), 3 )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       6   )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      4    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      5    )


        node06 = node03.children_map['t1 t2']
 
        self.assertEqual( node06.ast_node_type, 's' )
        self.assertEqual( node06.regex,         't1 t2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      0    )


    # s   s
    def test_union_two_ASTs_0067( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.union_two_ASTs(node01, node02)
 
        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2' )
        self.assertEqual( node03.children_map,  {} )
        self.assertEqual( node03.num_terms,     0   )
        self.assertEqual( node03.height,        0   )
        self.assertEqual( node03.node_id,       0   )


    # s   *
    def test_union_two_ASTs_0068( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t1 t2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      6    )      


    # s  ?
    def test_union_two_ASTs_0069( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t3', 't4'] )

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.union_two_ASTs(node01, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t3 t4 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t3 t4']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't3 t4' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      0    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      6    )      


    # *   e
    def test_union_two_ASTs_0071( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'])
        node02 = forrest01.repeat_AST(node01)
        node03 = forrest01.create_initial_union_node(['e'])

        node04 = forrest01.union_two_ASTs( node02, node03 )
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | e )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['e']
 
        self.assertEqual( node05.ast_node_type, 'e' )
        self.assertEqual( node05.regex,         'e' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )


    # *   t1
    def test_union_two_ASTs_0072( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_union_node(['t1'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node05.ast_node_type, '*' )
        self.assertEqual( node05.regex,         '( t1 t2 ) *' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )

        node06 = node04.children_map['t1']
 
        self.assertEqual( node06.ast_node_type, 't1' )
        self.assertEqual( node06.regex,         't1' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )


    # *   t2
    def test_union_two_ASTs_0073( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_union_node(['t2'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node05.ast_node_type, '*' )
        self.assertEqual( node05.regex,         '( t1 t2 ) *' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )

        node06 = node04.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )


    # *   n1
    def test_union_two_ASTs_0074( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_union_node(['n1'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | n1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )


    # *   n2
    def test_union_two_ASTs_0075( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_union_node(['n2'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | n2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )


    # *   u
    def test_union_two_ASTs_0076( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_union_node(['t1', 't2'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t1 | t2 )' )
        self.assertEqual( len(node04.children_map), 3 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      5    )

        node06 = node04.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      6    )


        node07 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node07.ast_node_type, '*' )
        self.assertEqual( node07.regex,         '( t1 t2 ) *' )
        self.assertEqual( node07.children_map,  {}   )
        self.assertEqual( node07.num_terms,     0    )
        self.assertEqual( node07.height,        0    )
        self.assertEqual( node07.node_id ,      3    )


    # *   s
    def test_union_two_ASTs_0077( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )


        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) * | t1 t2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )      



    # *   *
    def test_union_two_ASTs_0078( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = forrest01.repeat_AST(node03)

        node05 = forrest01.union_two_ASTs(node02, node04)
 
        self.assertEqual( node04.ast_node_type, '*' )
        self.assertEqual( node04.regex,         '( t1 t2 ) *' )
        self.assertEqual( node04.children_map,  {} )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )


    # *  ?
    def test_union_two_ASTs_0079( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t3', 't4'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = self.add_question_node( forrest01, node03 )

        node05 = forrest01.union_two_ASTs(node02, node04)
 
        self.assertEqual( node05.ast_node_type, 'u' )
        self.assertEqual( node05.regex,         '( ( t1 t2 ) ? | ( t3 t4 ) * )' )
        self.assertEqual( len(node05.children_map), 2 )
        self.assertEqual( node05.num_terms,     0   )
        self.assertEqual( node05.height,        0   )
        self.assertEqual( node05.node_id,       8   )

        node06 = node05.children_map['( t3 t4 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t3 t4 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )

        node07 = node05.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node07.ast_node_type, '?' )
        self.assertEqual( node07.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node07.children_map,  {}   )
        self.assertEqual( node07.num_terms,     0    )
        self.assertEqual( node07.height,        0    )
        self.assertEqual( node07.node_id ,      7    )      


    # ?   e
    def test_union_two_ASTs_0081( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'])
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_union_node(['e'])

        node04 = forrest01.union_two_ASTs( node02, node03 )
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | e )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['e']
 
        self.assertEqual( node05.ast_node_type, 'e' )
        self.assertEqual( node05.regex,         'e' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )


    # ?   t1
    def test_union_two_ASTs_0082( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_union_node(['t1'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node05.ast_node_type, '?' )
        self.assertEqual( node05.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )

        node06 = node04.children_map['t1']
 
        self.assertEqual( node06.ast_node_type, 't1' )
        self.assertEqual( node06.regex,         't1' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )


    # ?   t2
    def test_union_two_ASTs_0083( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_union_node(['t2'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node05.ast_node_type, '?' )
        self.assertEqual( node05.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )

        node06 = node04.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      4    )


    # ?   n1
    def test_union_two_ASTs_0084( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_union_node(['n1'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | n1 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n1']
 
        self.assertEqual( node05.ast_node_type, 'n1' )
        self.assertEqual( node05.regex,         'n1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )


    # ?   n2
    def test_union_two_ASTs_0085( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_union_node(['n2'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | n2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       5   )

        node05 = node04.children_map['n2']
 
        self.assertEqual( node05.ast_node_type, 'n2' )
        self.assertEqual( node05.regex,         'n2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )


    # ?   u
    def test_union_two_ASTs_0086( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_union_node(['t1', 't2'])

        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t1 | t2 )' )
        self.assertEqual( len(node04.children_map), 3 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t1']
 
        self.assertEqual( node05.ast_node_type, 't1' )
        self.assertEqual( node05.regex,         't1' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      5    )

        node06 = node04.children_map['t2']
 
        self.assertEqual( node06.ast_node_type, 't2' )
        self.assertEqual( node06.regex,         't2' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      6    )


        node07 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node07.ast_node_type, '?' )
        self.assertEqual( node07.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node07.children_map,  {}   )
        self.assertEqual( node07.num_terms,     0    )
        self.assertEqual( node07.height,        0    )
        self.assertEqual( node07.node_id ,      3    )


    # ?   s
    def test_union_two_ASTs_0087( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )


        node04 = forrest01.union_two_ASTs(node02, node03)
 
        self.assertEqual( node04.ast_node_type, 'u' )
        self.assertEqual( node04.regex,         '( ( t1 t2 ) ? | t1 t2 )' )
        self.assertEqual( len(node04.children_map), 2 )
        self.assertEqual( node04.num_terms,     0   )
        self.assertEqual( node04.height,        0   )
        self.assertEqual( node04.node_id,       7   )

        node05 = node04.children_map['t1 t2']
 
        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         't1 t2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      4    )

        node06 = node04.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )      


    # ?   *
    def test_union_two_ASTs_0078( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = forrest01.repeat_AST(node03)

        node05 = forrest01.union_two_ASTs(node02, node04)

        self.assertEqual( node05.ast_node_type, 'u' )
        self.assertEqual( node05.regex,         '( ( t1 t2 ) * | ( t1 t2 ) ? )' )
        self.assertEqual( len(node05.children_map), 2 )
        self.assertEqual( node05.num_terms,     0   )
        self.assertEqual( node05.height,        0   )
        self.assertEqual( node05.node_id,       8   )

        node06 = node05.children_map['( t1 t2 ) *']
 
        self.assertEqual( node06.ast_node_type, '*' )
        self.assertEqual( node06.regex,         '( t1 t2 ) *' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      7    )

        node07 = node05.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node07.ast_node_type, '?' )
        self.assertEqual( node07.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node07.children_map,  {}   )
        self.assertEqual( node07.num_terms,     0    )
        self.assertEqual( node07.height,        0    )
        self.assertEqual( node07.node_id ,      3    )      


    # ?  ?
    def test_union_two_ASTs_0079( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t3', 't4'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = self.add_question_node( forrest01, node03 )

        node05 = forrest01.union_two_ASTs(node02, node04)
 
        self.assertEqual( node05.ast_node_type, 'u' )
        self.assertEqual( node05.regex,         '( ( t1 t2 ) ? | ( t3 t4 ) ? )' )
        self.assertEqual( len(node05.children_map), 2 )
        self.assertEqual( node05.num_terms,     0   )
        self.assertEqual( node05.height,        0   )
        self.assertEqual( node05.node_id,       8   )

        node06 = node05.children_map['( t3 t4 ) ?']
 
        self.assertEqual( node06.ast_node_type, '?' )
        self.assertEqual( node06.regex,         '( t3 t4 ) ?' )
        self.assertEqual( node06.children_map,  {}   )
        self.assertEqual( node06.num_terms,     0    )
        self.assertEqual( node06.height,        0    )
        self.assertEqual( node06.node_id ,      3    )

        node07 = node05.children_map['( t1 t2 ) ?']
 
        self.assertEqual( node07.ast_node_type, '?' )
        self.assertEqual( node07.regex,         '( t1 t2 ) ?' )
        self.assertEqual( node07.children_map,  {}   )
        self.assertEqual( node07.num_terms,     0    )
        self.assertEqual( node07.height,        0    )
        self.assertEqual( node07.node_id ,      7    )      


    #   e    e
    def test_concat_two_ASTs_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = forrest01.create_initial_node('e')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 'e' )
        self.assertEqual( node03.regex,         'e' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       1    )


    #   e    t1
    def test_concat_two_ASTs_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = forrest01.create_initial_node('t1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 't1' )
        self.assertEqual( node03.regex,         't1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       1    )


    #   e    t2
    def test_concat_two_ASTs_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = forrest01.create_initial_node('t2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 't2' )
        self.assertEqual( node03.regex,         't2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       1    )


    #   e    n1
    def test_concat_two_ASTs_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = forrest01.create_initial_node('n1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 'n1' )
        self.assertEqual( node03.regex,         'n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       1    )


    #   e    n2
    def test_concat_two_ASTs_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = forrest01.create_initial_node('n2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 'n2' )
        self.assertEqual( node03.regex,         'n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       1    )


    #   e    u
    def test_concat_two_ASTs_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  2  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       1    )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      2    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      3    )


    #   e    s
    def test_concat_two_ASTs_0007( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       1    )


    #   e    *
    def test_concat_two_ASTs_0008( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, '*' )
        self.assertEqual( node04.regex,         '( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       4    )


    #   e    ?
    def test_concat_two_ASTs_0009( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, '?' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       4    )


    #   t1    e
    def test_concat_two_ASTs_0011( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = forrest01.create_initial_node('e')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 't1' )
        self.assertEqual( node03.regex,         't1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       0    )


    #   t1    t1
    def test_concat_two_ASTs_0012( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = forrest01.create_initial_node('t1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t1    t2
    def test_concat_two_ASTs_0013( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = forrest01.create_initial_node('t2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t1    n1
    def test_concat_two_ASTs_0014( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = forrest01.create_initial_node('n1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t1    n2
    def test_concat_two_ASTs_0015( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = forrest01.create_initial_node('n2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t1    u
    def test_concat_two_ASTs_0016( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 ( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   t1    s
    def test_concat_two_ASTs_0017( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   t1    *
    def test_concat_two_ASTs_0018( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't1 ( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   t1    ?
    def test_concat_two_ASTs_0019( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't1 ( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   t2    e
    def test_concat_two_ASTs_0021( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = forrest01.create_initial_node('e')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 't2' )
        self.assertEqual( node03.regex,         't2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       0    )


    #   t2    t1
    def test_concat_two_ASTs_0022( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = forrest01.create_initial_node('t1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't2 t1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t2    t2
    def test_concat_two_ASTs_0023( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = forrest01.create_initial_node('t2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't2 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t2    n1
    def test_concat_two_ASTs_0024( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = forrest01.create_initial_node('n1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't2 n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t2    n2
    def test_concat_two_ASTs_0025( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = forrest01.create_initial_node('n2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't2 n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   t2    u
    def test_concat_two_ASTs_0026( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't2 ( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   t2    s
    def test_concat_two_ASTs_0027( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't2 t1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   t2    *
    def test_concat_two_ASTs_0028( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't2 ( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   t2    ?
    def test_concat_two_ASTs_0029( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t2')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't2 ( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   n1    e
    def test_concat_two_ASTs_0031( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = forrest01.create_initial_node('e')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 'n1' )
        self.assertEqual( node03.regex,         'n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       0    )


    #   n1    t1
    def test_concat_two_ASTs_0032( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = forrest01.create_initial_node('t1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n1 t1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n1    t2
    def test_concat_two_ASTs_0033( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = forrest01.create_initial_node('t2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n1    n1
    def test_concat_two_ASTs_0034( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = forrest01.create_initial_node('n1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n1 n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n1    n2
    def test_concat_two_ASTs_0035( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = forrest01.create_initial_node('n2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n1 n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n1    u
    def test_concat_two_ASTs_0036( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n1 ( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   n1    s
    def test_concat_two_ASTs_0037( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n1 t1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   n1    *
    def test_concat_two_ASTs_0038( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         'n1 ( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   n1    ?
    def test_concat_two_ASTs_0039( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         'n1 ( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )



    #   n2    e
    def test_concat_two_ASTs_0041( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = forrest01.create_initial_node('e')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 'n2' )
        self.assertEqual( node03.regex,         'n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       0    )


    #   n2    t1
    def test_concat_two_ASTs_0042( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = forrest01.create_initial_node('t1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n2 t1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n2    t2
    def test_concat_two_ASTs_0043( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = forrest01.create_initial_node('t2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n2 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n2    n1
    def test_concat_two_ASTs_0044( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = forrest01.create_initial_node('n1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n2 n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n2    n2
    def test_concat_two_ASTs_0045( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = forrest01.create_initial_node('n2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n2 n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       2    )


    #   n2    u
    def test_concat_two_ASTs_0046( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n2 ( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   n2    s
    def test_concat_two_ASTs_0047( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         'n2 t1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   n2    *
    def test_concat_two_ASTs_0048( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         'n2 ( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   n2    ?
    def test_concat_two_ASTs_0049( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n2')

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         'n2 ( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   u   e
    def test_concat_two_ASTs_0051( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_node('e')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 'u' )
        self.assertEqual( node03.regex,         '( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  2  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       0    )

        node04 = node03.children_map['t1']
 
        self.assertEqual( node04.ast_node_type, 't1' )
        self.assertEqual( node04.regex,         't1' )
        self.assertEqual( node04.children_map,  {}   )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id ,      1    )

        node05 = node03.children_map['t2']
 
        self.assertEqual( node05.ast_node_type, 't2' )
        self.assertEqual( node05.regex,         't2' )
        self.assertEqual( node05.children_map,  {}   )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id ,      2    )


    #   u    t1
    def test_concat_two_ASTs_0052( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_node('t1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         '( t1 | t2 ) t1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   u    t2
    def test_concat_two_ASTs_0053( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_node('t2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         '( t1 | t2 ) t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   u   n1
    def test_concat_two_ASTs_0054( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_node('n1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         '( t1 | t2 ) n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   u    n2
    def test_concat_two_ASTs_0055( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_node('n2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         '( t1 | t2 ) n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   u    u
    def test_concat_two_ASTs_0056( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         '( t1 | t2 ) ( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       6    )


    #   u    s
    def test_concat_two_ASTs_0057( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         '( t1 | t2 ) t1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       6    )


    #   u    *
    def test_concat_two_ASTs_0058( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 | t2 ) ( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   u    ?
    def test_concat_two_ASTs_0059( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node(['t1', 't2'])

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 | t2 ) ( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   s   e
    def test_concat_two_ASTs_0061( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_node('e')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       0    )


    #   s    t1
    def test_concat_two_ASTs_0062( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_node('t1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2 t1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   s    t2
    def test_concat_two_ASTs_0063( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_node('t2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   s   n1
    def test_concat_two_ASTs_0064( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_node('n1')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2 n1' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   s    n2
    def test_concat_two_ASTs_0065( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_node('n2')

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2 n2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       4    )


    #   s    u
    def test_concat_two_ASTs_0066( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = forrest01.create_initial_union_node(['t1', 't2'])

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2 ( t1 | t2 )' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       6    )


    #   s    s
    def test_concat_two_ASTs_0067( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2 t1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       6    )


    #   s    *
    def test_concat_two_ASTs_0068( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = forrest01.repeat_AST(node02)

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't1 t2 ( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   s    ?
    def test_concat_two_ASTs_0069( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node02 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node03 = self.add_question_node( forrest01, node02 )

        node04 = forrest01.concat_two_ASTs(node01, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         't1 t2 ( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   *   e
    def test_concat_two_ASTs_0071( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_node('e')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, '*' )
        self.assertEqual( node04.regex,         '( t1 t2 ) *' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       3    )


    #   *    t1
    def test_concat_two_ASTs_0072( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_node('t1')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) * t1' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   *    t2
    def test_concat_two_ASTs_0073( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_node('t2')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) * t2' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   *   n1
    def test_concat_two_ASTs_0074( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_node('n1')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) * n1' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   *    n2
    def test_concat_two_ASTs_0075( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_node('n2')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) * n2' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   *    u
    def test_concat_two_ASTs_0076( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = forrest01.create_initial_union_node(['t1', 't2'])

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) * ( t1 | t2 )' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   *    s
    def test_concat_two_ASTs_0077( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node04 = forrest01.concat_two_ASTs( node02, node03 )

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) * t1 t2' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   *    *
    def test_concat_two_ASTs_0078( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = forrest01.repeat_AST(node03)

        node05 = forrest01.concat_two_ASTs(node02, node04)

        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         '( t1 t2 ) * ( t1 t2 ) *' )
        self.assertEqual( len(node05.children_map),  0  )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id,       8    )


    #   *    ?
    def test_concat_two_ASTs_0079( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = forrest01.repeat_AST(node01)

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = self.add_question_node( forrest01, node03 )

        node05 = forrest01.concat_two_ASTs(node02, node04)

        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         '( t1 t2 ) * ( t1 t2 ) ?' )
        self.assertEqual( len(node05.children_map),  0  )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id,       8    )


    #   ?   e
    def test_concat_two_ASTs_0081( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_node('e')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, '?' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ?' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       3    )


    #   ?    t1
    def test_concat_two_ASTs_0082( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_node('t1')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ? t1' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   ?    t2
    def test_concat_two_ASTs_0083( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_node('t2')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ? t2' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   ?   n1
    def test_concat_two_ASTs_0084( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_node('n1')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ? n1' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   ?    n2
    def test_concat_two_ASTs_0085( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_node('n2')

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ? n2' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       5    )


    #   ?    u
    def test_concat_two_ASTs_0086( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = forrest01.create_initial_union_node(['t1', 't2'])

        node04 = forrest01.concat_two_ASTs(node02, node03)

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ? ( t1 | t2 )' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   ?    s
    def test_concat_two_ASTs_0087( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )

        node04 = forrest01.concat_two_ASTs( node02, node03 )

        self.assertEqual( node04.ast_node_type, 's' )
        self.assertEqual( node04.regex,         '( t1 t2 ) ? t1 t2' )
        self.assertEqual( len(node04.children_map),  0  )
        self.assertEqual( node04.num_terms,     0    )
        self.assertEqual( node04.height,        0    )
        self.assertEqual( node04.node_id,       7    )


    #   ?    *
    def test_concat_two_ASTs_0088( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = forrest01.repeat_AST(node03)

        node05 = forrest01.concat_two_ASTs(node02, node04)

        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         '( t1 t2 ) ? ( t1 t2 ) *' )
        self.assertEqual( len(node05.children_map),  0  )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id,       8    )


    #   ?    ?
    def test_concat_two_ASTs_0089( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node02 = self.add_question_node( forrest01, node01 )

        node03 = self.create_initial_serial_node( forrest01, ['t1', 't2'] )
        node04 = self.add_question_node( forrest01, node03 )

        node05 = forrest01.concat_two_ASTs(node02, node04)

        self.assertEqual( node05.ast_node_type, 's' )
        self.assertEqual( node05.regex,         '( t1 t2 ) ? ( t1 t2 ) ?' )
        self.assertEqual( len(node05.children_map),  0  )
        self.assertEqual( node05.num_terms,     0    )
        self.assertEqual( node05.height,        0    )
        self.assertEqual( node05.node_id,       8    )


    #   ?    ?
    def test_concat_two_ASTs_0089( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 'e', 't2'] )

        node02 = self.create_initial_serial_node( forrest01, ['t1', 'e', 't2'] )

        node03 = forrest01.concat_two_ASTs(node01, node02)

        self.assertEqual( node03.ast_node_type, 's' )
        self.assertEqual( node03.regex,         't1 t2 t1 t2' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       8    )



    # 'e'
    def test_repeat_AST_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('e')
        node02 = forrest01.repeat_AST( node01 )

        self.assertEqual( node02.ast_node_type, 'e' )
        self.assertEqual( node02.regex,         'e' )
        self.assertEqual( len(node02.children_map),  0  )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id,       0    )


    # 't1'
    def test_repeat_AST_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('t1')
        node02 = forrest01.repeat_AST( node01 )

        self.assertEqual( node02.ast_node_type, '*' )
        self.assertEqual( node02.regex,         't1 *' )
        self.assertEqual( len(node02.children_map),  0  )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id,       1    )


    # 'n1'
    def test_repeat_AST_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_node('n1')
        node02 = forrest01.repeat_AST( node01 )

        self.assertEqual( node02.ast_node_type, '*' )
        self.assertEqual( node02.regex,         'n1 *' )
        self.assertEqual( len(node02.children_map),  0  )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id,       1    )

    # 'u'
    def test_repeat_AST_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node( ['t1', 't2' ] )
        node02 = forrest01.repeat_AST( node01 )

        self.assertEqual( node02.ast_node_type, '*' )
        self.assertEqual( node02.regex,         '( t1 | t2 ) *' )
        self.assertEqual( len(node02.children_map),  0  )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id,       3    )


    # 's'
    def test_repeat_AST_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2' ] )
        node02 = forrest01.repeat_AST( node01 )

        self.assertEqual( node02.ast_node_type, '*' )
        self.assertEqual( node02.regex,         '( t1 t2 ) *' )
        self.assertEqual( len(node02.children_map),  0  )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id,       3    )


    # '*'
    def test_repeat_AST_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2' ] )
        node02 = forrest01.repeat_AST( node01 )
        node03 = forrest01.repeat_AST( node02 )

        self.assertEqual( node03.ast_node_type, '*' )
        self.assertEqual( node03.regex,         '( t1 t2 ) *' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       3    )


    # '?'
    def test_repeat_AST_0007( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = self.create_initial_serial_node( forrest01, ['t1', 't2' ] )
        node02 = self.add_question_node( forrest01, node01 )
        node03 = forrest01.repeat_AST( node02 )

        self.assertEqual( node03.ast_node_type, '*' )
        self.assertEqual( node03.regex,         '( t1 t2 ) *' )
        self.assertEqual( len(node03.children_map),  0  )
        self.assertEqual( node03.num_terms,     0    )
        self.assertEqual( node03.height,        0    )
        self.assertEqual( node03.node_id,       3    )


    # epsilon in union
    def test_repeat_AST_0008( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node([ 't1', 't2', 'e' ])
        node02 = forrest01.repeat_AST( node01 )

        self.assertEqual( node02.ast_node_type, '*' )
        self.assertEqual( node02.regex,         '( t1 | t2 ) *' )
        self.assertEqual( len(node02.children_map),  0  )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id,       4    )


    # epsilon in union leaves one node.
    def test_repeat_AST_0008( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()

        node01 = forrest01.create_initial_union_node([ 't1', 'e' ])
        node02 = forrest01.repeat_AST( node01 )

        self.assertEqual( node02.ast_node_type, '*' )
        self.assertEqual( node02.regex,         't1 *' )
        self.assertEqual( len(node02.children_map),  0  )
        self.assertEqual( node02.num_terms,     0    )
        self.assertEqual( node02.height,        0    )
        self.assertEqual( node02.node_id,       3    )


    # (e) => none
    def test_remove_AST_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            E_1
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        forrest01.remove_AST( node01 )
        self.assertEqual( forrest01.num_nodes(),   0    )


    # (t) => none
    def test_remove_AST_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            T1_1
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        forrest01.remove_AST( node01 )
        self.assertEqual( forrest01.num_nodes(),   0    )

    # (n) => none
    def test_remove_AST_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            N1_1
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        forrest01.remove_AST( node01 )
        self.assertEqual( forrest01.num_nodes(),   0    )

    # (u) => none
    def test_remove_AST_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_1:T2_2 T3_3
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        forrest01.remove_AST( node01 )
        self.assertEqual( forrest01.num_nodes(),   0    )

    # (s) => none
    def test_remove_AST_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_1:T3_2 T3_3
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        forrest01.remove_AST( node01 )
        self.assertEqual( forrest01.num_nodes(),   0    )

    # (*) => none
    def test_remove_AST_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            *_1:T2_2
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        forrest01.remove_AST( node01 )
        self.assertEqual( forrest01.num_nodes(),   0    )

    # (?) => none
    def test_remove_AST_0007( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            ?_1:T2_2
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        forrest01.remove_AST( node01 )
        self.assertEqual( forrest01.num_nodes(),   0    )

    # |_1:(T2_2) T3_3
    def test_remove_AST_0008( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_1:T2_2 T3_3
        '''
        spec_expected = '''
            |_1:T3_3
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node02  = self.helper.get_node(forrest01, 2)
        forrest01.remove_AST( node02 )
        spec03 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec03, spec_expected ), True )


    # |_1:T2_2 (T3_3)
    def test_remove_AST_0009( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_1:T2_2 T3_3
        '''

        spec_expected = '''
            |_1:T2_2
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node03  = self.helper.get_node(forrest01, 3)
        forrest01.remove_AST( node03 )
        spec03 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec03, spec_expected ), True )


    # S_1:(T2_2) T3_3
    def test_remove_AST_0010( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_1:T2_2 T2_3
        '''
        spec_expected = '''
            S_1:T2_3
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 2)
        forrest01.remove_AST( node01 )
        spec03 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec03, spec_expected ), True )


    # S_1:T2_2 (T3_3)
    def test_remove_AST_0011( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_1:T2_2 T3_3
        '''
        spec_expected = '''
            S_1:T2_2
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 3)
        forrest01.remove_AST( node01 )
        spec03 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec03, spec_expected ), True )


    # *_1:(T2_2)
    def test_remove_AST_0012( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            *_1:T2_2
        '''
        spec_expected = '''
            *_1
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 2)
        forrest01.remove_AST( node01 )
        spec03 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec03, spec_expected ), True )


    # ?_1:(T2_2)
    def test_remove_AST_0013( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            ?_1:T2_2
        '''
        spec_expected = '''
            ?_1
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 2)
        forrest01.remove_AST( node01 )
        spec03 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec03, spec_expected ), True )


    # General pattern
    def test_remove_AST_0014( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_1:T2_2 S_3 T4_4 E_5
            S_3:T6_6 |_7 T8_8
            |_7:T9_9 T10_10
        '''
        spec_expected = '''
            |_1:T2_2 T4_4 E_5
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 3)
        forrest01.remove_AST( node01 )
        spec03 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec03, spec_expected ), True )


    def test_clone_AST_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            |_10:T1_11 S_12 T3_18 E_19
            S_12:T5_13 |_14 T7_17
            |_14:T8_15 T9_16
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = forrest01.clone_AST( root01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T1_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            T1_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 1)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            S_10:T5_11 |_12 T7_15
            |_12:T8_13 T9_14
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 2)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            T3_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 3)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            E_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 4)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0006( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            T5_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 5)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0007( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            |_10:T8_11 T9_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 6)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0008( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            T7_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 7)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0009( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            T8_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 8)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0010( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            |_0:T1_1 S_2 T3_3 E_4
            S_2:T5_5 |_6 T7_7
            |_6:T8_8 T9_9
        '''

        spec_expected = '''
            T9_10
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        node01  = self.helper.get_node(forrest01, 9)
        root02  = forrest01.clone_AST( node01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_clone_AST_0011( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            E_0
        '''

        spec_expected = '''
            E_1
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        root02  = forrest01.clone_AST( root01 )
        spec02 = self.helper.display_tree( root02 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_remove_epsilons_from_unions_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:T4_4 T5_5 T6_6
        '''

        spec_expected = '''
            S_0:T1_1 |_2 T3_3
            |_2:T4_4 T5_5 T6_6
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.remove_epsilons_from_unions( root01 )
        spec02 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_remove_epsilons_from_unions_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:T4_4 E_5 T6_6
        '''

        spec_expected = '''
            S_0:T1_1 ?_2 T3_3
            ?_2:|_7
            |_7:T4_4 T6_6
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.remove_epsilons_from_unions( root01 )
        spec02 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_remove_epsilons_from_unions_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:T4_4 E_5
        '''

        spec_expected = '''
            S_0:T1_1 ?_2 T3_3
            ?_2:T4_6
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.remove_epsilons_from_unions( root01 )
        spec02 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_remove_epsilons_from_unions_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:S_4 E_5 T6_6
            S_4:T7_7 T8_8 T9_9
        '''

        spec_expected = '''
            S_0:T1_1 ?_2 T3_3
            ?_2:|_10
            |_10:S_4 T6_6
            S_4:T7_7 T8_8 T9_9

        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.remove_epsilons_from_unions( root01 )
        spec02 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_remove_epsilons_from_unions_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:S_4 E_5
            S_4:T6_6 T7_7 T8_8
        '''

        spec_expected = '''
            S_0:T1_1 ?_2 T3_3
            ?_2:S_9
            S_9:T6_6 T7_7 T8_8

        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.remove_epsilons_from_unions( root01 )
        spec02 = self.helper.display_tree( root01 )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_create_tree_root_for_reduction_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:S_4 T5_5 T6_6
            S_4:T7_7 T8_8 T9_9
        '''

        spec_expected = '''
            R_10:S_0
            S_0:T1_1 |_2 T3_3
            |_2:S_4 T5_5 T6_6
            S_4:T7_7 T8_8 T9_9
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        spec02 = self.helper.display_tree( forrest01.root )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_prepare_for_reduction_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:S_4 T5_5 T6_6
            S_4:T7_7 T8_8 T9_9
        '''

        spec_expected = '''
            R_10:S_0
            S_0:T1_1 |_2 T3_3
            |_2:S_4 T5_5 T6_6
            S_4:T7_7 T8_8 T9_9
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()
        spec02 = self.helper.display_tree( forrest01.root )
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )

        node10 = self.helper.get_node( forrest01, 10 )
        node00 = self.helper.get_node( forrest01,  0 )
        node01 = self.helper.get_node( forrest01,  1 )
        node02 = self.helper.get_node( forrest01,  2 )
        node03 = self.helper.get_node( forrest01,  3 )
        node04 = self.helper.get_node( forrest01,  4 )
        node05 = self.helper.get_node( forrest01,  5 )
        node06 = self.helper.get_node( forrest01,  6 )
        node07 = self.helper.get_node( forrest01,  7 )
        node08 = self.helper.get_node( forrest01,  8 )
        node09 = self.helper.get_node( forrest01,  9 )

        self.assertEqual( node10.regex,     'r' )
        self.assertEqual( node10.num_terms,   7 )
        self.assertEqual( node10.height,      5 )
        self.assertEqual( len(node10.children_map),      1 )
        self.assertEqual( node10.children_map['n0'], node00 )

        self.assertEqual( node09.regex,      't9' )
        self.assertEqual( node09.num_terms,   1 )
        self.assertEqual( node09.height,      1 )
        self.assertEqual( len(node09.children_map),      0 )

        self.assertEqual( node08.regex,      't8' )
        self.assertEqual( node08.num_terms,   1 )
        self.assertEqual( node08.height,      1 )
        self.assertEqual( len(node08.children_map),      0 )

        self.assertEqual( node07.regex,      't7' )
        self.assertEqual( node07.num_terms,   1 )
        self.assertEqual( node07.height,      1 )
        self.assertEqual( len(node07.children_map),      0 )

        self.assertEqual( node06.regex,      't6' )
        self.assertEqual( node06.num_terms,   1 )
        self.assertEqual( node06.height,      1 )
        self.assertEqual( len(node06.children_map),      0 )

        self.assertEqual( node05.regex,      't5' )
        self.assertEqual( node05.num_terms,   1 )
        self.assertEqual( node05.height,      1 )
        self.assertEqual( len(node05.children_map),      0 )

        self.assertEqual( node04.regex,      't7 t8 t9' )
        self.assertEqual( node04.num_terms,   3 )
        self.assertEqual( node04.height,      2 )
        self.assertEqual( len(node04.children_map),      0 )

        self.assertEqual( node03.regex,      't3' )
        self.assertEqual( node03.num_terms,   1 )
        self.assertEqual( node03.height,      1 )
        self.assertEqual( len(node04.children_map),      0 )

        self.assertEqual( node02.regex,      '( t7 t8 t9 | t5 | t6 )' )
        self.assertEqual( node02.num_terms,   5 )
        self.assertEqual( node02.height,      3 )
        self.assertEqual( len(node02.children_map),      3 )
        self.assertEqual( node02.children_map['t7 t8 t9'],  node04 )
        self.assertEqual( node02.children_map['t5'],        node05 )
        self.assertEqual( node02.children_map['t6'],        node06 )

        self.assertEqual( node01.regex,      't1' )
        self.assertEqual( node01.num_terms,   1 )
        self.assertEqual( node01.height,      1 )
        self.assertEqual( len(node01.children_map),      0 )

        self.assertEqual( node00.regex,      't1 ( t7 t8 t9 | t5 | t6 ) t3' )
        self.assertEqual( node00.num_terms,   7 )
        self.assertEqual( node00.height,      4 )
        self.assertEqual( len(node00.children_map),      0 )


    def test_find_nonterminals_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 |_2 T3_3
            |_2:S_4 N5_5 T6_6
            S_4:T7_7 T8_8 N9_9
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        list01 = forrest01.find_nonterminals()

        self.assertEqual( len(list01), 3 )
        self.assertEqual( 'n0' in list01 , True )
        self.assertEqual( 'n5' in list01 , True )
        self.assertEqual( 'n9' in list01 , True )


    def test_isolate_balanced_children_0001( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5
            |_3:S_6 N7_7 T8_8
            S_6:T9_9 T10_10 N11_11
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        pos_begin = 0
        pos_end   = 4
        list01 = forrest01.isolate_balanced_children( node01, pos_begin, pos_end )

        spec02 = self.helper.display_tree( forrest01.root )

#        print (spec02)

        spec_expected = '''
            R_12:S_0
            S_0:T2_2 |_3 T4_4
            |_3:S_6 N7_7 T8_8
            S_6:T9_9 T10_10 N11_11
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )

        self.assertEqual( node01.balanced_out_pre,  't1' )
        self.assertEqual( node01.balanced_out_post, 't5' )


    def test_isolate_balanced_children_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        pos_begin = 3
        pos_end   = 5
        list01 = forrest01.isolate_balanced_children( node01, pos_begin, pos_end )

        spec02 = self.helper.display_tree( forrest01.root )

        node05 = self.helper.get_node( forrest01,  5 )

#        print (spec02)

        spec_expected = '''
            R_13:S_0
            S_0:T1_1 T2_2 |_3 T5_5
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )
        self.assertEqual( node05.balanced_out_pre,  't4' )
        self.assertEqual( node05.balanced_out_post, 't6' )


    def test_isolate_balanced_children_0002( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        pos_begin = 3
        pos_end   = 5
        list01 = forrest01.isolate_balanced_children( node01, pos_begin, pos_end )

        spec02 = self.helper.display_tree( forrest01.root )

        node05 = self.helper.get_node( forrest01,  5 )

#        print (spec02)

        spec_expected = '''
            R_13:S_0
            S_0:T1_1 T2_2 |_3 T5_5
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )
        self.assertEqual( node05.balanced_out_pre,  't4' )
        self.assertEqual( node05.balanced_out_post, 't6' )


    def test_isolate_balanced_children_0003( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        pos_begin = 1
        pos_end   = 4
        list01 = forrest01.isolate_balanced_children( node01, pos_begin, pos_end )

        spec02 = self.helper.display_tree( forrest01.root )

        node14 = self.helper.get_node( forrest01,  14 )

#        print (spec02)

        spec_expected = '''
            R_13:S_0
            S_0:T1_1 S_14 T6_6
            S_14:|_3 T4_4
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )
        self.assertEqual( node14.balanced_out_pre,  't2' )
        self.assertEqual( node14.balanced_out_post, 't5' )


    def test_isolate_balanced_children_0004( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        pos_begin = 1
        pos_end   = 3
        list01 = forrest01.isolate_balanced_children( node01, pos_begin, pos_end )

        spec02 = self.helper.display_tree( forrest01.root )

        node14 = self.helper.get_node( forrest01,  14 )

#        print (spec02)

        spec_expected = '''
            R_13:S_0
            S_0:T1_1 S_14 T5_5 T6_6
            S_14:|_3
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )
        self.assertEqual( node14.balanced_out_pre,  't2' )
        self.assertEqual( node14.balanced_out_post, 't4' )


    def test_isolate_balanced_children_0005( self ):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        pos_begin = 3
        pos_end   = 5

        node05 = self.helper.get_node( forrest01,  5 )
        node05.balanced_out_pre = 't100'
        node05.balanced_out_post = 't200'

        list01 = forrest01.isolate_balanced_children( node01, pos_begin, pos_end )

        spec02 = self.helper.display_tree( forrest01.root )

        node14 = self.helper.get_node( forrest01,  14 )

#        print (spec02)

        spec_expected = '''
            R_13:S_0
            S_0:T1_1 T2_2 |_3 S_14
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
            S_14:T5_5
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )
        self.assertEqual( node14.balanced_out_pre,  't4' )
        self.assertEqual( node14.balanced_out_post, 't6' )


    def test_visit_and_balance_trees_for_out_tokens_0001( self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )

        list01 = forrest01.visit_and_balance_trees_for_out_tokens( node01, {} )

        spec02 = self.helper.display_tree( forrest01.root )

        node14 = self.helper.get_node( forrest01,  14 )

#        print (spec02)

        spec_expected = '''
            R_13:S_0
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )


    def test_visit_and_balance_trees_for_out_tokens_0002( self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        balanced_dic =  {}
        balanced_dic['t1'] = 't6'

        list01 = forrest01.visit_and_balance_trees_for_out_tokens( node01, balanced_dic )

        spec02 = self.helper.display_tree( forrest01.root )

        node14 = self.helper.get_node( forrest01,  14 )

#        print (spec02)

        spec_expected = '''
            R_13:S_0
            S_0:T2_2 |_3 T4_4 T5_5
            |_3:S_7 N8_8 T9_9
            S_7:T10_10 T11_11 N12_12
        '''
        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )

        self.assertEqual( node01.balanced_out_pre,  't1' )
        self.assertEqual( node01.balanced_out_post, 't6' )


    def test_visit_and_balance_trees_for_out_tokens_0003( self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 T3_3 T4_4 T5_5 T6_6 T7_7
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        balanced_dic =  {}
        balanced_dic['t1'] = 't7'
        balanced_dic['t2'] = 't6'
        balanced_dic['t3'] = 't5'

        list01 = forrest01.visit_and_balance_trees_for_out_tokens( node01, balanced_dic )

        spec02 = self.helper.display_tree( forrest01.root )

        node14 = self.helper.get_node( forrest01,  14 )

#        print (spec02)

        spec_expected = '''
            R_8:S_0
            S_0:S_9
            S_9:T4_4
        '''
        node04 = self.helper.get_node( forrest01,  4 )
        node09 = self.helper.get_node( forrest01,  9 )

        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )

        self.assertEqual( node01.balanced_out_pre,  't1' )
        self.assertEqual( node01.balanced_out_post, 't7' )

        self.assertEqual( node09.balanced_out_pre,  't2' )
        self.assertEqual( node09.balanced_out_post, 't6' )

        self.assertEqual( node04.balanced_out_pre,  't3' )
        self.assertEqual( node04.balanced_out_post, 't5' )


    def test_visit_and_balance_trees_for_out_tokens_0004( self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 T3_3 T4_4 T5_5 T6_6 T7_7
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        balanced_dic =  {}
        balanced_dic['t1'] = 't4'
        balanced_dic['t5'] = 't7'

        list01 = forrest01.visit_and_balance_trees_for_out_tokens( node01, balanced_dic )

        spec02 = self.helper.display_tree( forrest01.root )

        node14 = self.helper.get_node( forrest01,  14 )

#        print (spec02)

        spec_expected = '''
            R_8:S_0
            S_0:S_9 T6_6
            S_9:T2_2 T3_3
        '''
        node09 = self.helper.get_node( forrest01,  9 )
        node06 = self.helper.get_node( forrest01,  6 )

        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )

        self.assertEqual( node01.balanced_out_pre,  '' )
        self.assertEqual( node01.balanced_out_post, '' )

        self.assertEqual( node09.balanced_out_pre,  't1' )
        self.assertEqual( node09.balanced_out_post, 't4' )

        self.assertEqual( node06.balanced_out_pre,  't5' )
        self.assertEqual( node06.balanced_out_post, 't7' )



    def test_balance_trees_for_out_tokens_0001( self):

        forrest01 = nlpregex.regular_language.sse_forrest.sseASForrest()             
        spec01 = '''
            S_0:T1_1 T2_2 |_3 T4_4 T5_5 T6_6 T7_7
            |_3:S_8 N9_9 T10_10
            S_8:T11_11 T12_12 N13_13 T14_14
        '''

        root01  = self.helper.construct_ast_from_spec( forrest01, spec01 )
        forrest01.create_tree_root_for_reduction( root01 )
        forrest01.prepare_for_reduction()

        node01 = self.helper.get_node( forrest01,  0 )
        balanced_list =  [ ('t11', 't14'), ('t1', 't4'), ('t5', 't7') ]

        list01 = forrest01.balance_trees_for_out_tokens( balanced_list )

        spec02 = self.helper.display_tree( forrest01.root )

#        print (spec02)

        spec_expected = '''
            R_15:S_0
            S_0:S_16 T6_6
            S_16:T2_2 |_3
            |_3:S_8 N9_9 T10_10
            S_8:T12_12 N13_13
        '''

        node08 = self.helper.get_node( forrest01,   8 )
        node16 = self.helper.get_node( forrest01,  16 )
        node06 = self.helper.get_node( forrest01,   6 )

        self.assertEqual( self.helper.compare_specs( spec02, spec_expected ), True )

        self.assertEqual( node08.balanced_out_pre,  't11' )
        self.assertEqual( node08.balanced_out_post, 't14' )

        self.assertEqual( node16.balanced_out_pre,  't1' )
        self.assertEqual( node16.balanced_out_post, 't4' )

        self.assertEqual( node06.balanced_out_pre,  't5' )
        self.assertEqual( node06.balanced_out_post, 't7' )








if __name__ == '__main__':
    unittest.main()
