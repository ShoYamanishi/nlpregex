#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for BaseEdge."""

import unittest
import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph


class test_BaseEdge ( unittest.TestCase ):


    def test_constructor(self):

        edge01 = nlpregex.abs_graph.edge.BaseEdge()

        self.assertIsNone    ( edge01.graph )
        self.assertIsNone    ( edge01.graph_delg )

        self.assertIsNone    ( edge01.src_node )
        self.assertIsNone    ( edge01.src_delg )
        self.assertIsNone    ( edge01.dst_node )
        self.assertIsNone    ( edge01.dst_delg )


    def test_add_to_graph_directed(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed" )

        self.assertEqual( graph01.num_directed_edges(),   1 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge01 )

        self.assertEqual( edge01.graph,                   graph01 )
        self.assertEqual( edge01.src_node,                node01 )
        self.assertEqual( edge01.dst_node,                node02 )

        self.assertEqual( node01.in_degree(),             0 )
        self.assertEqual( node01.out_degree(),            1 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.out_neighbors()[0],      edge01 )

        self.assertEqual( node02.in_degree(),             1 )
        self.assertEqual( node02.out_degree(),            0 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.in_neighbors()[0],       edge01 )


    def test_add_to_graph_undirected(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected" )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   1 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01 )

        self.assertEqual( edge01.graph,                     graph01 )
        self.assertEqual( edge01.src_node,                  node01 )
        self.assertEqual( edge01.dst_node,                  node02 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       1 )
        self.assertEqual( node01.undirected_neighbors()[0], edge01 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01 )


    def test_remove_from_graph_directed(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed" )

        rtn_pair_01 = edge01.remove_from_graph()

        self.assertEqual( rtn_pair_01, (node01, node02) )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   0 )
        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       0 )
        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       0 )

        self.assertIsNone    ( edge01.graph )
        self.assertIsNone    ( edge01.graph_delg )

        self.assertIsNone    ( edge01.src_node )
        self.assertIsNone    ( edge01.src_delg )
        self.assertIsNone    ( edge01.dst_node )
        self.assertIsNone    ( edge01.dst_delg )


    def test_remove_from_graph_undirected(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected" )

        rtn_pair_01 = edge01.remove_from_graph()

        self.assertEqual( rtn_pair_01, (node01, node02) )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   0 )
        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       0 )
        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       0 )

        self.assertIsNone    ( edge01.graph )
        self.assertIsNone    ( edge01.graph_delg )

        self.assertIsNone    ( edge01.src_node )
        self.assertIsNone    ( edge01.src_delg )
        self.assertIsNone    ( edge01.dst_node )
        self.assertIsNone    ( edge01.dst_delg )


    def test_other_node_of_directed(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "directed" )

        self.assertEqual( edge01.other_node_of(node01), node02 )
        self.assertEqual( edge01.other_node_of(node02), node01 )


    def test_other_node_of_undirected(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01 = nlpregex.abs_graph.edge.BaseEdge()
        edge01.add_to_graph(graph01, node01, node02, "undirected" )

        self.assertEqual( edge01.other_node_of(node01), node02 )
        self.assertEqual( edge01.other_node_of(node02), node01 )


    def test_add_to_graph_at_specific_positions_directed_empty(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph_at_specific_positions( graph01, node01, node02, "directed", None, None )

        self.assertEqual( graph01.num_directed_edges(),   1 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge01_02 )

        self.assertEqual( edge01_02.graph,                graph01 )
        self.assertEqual( edge01_02.src_node,             node01 )
        self.assertEqual( edge01_02.dst_node,             node02 )

        self.assertEqual( node01.in_degree(),             0 )
        self.assertEqual( node01.out_degree(),            1 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.out_neighbors()[0],      edge01_02 )

        self.assertEqual( node02.in_degree(),             1 )
        self.assertEqual( node02.out_degree(),            0 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.in_neighbors()[0],       edge01_02 )


    def test_add_to_graph_at_specific_positions_directed_ptn01_01(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "directed" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph_at_specific_positions( graph01, node01, node03, "directed", None, None )

        self.assertEqual( graph01.num_directed_edges(),   2 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge01_02 )
        self.assertEqual( graph01.directed_edges()[1],    edge01_03 )

        self.assertEqual( edge01_02.graph,                graph01 )
        self.assertEqual( edge01_02.src_node,             node01 )
        self.assertEqual( edge01_02.dst_node,             node02 )

        self.assertEqual( edge01_03.graph,                graph01 )
        self.assertEqual( edge01_03.src_node,             node01 )
        self.assertEqual( edge01_03.dst_node,             node03 )

        self.assertEqual( node01.in_degree(),             0 )
        self.assertEqual( node01.out_degree(),            2 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.out_neighbors()[0],      edge01_02 )
        self.assertEqual( node01.out_neighbors()[1],      edge01_03 )

        self.assertEqual( node02.in_degree(),             1 )
        self.assertEqual( node02.out_degree(),            0 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.in_neighbors()[0],       edge01_02 )

        self.assertEqual( node03.in_degree(),             1 )
        self.assertEqual( node03.out_degree(),            0 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.in_neighbors()[0],       edge01_03 )


    def test_add_to_graph_at_specific_positions_directed_ptn01_02(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "directed" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph_at_specific_positions( graph01, node01, node03, "directed", edge01_02, None )

        self.assertEqual( graph01.num_directed_edges(),   2 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge01_02 )
        self.assertEqual( graph01.directed_edges()[1],    edge01_03 )

        self.assertEqual( edge01_02.graph,                graph01 )
        self.assertEqual( edge01_02.src_node,             node01 )
        self.assertEqual( edge01_02.dst_node,             node02 )

        self.assertEqual( edge01_03.graph,                graph01 )
        self.assertEqual( edge01_03.src_node,             node01 )
        self.assertEqual( edge01_03.dst_node,             node03 )

        self.assertEqual( node01.in_degree(),             0 )
        self.assertEqual( node01.out_degree(),            2 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.out_neighbors()[0],      edge01_03 )
        self.assertEqual( node01.out_neighbors()[1],      edge01_02 )

        self.assertEqual( node02.in_degree(),             1 )
        self.assertEqual( node02.out_degree(),            0 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.in_neighbors()[0],       edge01_02 )

        self.assertEqual( node03.in_degree(),             1 )
        self.assertEqual( node03.out_degree(),            0 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.in_neighbors()[0],       edge01_03 )


    def test_add_to_graph_at_specific_positions_directed_ptn01_03(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "directed" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "directed" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "directed", None, None )

        self.assertEqual( graph01.num_directed_edges(),   3 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge01_02 )
        self.assertEqual( graph01.directed_edges()[1],    edge01_03 )
        self.assertEqual( graph01.directed_edges()[2],    edge01_04 )

        self.assertEqual( edge01_02.graph,                graph01 )
        self.assertEqual( edge01_02.src_node,             node01 )
        self.assertEqual( edge01_02.dst_node,             node02 )

        self.assertEqual( edge01_03.graph,                graph01 )
        self.assertEqual( edge01_03.src_node,             node01 )
        self.assertEqual( edge01_03.dst_node,             node03 )

        self.assertEqual( edge01_04.graph,                graph01 )
        self.assertEqual( edge01_04.src_node,             node01 )
        self.assertEqual( edge01_04.dst_node,             node04 )

        self.assertEqual( node01.in_degree(),             0 )
        self.assertEqual( node01.out_degree(),            3 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.out_neighbors()[0],      edge01_02 )
        self.assertEqual( node01.out_neighbors()[1],      edge01_03 )
        self.assertEqual( node01.out_neighbors()[2],      edge01_04 )

        self.assertEqual( node02.in_degree(),             1 )
        self.assertEqual( node02.out_degree(),            0 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.in_neighbors()[0],       edge01_02 )

        self.assertEqual( node03.in_degree(),             1 )
        self.assertEqual( node03.out_degree(),            0 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.in_neighbors()[0],       edge01_03 )

        self.assertEqual( node04.in_degree(),             1 )
        self.assertEqual( node04.out_degree(),            0 )
        self.assertEqual( node04.undirected_degree(),     0 )
        self.assertEqual( node04.in_neighbors()[0],       edge01_04 )


    def test_add_to_graph_at_specific_positions_directed_ptn01_04(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "directed" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "directed" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "directed", edge01_02, None )

        self.assertEqual( graph01.num_directed_edges(),   3 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge01_02 )
        self.assertEqual( graph01.directed_edges()[1],    edge01_03 )
        self.assertEqual( graph01.directed_edges()[2],    edge01_04 )

        self.assertEqual( edge01_02.graph,                graph01 )
        self.assertEqual( edge01_02.src_node,             node01 )
        self.assertEqual( edge01_02.dst_node,             node02 )

        self.assertEqual( edge01_03.graph,                graph01 )
        self.assertEqual( edge01_03.src_node,             node01 )
        self.assertEqual( edge01_03.dst_node,             node03 )

        self.assertEqual( edge01_04.graph,                graph01 )
        self.assertEqual( edge01_04.src_node,             node01 )
        self.assertEqual( edge01_04.dst_node,             node04 )

        self.assertEqual( node01.in_degree(),             0 )
        self.assertEqual( node01.out_degree(),            3 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.out_neighbors()[0],      edge01_04 )
        self.assertEqual( node01.out_neighbors()[1],      edge01_02 )
        self.assertEqual( node01.out_neighbors()[2],      edge01_03 )

        self.assertEqual( node02.in_degree(),             1 )
        self.assertEqual( node02.out_degree(),            0 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.in_neighbors()[0],       edge01_02 )

        self.assertEqual( node03.in_degree(),             1 )
        self.assertEqual( node03.out_degree(),            0 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.in_neighbors()[0],       edge01_03 )

        self.assertEqual( node04.in_degree(),             1 )
        self.assertEqual( node04.out_degree(),            0 )
        self.assertEqual( node04.undirected_degree(),     0 )
        self.assertEqual( node04.in_neighbors()[0],       edge01_04 )


    def test_add_to_graph_at_specific_positions_directed_ptn01_05(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "directed" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "directed" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "directed", edge01_03, None )

        self.assertEqual( graph01.num_directed_edges(),   3 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge01_02 )
        self.assertEqual( graph01.directed_edges()[1],    edge01_03 )
        self.assertEqual( graph01.directed_edges()[2],    edge01_04 )

        self.assertEqual( edge01_02.graph,                graph01 )
        self.assertEqual( edge01_02.src_node,             node01 )
        self.assertEqual( edge01_02.dst_node,             node02 )

        self.assertEqual( edge01_03.graph,                graph01 )
        self.assertEqual( edge01_03.src_node,             node01 )
        self.assertEqual( edge01_03.dst_node,             node03 )

        self.assertEqual( edge01_04.graph,                graph01 )
        self.assertEqual( edge01_04.src_node,             node01 )
        self.assertEqual( edge01_04.dst_node,             node04 )

        self.assertEqual( node01.in_degree(),             0 )
        self.assertEqual( node01.out_degree(),            3 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.out_neighbors()[0],      edge01_02 )
        self.assertEqual( node01.out_neighbors()[1],      edge01_04 )
        self.assertEqual( node01.out_neighbors()[2],      edge01_03 )

        self.assertEqual( node02.in_degree(),             1 )
        self.assertEqual( node02.out_degree(),            0 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.in_neighbors()[0],       edge01_02 )

        self.assertEqual( node03.in_degree(),             1 )
        self.assertEqual( node03.out_degree(),            0 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.in_neighbors()[0],       edge01_03 )

        self.assertEqual( node04.in_degree(),             1 )
        self.assertEqual( node04.out_degree(),            0 )
        self.assertEqual( node04.undirected_degree(),     0 )
        self.assertEqual( node04.in_neighbors()[0],       edge01_04 )


    def test_add_to_graph_at_specific_positions_directed_ptn02_01(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "directed" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph_at_specific_positions( graph01, node03, node01, "directed", None, None )

        self.assertEqual( graph01.num_directed_edges(),   2 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge02_01 )
        self.assertEqual( graph01.directed_edges()[1],    edge03_01 )

        self.assertEqual( edge02_01.graph,                graph01 )
        self.assertEqual( edge02_01.src_node,             node02 )
        self.assertEqual( edge02_01.dst_node,             node01 )

        self.assertEqual( edge03_01.graph,                graph01 )
        self.assertEqual( edge03_01.src_node,             node03 )
        self.assertEqual( edge03_01.dst_node,             node01 )

        self.assertEqual( node01.in_degree(),             2 )
        self.assertEqual( node01.out_degree(),            0 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.in_neighbors()[0],       edge02_01 )
        self.assertEqual( node01.in_neighbors()[1],       edge03_01 )

        self.assertEqual( node02.in_degree(),             0 )
        self.assertEqual( node02.out_degree(),            1 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.out_neighbors()[0],      edge02_01 )

        self.assertEqual( node03.in_degree(),             0 )
        self.assertEqual( node03.out_degree(),            1 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.out_neighbors()[0],      edge03_01 )


    def test_add_to_graph_at_specific_positions_directed_ptn02_02(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "directed" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph_at_specific_positions( graph01, node03, node01, "directed", None, edge02_01 )

        self.assertEqual( graph01.num_directed_edges(),   2 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge02_01 )
        self.assertEqual( graph01.directed_edges()[1],    edge03_01 )

        self.assertEqual( edge02_01.graph,                graph01 )
        self.assertEqual( edge02_01.src_node,             node02 )
        self.assertEqual( edge02_01.dst_node,             node01 )

        self.assertEqual( edge03_01.graph,                graph01 )
        self.assertEqual( edge03_01.src_node,             node03 )
        self.assertEqual( edge03_01.dst_node,             node01 )

        self.assertEqual( node01.in_degree(),             2 )
        self.assertEqual( node01.out_degree(),            0 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.in_neighbors()[0],       edge03_01 )
        self.assertEqual( node01.in_neighbors()[1],       edge02_01 )

        self.assertEqual( node02.in_degree(),             0 )
        self.assertEqual( node02.out_degree(),            1 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.out_neighbors()[0],      edge02_01 )

        self.assertEqual( node03.in_degree(),             0 )
        self.assertEqual( node03.out_degree(),            1 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.out_neighbors()[0],      edge03_01 )


    def test_add_to_graph_at_specific_positions_directed_ptn02_03(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "directed" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "directed" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "directed", None, None )

        self.assertEqual( graph01.num_directed_edges(),   3 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge02_01 )
        self.assertEqual( graph01.directed_edges()[1],    edge03_01 )
        self.assertEqual( graph01.directed_edges()[2],    edge04_01 )

        self.assertEqual( edge02_01.graph,                graph01 )
        self.assertEqual( edge02_01.src_node,             node02 )
        self.assertEqual( edge02_01.dst_node,             node01 )

        self.assertEqual( edge03_01.graph,                graph01 )
        self.assertEqual( edge03_01.src_node,             node03 )
        self.assertEqual( edge03_01.dst_node,             node01 )

        self.assertEqual( edge04_01.graph,                graph01 )
        self.assertEqual( edge04_01.src_node,             node04 )
        self.assertEqual( edge04_01.dst_node,             node01 )

        self.assertEqual( node01.in_degree(),             3 )
        self.assertEqual( node01.out_degree(),            0 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.in_neighbors()[0],       edge02_01 )
        self.assertEqual( node01.in_neighbors()[1],       edge03_01 )
        self.assertEqual( node01.in_neighbors()[2],       edge04_01 )

        self.assertEqual( node02.in_degree(),             0 )
        self.assertEqual( node02.out_degree(),            1 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.out_neighbors()[0],      edge02_01 )

        self.assertEqual( node03.in_degree(),             0 )
        self.assertEqual( node03.out_degree(),            1 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.out_neighbors()[0],      edge03_01 )

        self.assertEqual( node04.in_degree(),             0 )
        self.assertEqual( node04.out_degree(),            1 )
        self.assertEqual( node04.undirected_degree(),     0 )
        self.assertEqual( node04.out_neighbors()[0],      edge04_01 )


    def test_add_to_graph_at_specific_positions_directed_ptn02_04(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "directed" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "directed" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "directed", None, edge02_01 )

        self.assertEqual( graph01.num_directed_edges(),   3 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge02_01 )
        self.assertEqual( graph01.directed_edges()[1],    edge03_01 )
        self.assertEqual( graph01.directed_edges()[2],    edge04_01 )

        self.assertEqual( edge02_01.graph,                graph01 )
        self.assertEqual( edge02_01.src_node,             node02 )
        self.assertEqual( edge02_01.dst_node,             node01 )

        self.assertEqual( edge03_01.graph,                graph01 )
        self.assertEqual( edge03_01.src_node,             node03 )
        self.assertEqual( edge03_01.dst_node,             node01 )

        self.assertEqual( edge04_01.graph,                graph01 )
        self.assertEqual( edge04_01.src_node,             node04 )
        self.assertEqual( edge04_01.dst_node,             node01 )

        self.assertEqual( node01.in_degree(),             3 )
        self.assertEqual( node01.out_degree(),            0 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.in_neighbors()[0],       edge04_01 )
        self.assertEqual( node01.in_neighbors()[1],       edge02_01 )
        self.assertEqual( node01.in_neighbors()[2],       edge03_01 )

        self.assertEqual( node02.in_degree(),             0 )
        self.assertEqual( node02.out_degree(),            1 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.out_neighbors()[0],      edge02_01 )

        self.assertEqual( node03.in_degree(),             0 )
        self.assertEqual( node03.out_degree(),            1 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.out_neighbors()[0],      edge03_01 )

        self.assertEqual( node04.in_degree(),             0 )
        self.assertEqual( node04.out_degree(),            1 )
        self.assertEqual( node04.undirected_degree(),     0 )
        self.assertEqual( node04.out_neighbors()[0],      edge04_01 )


    def test_add_to_graph_at_specific_positions_directed_ptn02_05(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "directed" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "directed" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "directed", None, edge03_01 )

        self.assertEqual( graph01.num_directed_edges(),   3 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.directed_edges()[0],    edge02_01 )
        self.assertEqual( graph01.directed_edges()[1],    edge03_01 )
        self.assertEqual( graph01.directed_edges()[2],    edge04_01 )

        self.assertEqual( edge02_01.graph,                graph01 )
        self.assertEqual( edge02_01.src_node,             node02 )
        self.assertEqual( edge02_01.dst_node,             node01 )

        self.assertEqual( edge03_01.graph,                graph01 )
        self.assertEqual( edge03_01.src_node,             node03 )
        self.assertEqual( edge03_01.dst_node,             node01 )

        self.assertEqual( edge04_01.graph,                graph01 )
        self.assertEqual( edge04_01.src_node,             node04 )
        self.assertEqual( edge04_01.dst_node,             node01 )

        self.assertEqual( node01.in_degree(),             3 )
        self.assertEqual( node01.out_degree(),            0 )
        self.assertEqual( node01.undirected_degree(),     0 )
        self.assertEqual( node01.in_neighbors()[0],       edge02_01 )
        self.assertEqual( node01.in_neighbors()[1],       edge04_01 )
        self.assertEqual( node01.in_neighbors()[2],       edge03_01 )

        self.assertEqual( node02.in_degree(),             0 )
        self.assertEqual( node02.out_degree(),            1 )
        self.assertEqual( node02.undirected_degree(),     0 )
        self.assertEqual( node02.out_neighbors()[0],      edge02_01 )

        self.assertEqual( node03.in_degree(),             0 )
        self.assertEqual( node03.out_degree(),            1 )
        self.assertEqual( node03.undirected_degree(),     0 )
        self.assertEqual( node03.out_neighbors()[0],      edge03_01 )

        self.assertEqual( node04.in_degree(),             0 )
        self.assertEqual( node04.out_degree(),            1 )
        self.assertEqual( node04.undirected_degree(),     0 )
        self.assertEqual( node04.out_neighbors()[0],      edge04_01 )


    def test_add_to_graph_at_specific_positions_undirected_empty(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph_at_specific_positions( graph01, node01, node02, "undirected", None, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   1 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01_02 )

        self.assertEqual( edge01_02.graph,                  graph01 )
        self.assertEqual( edge01_02.src_node,               node01 )
        self.assertEqual( edge01_02.dst_node,               node02 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       1 )
        self.assertEqual( node01.undirected_neighbors()[0], edge01_02 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01_02 )


    def test_add_to_graph_at_specific_positions_undirected_ptn01_01(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "undirected" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "undirected" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "undirected", None, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01_02 )
        self.assertEqual( graph01.undirected_edges()[1],    edge01_03 )
        self.assertEqual( graph01.undirected_edges()[2],    edge01_04 )

        self.assertEqual( edge01_02.graph,                  graph01 )
        self.assertEqual( edge01_02.src_node,               node01 )
        self.assertEqual( edge01_02.dst_node,               node02 )

        self.assertEqual( edge01_03.graph,                  graph01 )
        self.assertEqual( edge01_03.src_node,               node01 )
        self.assertEqual( edge01_03.dst_node,               node03 )

        self.assertEqual( edge01_04.graph,                  graph01 )
        self.assertEqual( edge01_04.src_node,               node01 )
        self.assertEqual( edge01_04.dst_node,               node04 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge01_02 )
        self.assertEqual( node01.undirected_neighbors()[1], edge01_03 )
        self.assertEqual( node01.undirected_neighbors()[2], edge01_04 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01_02 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge01_03 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge01_04 )


    def test_add_to_graph_at_specific_positions_undirected_ptn01_02(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "undirected" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "undirected" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "undirected", edge01_02, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01_02 )
        self.assertEqual( graph01.undirected_edges()[1],    edge01_03 )
        self.assertEqual( graph01.undirected_edges()[2],    edge01_04 )

        self.assertEqual( edge01_02.graph,                  graph01 )
        self.assertEqual( edge01_02.src_node,               node01 )
        self.assertEqual( edge01_02.dst_node,               node02 )

        self.assertEqual( edge01_03.graph,                  graph01 )
        self.assertEqual( edge01_03.src_node,               node01 )
        self.assertEqual( edge01_03.dst_node,               node03 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge01_04 )
        self.assertEqual( node01.undirected_neighbors()[1], edge01_02 )
        self.assertEqual( node01.undirected_neighbors()[2], edge01_03 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01_02 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge01_03 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge01_04 )


    def test_add_to_graph_at_specific_positions_undirected_ptn01_03(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "undirected" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "undirected" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "undirected", edge01_03, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01_02 )
        self.assertEqual( graph01.undirected_edges()[1],    edge01_03 )
        self.assertEqual( graph01.undirected_edges()[2],    edge01_04 )

        self.assertEqual( edge01_02.graph,                  graph01 )
        self.assertEqual( edge01_02.src_node,               node01 )
        self.assertEqual( edge01_02.dst_node,               node02 )

        self.assertEqual( edge01_03.graph,                  graph01 )
        self.assertEqual( edge01_03.src_node,               node01 )
        self.assertEqual( edge01_03.dst_node,               node03 )

        self.assertEqual( edge01_04.graph,                  graph01 )
        self.assertEqual( edge01_04.src_node,               node01 )
        self.assertEqual( edge01_04.dst_node,               node04 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge01_02 )
        self.assertEqual( node01.undirected_neighbors()[1], edge01_04 )
        self.assertEqual( node01.undirected_neighbors()[2], edge01_03 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01_02 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge01_03 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge01_04 )


    def test_add_to_graph_at_specific_positions_undirected_ptn01_04(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "undirected" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "undirected" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "undirected", None, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge02_01 )
        self.assertEqual( graph01.undirected_edges()[1],    edge03_01 )
        self.assertEqual( graph01.undirected_edges()[2],    edge01_04 )

        self.assertEqual( edge02_01.graph,                  graph01 )
        self.assertEqual( edge02_01.src_node,               node02 )
        self.assertEqual( edge02_01.dst_node,               node01 )

        self.assertEqual( edge03_01.graph,                  graph01 )
        self.assertEqual( edge03_01.src_node,               node03 )
        self.assertEqual( edge03_01.dst_node,               node01 )

        self.assertEqual( edge01_04.graph,                  graph01 )
        self.assertEqual( edge01_04.src_node,               node01 )
        self.assertEqual( edge01_04.dst_node,               node04 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge02_01 )
        self.assertEqual( node01.undirected_neighbors()[1], edge03_01 )
        self.assertEqual( node01.undirected_neighbors()[2], edge01_04 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge02_01 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge03_01 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge01_04 )


    def test_add_to_graph_at_specific_positions_undirected_ptn01_05(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "undirected" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "undirected" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "undirected", edge02_01, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge02_01 )
        self.assertEqual( graph01.undirected_edges()[1],    edge03_01 )
        self.assertEqual( graph01.undirected_edges()[2],    edge01_04 )

        self.assertEqual( edge02_01.graph,                  graph01 )
        self.assertEqual( edge02_01.src_node,               node02 )
        self.assertEqual( edge02_01.dst_node,               node01 )

        self.assertEqual( edge03_01.graph,                  graph01 )
        self.assertEqual( edge03_01.src_node,               node03 )
        self.assertEqual( edge03_01.dst_node,               node01 )

        self.assertEqual( edge01_04.graph,                  graph01 )
        self.assertEqual( edge01_04.src_node,               node01 )
        self.assertEqual( edge01_04.dst_node,               node04 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge01_04 )
        self.assertEqual( node01.undirected_neighbors()[1], edge02_01 )
        self.assertEqual( node01.undirected_neighbors()[2], edge03_01 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge02_01 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge03_01 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge01_04 )


    def test_add_to_graph_at_specific_positions_undirected_ptn01_06(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "undirected" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "undirected" )

        edge01_04 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_04.add_to_graph_at_specific_positions( graph01, node01, node04, "undirected", edge03_01, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge02_01 )
        self.assertEqual( graph01.undirected_edges()[1],    edge03_01 )
        self.assertEqual( graph01.undirected_edges()[2],    edge01_04 )

        self.assertEqual( edge02_01.graph,                  graph01 )
        self.assertEqual( edge02_01.src_node,               node02 )
        self.assertEqual( edge02_01.dst_node,               node01 )

        self.assertEqual( edge03_01.graph,                  graph01 )
        self.assertEqual( edge03_01.src_node,               node03 )
        self.assertEqual( edge03_01.dst_node,               node01 )

        self.assertEqual( edge01_04.graph,                  graph01 )
        self.assertEqual( edge01_04.src_node,               node01 )
        self.assertEqual( edge01_04.dst_node,               node04 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge02_01 )
        self.assertEqual( node01.undirected_neighbors()[1], edge01_04 )
        self.assertEqual( node01.undirected_neighbors()[2], edge03_01 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge02_01 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge03_01 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge01_04 )


    def test_add_to_graph_at_specific_positions_undirected_ptn02_01(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "undirected" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "undirected" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "undirected", None, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge02_01 )
        self.assertEqual( graph01.undirected_edges()[1],    edge03_01 )
        self.assertEqual( graph01.undirected_edges()[2],    edge04_01 )

        self.assertEqual( edge02_01.graph,                  graph01 )
        self.assertEqual( edge02_01.src_node,               node02 )
        self.assertEqual( edge02_01.dst_node,               node01 )

        self.assertEqual( edge03_01.graph,                  graph01 )
        self.assertEqual( edge03_01.src_node,               node03 )
        self.assertEqual( edge03_01.dst_node,               node01 )

        self.assertEqual( edge04_01.graph,                  graph01 )
        self.assertEqual( edge04_01.src_node,               node04 )
        self.assertEqual( edge04_01.dst_node,               node01 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge02_01 )
        self.assertEqual( node01.undirected_neighbors()[1], edge03_01 )
        self.assertEqual( node01.undirected_neighbors()[2], edge04_01 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge02_01 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge03_01 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge04_01 )


    def test_add_to_graph_at_specific_positions_undirected_ptn02_02(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "undirected" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "undirected" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "undirected", None, edge02_01 )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge02_01 )
        self.assertEqual( graph01.undirected_edges()[1],    edge03_01 )
        self.assertEqual( graph01.undirected_edges()[2],    edge04_01 )

        self.assertEqual( edge02_01.graph,                  graph01 )
        self.assertEqual( edge02_01.src_node,               node02 )
        self.assertEqual( edge02_01.dst_node,               node01 )

        self.assertEqual( edge03_01.graph,                  graph01 )
        self.assertEqual( edge03_01.src_node,               node03 )
        self.assertEqual( edge03_01.dst_node,               node01 )

        self.assertEqual( edge04_01.graph,                  graph01 )
        self.assertEqual( edge04_01.src_node,               node04 )
        self.assertEqual( edge04_01.dst_node,               node01 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )
        self.assertEqual( node01.undirected_neighbors()[0], edge04_01 )
        self.assertEqual( node01.undirected_neighbors()[1], edge02_01 )
        self.assertEqual( node01.undirected_neighbors()[2], edge03_01 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge02_01 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge03_01 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge04_01 )


    def test_add_to_graph_at_specific_positions_undirected_ptn02_03(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge02_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge02_01.add_to_graph( graph01, node02, node01, "undirected" )

        edge03_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge03_01.add_to_graph( graph01, node03, node01, "undirected" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "undirected", None, edge03_01 )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge02_01 )
        self.assertEqual( graph01.undirected_edges()[1],    edge03_01 )
        self.assertEqual( graph01.undirected_edges()[2],    edge04_01 )

        self.assertEqual( edge02_01.graph,                  graph01 )
        self.assertEqual( edge02_01.src_node,               node02 )
        self.assertEqual( edge02_01.dst_node,               node01 )

        self.assertEqual( edge03_01.graph,                  graph01 )
        self.assertEqual( edge03_01.src_node,               node03 )
        self.assertEqual( edge03_01.dst_node,               node01 )

        self.assertEqual( edge04_01.graph,                  graph01 )
        self.assertEqual( edge04_01.src_node,               node04 )
        self.assertEqual( edge04_01.dst_node,               node01 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )

        self.assertEqual( node01.undirected_neighbors()[0], edge02_01 )
        self.assertEqual( node01.undirected_neighbors()[1], edge04_01 )
        self.assertEqual( node01.undirected_neighbors()[2], edge03_01 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge02_01 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge03_01 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge04_01 )


    def test_add_to_graph_at_specific_positions_undirected_ptn02_04(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "undirected" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "undirected" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "undirected", None, None )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01_02 )
        self.assertEqual( graph01.undirected_edges()[1],    edge01_03 )
        self.assertEqual( graph01.undirected_edges()[2],    edge04_01 )

        self.assertEqual( edge01_02.graph,                  graph01 )
        self.assertEqual( edge01_02.src_node,               node01 )
        self.assertEqual( edge01_02.dst_node,               node02 )

        self.assertEqual( edge01_03.graph,                  graph01 )
        self.assertEqual( edge01_03.src_node,               node01 )
        self.assertEqual( edge01_03.dst_node,               node03 )

        self.assertEqual( edge04_01.graph,                  graph01 )
        self.assertEqual( edge04_01.src_node,               node04 )
        self.assertEqual( edge04_01.dst_node,               node01 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )

        self.assertEqual( node01.undirected_neighbors()[0], edge01_02 )
        self.assertEqual( node01.undirected_neighbors()[1], edge01_03 )
        self.assertEqual( node01.undirected_neighbors()[2], edge04_01 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01_02 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge01_03 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge04_01 )


    def test_add_to_graph_at_specific_positions_undirected_ptn02_05(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "undirected" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "undirected" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "undirected", None, edge01_02 )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01_02 )
        self.assertEqual( graph01.undirected_edges()[1],    edge01_03 )
        self.assertEqual( graph01.undirected_edges()[2],    edge04_01 )

        self.assertEqual( edge01_02.graph,                  graph01 )
        self.assertEqual( edge01_02.src_node,               node01 )
        self.assertEqual( edge01_02.dst_node,               node02 )

        self.assertEqual( edge01_03.graph,                  graph01 )
        self.assertEqual( edge01_03.src_node,               node01 )
        self.assertEqual( edge01_03.dst_node,               node03 )

        self.assertEqual( edge04_01.graph,                  graph01 )
        self.assertEqual( edge04_01.src_node,               node04 )
        self.assertEqual( edge04_01.dst_node,               node01 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )

        self.assertEqual( node01.undirected_neighbors()[0], edge04_01 )
        self.assertEqual( node01.undirected_neighbors()[1], edge01_02 )
        self.assertEqual( node01.undirected_neighbors()[2], edge01_03 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01_02 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge01_03 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge04_01 )


    def test_add_to_graph_at_specific_positions_undirected_ptn02_06(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph01)

        edge01_02 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_02.add_to_graph( graph01, node01, node02, "undirected" )

        edge01_03 = nlpregex.abs_graph.edge.BaseEdge()
        edge01_03.add_to_graph( graph01, node01, node03, "undirected" )

        edge04_01 = nlpregex.abs_graph.edge.BaseEdge()
        edge04_01.add_to_graph_at_specific_positions( graph01, node04, node01, "undirected", None, edge01_03 )

        self.assertEqual( graph01.num_directed_edges(),     0 )
        self.assertEqual( graph01.num_undirected_edges(),   3 )
        self.assertEqual( graph01.undirected_edges()[0],    edge01_02 )
        self.assertEqual( graph01.undirected_edges()[1],    edge01_03 )
        self.assertEqual( graph01.undirected_edges()[2],    edge04_01 )

        self.assertEqual( edge01_02.graph,                  graph01 )
        self.assertEqual( edge01_02.src_node,               node01 )
        self.assertEqual( edge01_02.dst_node,               node02 )

        self.assertEqual( edge01_03.graph,                  graph01 )
        self.assertEqual( edge01_03.src_node,               node01 )
        self.assertEqual( edge01_03.dst_node,               node03 )

        self.assertEqual( edge04_01.graph,                  graph01 )
        self.assertEqual( edge04_01.src_node,               node04 )
        self.assertEqual( edge04_01.dst_node,               node01 )

        self.assertEqual( node01.in_degree(),               0 )
        self.assertEqual( node01.out_degree(),              0 )
        self.assertEqual( node01.undirected_degree(),       3 )

        self.assertEqual( node01.undirected_neighbors()[0], edge01_02 )
        self.assertEqual( node01.undirected_neighbors()[1], edge04_01 )
        self.assertEqual( node01.undirected_neighbors()[2], edge01_03 )

        self.assertEqual( node02.in_degree(),               0 )
        self.assertEqual( node02.out_degree(),              0 )
        self.assertEqual( node02.undirected_degree(),       1 )
        self.assertEqual( node02.undirected_neighbors()[0], edge01_02 )

        self.assertEqual( node03.in_degree(),               0 )
        self.assertEqual( node03.out_degree(),              0 )
        self.assertEqual( node03.undirected_degree(),       1 )
        self.assertEqual( node03.undirected_neighbors()[0], edge01_03 )

        self.assertEqual( node04.in_degree(),               0 )
        self.assertEqual( node04.out_degree(),              0 )
        self.assertEqual( node04.undirected_degree(),       1 )
        self.assertEqual( node04.undirected_neighbors()[0], edge04_01 )


if __name__ == '__main__':
    unittest.main()
