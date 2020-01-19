#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for BaseNode."""

import unittest
import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph


class test_BaseNode ( unittest.TestCase ):


    def test_constructor(self):

        node01 = nlpregex.abs_graph.node.BaseNode()
        self.assertIsNone    ( node01.graph )
        self.assertIsNone    ( node01.graph_delg )
        self.assertIsInstance( node01.in_neighbors_list,         nlpregex.abs_graph.double_link.List )
        self.assertIsInstance( node01.out_neighbors_list,        nlpregex.abs_graph.double_link.List )
        self.assertIsInstance( node01.undirected_neighbors_list, nlpregex.abs_graph.double_link.List )


    def test_add_to_graph(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()

        node01.add_to_graph(graph01)

        self.assertEqual( graph01.num_nodes(), 1)
        self.assertEqual( node01.graph, graph01)
        self.assertEqual( graph01.num_nodes(), 1)


    def test_in_neighbors_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        rtn01 = node01.in_neighbors()
    
        self.assertEqual( len(rtn01), 0      )


    def test_in_neighbors_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        rtn01 = node02.in_neighbors()
    
        self.assertEqual( len(rtn01), 1      )
        self.assertEqual( rtn01[0],   edge01 )


    def test_in_neighbors_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")


        rtn01 = node02.in_neighbors()
    
        self.assertEqual( len(rtn01), 2      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )


    def test_in_neighbors_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "directed")

        rtn01 = node02.in_neighbors()
    
        self.assertEqual( len(rtn01), 3      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )
        self.assertEqual( rtn01[2],   edge03 )


    def test_in_neighbors_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "directed")

        rtn01 = node02.in_neighbors()
    
        self.assertEqual( len(rtn01), 3      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )
        self.assertEqual( rtn01[2],   edge03 )


    def test_in_degree_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertEqual( node01.in_degree(), 0 )


    def test_in_degree_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        self.assertEqual( node02.in_degree(), 1 )


    def test_in_degree_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")

        self.assertEqual( node02.in_degree(), 2 )


    def test_in_degree_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "directed")

        self.assertEqual( node02.in_degree(), 3 )


    def test_in_degree_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "directed")

        rtn01 = node02.in_neighbors()
    
        self.assertEqual( node02.in_degree(), 3 )


    def test_in_neighbor_head_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertIsNone( node01.in_neighbor_head() )


    def test_in_neighbor_head_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        self.assertEqual( node02.in_neighbor_head(), edge01 )


    def test_in_neighbor_head_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")

        self.assertEqual( node02.in_neighbor_head(), edge01 )


    def test_in_neighbor_head_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "directed")

        self.assertEqual( node02.in_neighbor_head(), edge01 )


    def test_in_neighbor_head_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "directed")

        self.assertEqual( node02.in_neighbor_head(), edge01 )


    def test_in_neighbor_tail_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertIsNone( node01.in_neighbor_tail() )


    def test_in_neighbor_tail_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        self.assertEqual( node02.in_neighbor_tail(), edge01 )


    def test_in_neighbor_tail_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")

        self.assertEqual( node02.in_neighbor_tail(), edge02 )


    def test_in_neighbor_tail_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "directed")

        self.assertEqual( node02.in_neighbor_tail(), edge03 )


    def test_in_neighbor_tail_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "directed")

        self.assertEqual( node02.in_neighbor_tail(), edge03 )


    def test_out_neighbors_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        rtn01 = node01.out_neighbors()
    
        self.assertEqual( len(rtn01), 0      )


    def test_out_neighbors_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        rtn01 = node02.out_neighbors()
    
        self.assertEqual( len(rtn01), 1      )
        self.assertEqual( rtn01[0],   edge01 )


    def test_out_neighbors_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")


        rtn01 = node02.out_neighbors()
    
        self.assertEqual( len(rtn01), 2      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )


    def test_out_neighbors_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node04, "directed")

        rtn01 = node02.out_neighbors()
    
        self.assertEqual( len(rtn01), 3      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )
        self.assertEqual( rtn01[2],   edge03 )


    def test_out_neighbors_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node01, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node01, "directed")

        rtn01 = node02.out_neighbors()
    
        self.assertEqual( len(rtn01), 3      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )
        self.assertEqual( rtn01[2],   edge03 )


    def test_out_degree_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertEqual( node01.out_degree(), 0 )


    def test_out_degree_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        self.assertEqual( node02.out_degree(), 1 )


    def test_out_degree_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")

        self.assertEqual( node02.out_degree(), 2 )


    def test_out_degree_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node04, "directed")

        self.assertEqual( node02.out_degree(), 3 )


    def test_out_degree_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node01, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node01, "directed")

        rtn01 = node02.out_neighbors()
    
        self.assertEqual( node02.out_degree(), 3 )


    def test_out_neighbor_head_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertIsNone( node01.out_neighbor_head() )


    def test_out_neighbor_head_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        self.assertEqual( node02.out_neighbor_head(), edge01 )


    def test_out_neighbor_head_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")

        self.assertEqual( node02.out_neighbor_head(), edge01 )


    def test_out_neighbor_head_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node04, "directed")

        self.assertEqual( node02.out_neighbor_head(), edge01 )


    def test_out_neighbor_head_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node01, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node01, "directed")

        self.assertEqual( node02.out_neighbor_head(), edge01 )


    def test_out_neighbor_tail_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertIsNone( node01.out_neighbor_tail() )


    def test_out_neighbor_tail_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        self.assertEqual( node02.out_neighbor_tail(), edge01 )


    def test_out_neighbor_tail_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")

        self.assertEqual( node02.out_neighbor_tail(), edge02 )


    def test_out_neighbor_tail_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node03, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node04, "directed")

        self.assertEqual( node02.out_neighbor_tail(), edge03 )


    def test_out_neighbor_tail_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node02, node01, "directed")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node02, node01, "directed")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node02, node01, "directed")

        self.assertEqual( node02.out_neighbor_tail(), edge03 )


    def test_undirected_neighbors_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        rtn01 = node01.undirected_neighbors()
    
        self.assertEqual( len(rtn01), 0      )


    def test_undirected_neighbors_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        rtn01 = node02.undirected_neighbors()
    
        self.assertEqual( len(rtn01), 1      )
        self.assertEqual( rtn01[0],   edge01 )


    def test_undirected_neighbors_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")


        rtn01 = node02.undirected_neighbors()
    
        self.assertEqual( len(rtn01), 2      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )


    def test_undirected_neighbors_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "undirected")

        rtn01 = node02.undirected_neighbors()
    
        self.assertEqual( len(rtn01), 3      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )
        self.assertEqual( rtn01[2],   edge03 )


    def test_undirected_neighbors_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "undirected")

        rtn01 = node02.undirected_neighbors()
    
        self.assertEqual( len(rtn01), 3      )
        self.assertEqual( rtn01[0],   edge01 )
        self.assertEqual( rtn01[1],   edge02 )
        self.assertEqual( rtn01[2],   edge03 )


    def test_undirected_degree_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertEqual( node01.undirected_degree(), 0 )


    def test_undirected_degree_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        self.assertEqual( node02.undirected_degree(), 1 )


    def test_undirected_degree_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")

        self.assertEqual( node02.undirected_degree(), 2 )


    def test_undirected_degree_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "undirected")

        self.assertEqual( node02.undirected_degree(), 3 )


    def test_undirected_degree_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "undirected")

        rtn01 = node02.undirected_neighbors()
    
        self.assertEqual( node02.undirected_degree(), 3 )


    def test_undirected_neighbor_head_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertIsNone( node01.undirected_neighbor_head() )


    def test_undirected_neighbor_head_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_head(), edge01 )


    def test_undirected_neighbor_head_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_head(), edge01 )


    def test_undirected_neighbor_head_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_head(), edge01 )


    def test_undirected_neighbor_head_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_head(), edge01 )


    def test_undirected_neighbor_tail_zero_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        self.assertIsNone( node01.undirected_neighbor_tail() )


    def test_undirected_neighbor_tail_one_edge(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_tail(), edge01 )


    def test_undirected_neighbor_tail_two_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_tail(), edge02 )


    def test_undirected_neighbor_tail_three_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node03, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node04, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_tail(), edge03 )


    def test_undirected_neighbor_tail_three_multiedges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected")

        edge02 = nlpregex.abs_graph.edge.BaseEdge()
        edge02.add_to_graph(graph01, node01, node02, "undirected")

        edge03 = nlpregex.abs_graph.edge.BaseEdge()
        edge03.add_to_graph(graph01, node01, node02, "undirected")

        self.assertEqual( node02.undirected_neighbor_tail(), edge03 )


    def test_all_neighbors_mixed(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        node05  = nlpregex.abs_graph.node.BaseNode()
        node05.add_to_graph(graph01)

        node06  = nlpregex.abs_graph.node.BaseNode()
        node06.add_to_graph(graph01)

        node07  = nlpregex.abs_graph.node.BaseNode()
        node07.add_to_graph(graph01)

        node08  = nlpregex.abs_graph.node.BaseNode()
        node08.add_to_graph(graph01)

        node09  = nlpregex.abs_graph.node.BaseNode()
        node09.add_to_graph(graph01)

        node10  = nlpregex.abs_graph.node.BaseNode()
        node10.add_to_graph(graph01)

        edge_01_02_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed")

        edge_01_03_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03_dir.add_to_graph(graph01, node01, node03, "directed")

        edge_01_04_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04_dir.add_to_graph(graph01, node01, node04, "directed")

        edge_05_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_05_01_dir.add_to_graph(graph01, node05, node01, "directed")

        edge_06_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_06_01_dir.add_to_graph(graph01, node06, node01, "directed")

        edge_07_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_07_01_dir.add_to_graph(graph01, node07, node01, "directed")

        edge_01_08_undir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_08_undir.add_to_graph(graph01, node01, node08, "undirected")

        edge_01_09_undir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_09_undir.add_to_graph(graph01, node01, node09, "undirected")

        edge_01_10_undir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_10_undir.add_to_graph(graph01, node01, node10, "undirected")

        rtn01 = node01.all_neighbors()

        self.assertEqual( len( rtn01 ), 9 )
        self.assertEqual( rtn01[0], edge_05_01_dir   )
        self.assertEqual( rtn01[1], edge_06_01_dir   )
        self.assertEqual( rtn01[2], edge_07_01_dir   )
        self.assertEqual( rtn01[3], edge_01_02_dir   )
        self.assertEqual( rtn01[4], edge_01_03_dir   )
        self.assertEqual( rtn01[5], edge_01_04_dir   )
        self.assertEqual( rtn01[6], edge_01_08_undir )
        self.assertEqual( rtn01[7], edge_01_09_undir )
        self.assertEqual( rtn01[8], edge_01_10_undir )


    def test_all_neighbors_mixed(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        node05  = nlpregex.abs_graph.node.BaseNode()
        node05.add_to_graph(graph01)

        node06  = nlpregex.abs_graph.node.BaseNode()
        node06.add_to_graph(graph01)

        node07  = nlpregex.abs_graph.node.BaseNode()
        node07.add_to_graph(graph01)

        node08  = nlpregex.abs_graph.node.BaseNode()
        node08.add_to_graph(graph01)

        node09  = nlpregex.abs_graph.node.BaseNode()
        node09.add_to_graph(graph01)

        node10  = nlpregex.abs_graph.node.BaseNode()
        node10.add_to_graph(graph01)

        edge_01_02_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed")

        edge_01_03_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03_dir.add_to_graph(graph01, node01, node03, "directed")

        edge_01_04_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04_dir.add_to_graph(graph01, node01, node04, "directed")

        edge_05_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_05_01_dir.add_to_graph(graph01, node05, node01, "directed")

        edge_06_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_06_01_dir.add_to_graph(graph01, node06, node01, "directed")

        edge_07_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_07_01_dir.add_to_graph(graph01, node07, node01, "directed")

        edge_01_08_undir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_08_undir.add_to_graph(graph01, node01, node08, "undirected")

        edge_01_09_undir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_09_undir.add_to_graph(graph01, node01, node09, "undirected")

        edge_01_10_undir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_10_undir.add_to_graph(graph01, node01, node10, "undirected")

        rtn01 = node01.remove_from_graph()

        self.assertEqual( graph01.num_nodes(), 9 )
        self.assertEqual( graph01.num_edges(), 0 )

        self.assertIsNone( node01.graph )
        self.assertIsNone( node01.graph_delg )

        self.assertEqual( node01.in_neighbors_list.cnt(),         0 )
        self.assertEqual( node01.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node01.undirected_neighbors_list.cnt(), 0 )

        self.assertEqual( len( rtn01 ), 9 )

        self.assertEqual( rtn01[0][0] , edge_05_01_dir )
        self.assertEqual( rtn01[1][0] , edge_06_01_dir )
        self.assertEqual( rtn01[2][0] , edge_07_01_dir )
        self.assertEqual( rtn01[3][0] , edge_01_02_dir )
        self.assertEqual( rtn01[4][0] , edge_01_03_dir )
        self.assertEqual( rtn01[5][0] , edge_01_04_dir )
        self.assertEqual( rtn01[6][0] , edge_01_08_undir )
        self.assertEqual( rtn01[7][0] , edge_01_09_undir )
        self.assertEqual( rtn01[8][0] , edge_01_10_undir )

        self.assertEqual( rtn01[0][1] , (node05, node01) )
        self.assertEqual( rtn01[1][1] , (node06, node01) )
        self.assertEqual( rtn01[2][1] , (node07, node01) )
        self.assertEqual( rtn01[3][1] , (node01, node02) )
        self.assertEqual( rtn01[4][1] , (node01, node03) )
        self.assertEqual( rtn01[5][1] , (node01, node04) )
        self.assertEqual( rtn01[6][1] , (node01, node08) )
        self.assertEqual( rtn01[7][1] , (node01, node09) )
        self.assertEqual( rtn01[8][1] , (node01, node10) )


    def test_add_to_graph(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph( graph01 )

        self.assertEqual( graph01.num_nodes(), 1      )
        self.assertEqual( graph01.nodes()[0],  node01 )
        self.assertEqual( node01.graph ,       graph01)


    def test_remove_from_graph(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        node05  = nlpregex.abs_graph.node.BaseNode()
        node05.add_to_graph(graph01)

        node06  = nlpregex.abs_graph.node.BaseNode()
        node06.add_to_graph(graph01)

        node07  = nlpregex.abs_graph.node.BaseNode()
        node07.add_to_graph(graph01)

        edge_02_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_01_dir.add_to_graph(graph01, node02, node01, "directed")

        edge_03_01_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_01_dir.add_to_graph(graph01, node03, node01, "directed")

        edge_01_04_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04_dir.add_to_graph(graph01, node01, node04, "directed")

        edge_01_05_dir = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05_dir.add_to_graph(graph01, node01, node05, "directed")

        edge_01_06 = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_06.add_to_graph(graph01, node01, node06, "undirected")

        edge_01_07 = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_07.add_to_graph(graph01, node01, node07, "undirected")

        edge_list01 = node01.remove_from_graph()

        self.assertEqual( graph01.num_nodes(), 6      )
        self.assertEqual( graph01.nodes()[0],  node02 )
        self.assertEqual( graph01.nodes()[1],  node03 )
        self.assertEqual( graph01.nodes()[2],  node04 )
        self.assertEqual( graph01.nodes()[3],  node05 )
        self.assertEqual( graph01.nodes()[4],  node06 )
        self.assertEqual( graph01.nodes()[5],  node07 )

        self.assertIsNone( node01.graph )
        self.assertIsNone( node01.graph_delg )

        self.assertEqual( node01. in_neighbors_list.cnt(),        0 )
        self.assertEqual( node01.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node01.undirected_neighbors_list.cnt(), 0 )

        self.assertEqual( node02. in_neighbors_list.cnt(),        0 )
        self.assertEqual( node02.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node02.undirected_neighbors_list.cnt(), 0 )

        self.assertEqual( node03. in_neighbors_list.cnt(),        0 )
        self.assertEqual( node03.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node03.undirected_neighbors_list.cnt(), 0 )

        self.assertEqual( node04. in_neighbors_list.cnt(),        0 )
        self.assertEqual( node04.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node04.undirected_neighbors_list.cnt(), 0 )

        self.assertEqual( node05. in_neighbors_list.cnt(),        0 )
        self.assertEqual( node05.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node05.undirected_neighbors_list.cnt(), 0 )

        self.assertEqual( node06. in_neighbors_list.cnt(),        0 )
        self.assertEqual( node06.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node06.undirected_neighbors_list.cnt(), 0 )

        self.assertEqual( node07. in_neighbors_list.cnt(),        0 )
        self.assertEqual( node07.out_neighbors_list.cnt(),        0 )
        self.assertEqual( node07.undirected_neighbors_list.cnt(), 0 )



if __name__ == '__main__':
    unittest.main()
