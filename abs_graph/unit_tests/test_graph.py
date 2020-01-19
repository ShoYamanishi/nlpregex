#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for BaseGraph."""

import unittest
import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph


class test_BaseGraph ( unittest.TestCase ):


    def test_constructor(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        self.assertIsInstance( graph01.directed_edges_list,   nlpregex.abs_graph.double_link.List )
        self.assertIsInstance( graph01.undirected_edges_list, nlpregex.abs_graph.double_link.List )
        self.assertIsInstance( graph01.nodes_list,            nlpregex.abs_graph.double_link.List )


    def test_directed_edges_empty(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        rtn01 = graph01.directed_edges()
        self.assertEqual( len(rtn01), 0 )


    def test_directed_edges_K2(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        rtn01 = graph01.directed_edges()
        self.assertEqual( len(rtn01), 1 )
        self.assertEqual( rtn01[0], edge_01_02 )


    def test_directed_edges_K3(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_03_01  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_01.add_to_graph(graph01, node03, node01, "directed" )

        rtn01 = graph01.directed_edges()
        self.assertEqual( len(rtn01), 3 )
        self.assertEqual( rtn01[0], edge_01_02 )
        self.assertEqual( rtn01[1], edge_02_03 )
        self.assertEqual( rtn01[2], edge_03_01 )


    def test_directed_edges_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "directed" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "directed" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "directed" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "directed" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "directed" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "directed" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "directed" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "directed" )

        rtn01 = graph01.directed_edges()
        self.assertEqual( len(rtn01), 10 )
        self.assertEqual( rtn01[0], edge_01_02 )
        self.assertEqual( rtn01[1], edge_01_03 )
        self.assertEqual( rtn01[2], edge_01_04 )
        self.assertEqual( rtn01[3], edge_01_05 )
        self.assertEqual( rtn01[4], edge_02_03 )
        self.assertEqual( rtn01[5], edge_02_04 )
        self.assertEqual( rtn01[6], edge_02_05 )
        self.assertEqual( rtn01[7], edge_03_04 )
        self.assertEqual( rtn01[8], edge_03_05 )
        self.assertEqual( rtn01[9], edge_04_05 )


    def test_num_directed_edges_empty(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        self.assertEqual( graph01.num_directed_edges(), 0 )


    def test_num_directed_edges_K2(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        self.assertEqual( graph01.num_directed_edges(), 1 )


    def test_num_directed_edges_K3(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_03_01  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_01.add_to_graph(graph01, node03, node01, "directed" )

        self.assertEqual( graph01.num_directed_edges(), 3 )


    def test_num_directed_edges_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "directed" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "directed" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "directed" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "directed" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "directed" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "directed" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "directed" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "directed" )

        self.assertEqual( graph01.num_directed_edges(), 10 )


    def test_undirected_edges_empty(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        rtn01 = graph01.undirected_edges()
        self.assertEqual( len(rtn01), 0 )


    def test_undirected_edges_K2(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "undirected" )

        rtn01 = graph01.undirected_edges()
        self.assertEqual( len(rtn01), 1 )
        self.assertEqual( rtn01[0], edge_01_02 )


    def test_undirected_edges_K3(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "undirected" )

        edge_03_01  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_01.add_to_graph(graph01, node03, node01, "undirected" )

        rtn01 = graph01.undirected_edges()
        self.assertEqual( len(rtn01), 3 )
        self.assertEqual( rtn01[0], edge_01_02 )
        self.assertEqual( rtn01[1], edge_02_03 )
        self.assertEqual( rtn01[2], edge_03_01 )


    def test_undirected_edges_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "undirected" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "undirected" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "undirected" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "undirected" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "undirected" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "undirected" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "undirected" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "undirected" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "undirected" )

        rtn01 = graph01.undirected_edges()
        self.assertEqual( len(rtn01), 10 )
        self.assertEqual( rtn01[0], edge_01_02 )
        self.assertEqual( rtn01[1], edge_01_03 )
        self.assertEqual( rtn01[2], edge_01_04 )
        self.assertEqual( rtn01[3], edge_01_05 )
        self.assertEqual( rtn01[4], edge_02_03 )
        self.assertEqual( rtn01[5], edge_02_04 )
        self.assertEqual( rtn01[6], edge_02_05 )
        self.assertEqual( rtn01[7], edge_03_04 )
        self.assertEqual( rtn01[8], edge_03_05 )
        self.assertEqual( rtn01[9], edge_04_05 )


    def test_num_undirected_edges_empty(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        self.assertEqual( graph01.num_undirected_edges(), 0 )


    def test_num_undirected_edges_K2(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "undirected" )

        self.assertEqual( graph01.num_undirected_edges(), 1 )


    def test_num_undirected_edges_K3(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()
        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "undirected" )

        edge_03_01  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_01.add_to_graph(graph01, node03, node01, "undirected" )

        self.assertEqual( graph01.num_undirected_edges(), 3 )


    def test_num_undirected_edges_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "undirected" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "undirected" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "undirected" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "undirected" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "undirected" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "undirected" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "undirected" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "undirected" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "undirected" )

        self.assertEqual( graph01.num_undirected_edges(), 10 )


    def test_edges_mixed_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "undirected" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "directed" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "undirected" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "directed" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "undirected" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "directed" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "undirected" )

        rtn01 = graph01.edges()
        self.assertEqual( len(rtn01), 10 )
        self.assertEqual( rtn01[0], edge_01_02 )
        self.assertEqual( rtn01[5], edge_01_03 )
        self.assertEqual( rtn01[1], edge_01_04 )
        self.assertEqual( rtn01[6], edge_01_05 )
        self.assertEqual( rtn01[2], edge_02_03 )
        self.assertEqual( rtn01[7], edge_02_04 )
        self.assertEqual( rtn01[3], edge_02_05 )
        self.assertEqual( rtn01[8], edge_03_04 )
        self.assertEqual( rtn01[4], edge_03_05 )
        self.assertEqual( rtn01[9], edge_04_05 )


    def test_num_edges_mixed_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "undirected" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "directed" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "undirected" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "directed" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "undirected" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "directed" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "undirected" )

        self.assertEqual(  graph01.num_edges(), 10 )


    def test_nodes_mixed_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "undirected" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "directed" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "undirected" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "directed" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "undirected" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "directed" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "undirected" )

        rtn01 = graph01.nodes()

        self.assertEqual( len(rtn01), 5 )
        self.assertEqual( rtn01[0], node01 )
        self.assertEqual( rtn01[1], node02 )
        self.assertEqual( rtn01[2], node03 )
        self.assertEqual( rtn01[3], node04 )
        self.assertEqual( rtn01[4], node05 )


    def test_num_nodes_mixed_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "undirected" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "directed" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "undirected" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "directed" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "undirected" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "directed" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "undirected" )

        self.assertEqual( graph01.num_nodes(), 5 )


    def test_empty_mixed_K5(self):

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


        edge_01_02  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03.add_to_graph(graph01, node01, node03, "undirected" )

        edge_01_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_04.add_to_graph(graph01, node01, node04, "directed" )

        edge_01_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_05.add_to_graph(graph01, node01, node05, "undirected" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_04.add_to_graph(graph01, node02, node04, "undirected" )

        edge_02_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05.add_to_graph(graph01, node02, node05, "directed" )

        edge_03_04  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04.add_to_graph(graph01, node03, node04, "undirected" )

        edge_03_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_05.add_to_graph(graph01, node03, node05, "directed" )

        edge_04_05  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05.add_to_graph(graph01, node04, node05, "undirected" )

        graph01.empty()

        self.assertEqual( graph01.num_nodes(), 0 )
        self.assertEqual( graph01.num_edges(), 0 )
        self.assertEqual( graph01.num_undirected_edges(), 0 )
        self.assertEqual( graph01.num_directed_edges(), 0 )


    def test_transfer_from(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03.add_to_graph(graph01, node02, node03, "undirected" )

        graph02 = nlpregex.abs_graph.graph.BaseGraph()

        node04  = nlpregex.abs_graph.node.BaseNode()
        node04.add_to_graph(graph02)

        node05  = nlpregex.abs_graph.node.BaseNode()
        node05.add_to_graph(graph02)

        node06  = nlpregex.abs_graph.node.BaseNode()
        node06.add_to_graph(graph02)

        edge_04_05_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_05_dir.add_to_graph(graph01, node04, node05, "directed" )

        edge_05_06  = nlpregex.abs_graph.edge.BaseEdge()
        edge_05_06.add_to_graph(graph01, node05, node06, "undirected" )

        graph03 = graph01.transfer_from( graph02 )

        self.assertEqual( graph03,              graph02 )

        self.assertEqual( graph01.num_nodes(),  6 );
        self.assertEqual( graph01.num_edges(),  4 );

        self.assertEqual( graph02.num_nodes(),  0 );
        self.assertEqual( graph02.num_edges(),  0 );

        self.assertEqual( node04.graph,         graph01 )

        self.assertEqual( node05.graph,         graph01 )
        self.assertEqual( node06.graph,         graph01 )

        self.assertEqual( edge_04_05_dir.graph, graph01 )
        self.assertEqual( edge_05_06.graph,     graph01 )

        self.assertEqual( node04.out_neighbors()[0], edge_04_05_dir )
        self.assertEqual( node05.in_neighbors() [0], edge_04_05_dir )

        self.assertEqual( node05.undirected_neighbors()[0], edge_05_06 )
        self.assertEqual( node05.undirected_neighbors()[0], edge_05_06 )

        self.assertEqual( edge_04_05_dir.src_node, node04 )
        self.assertEqual( edge_04_05_dir.dst_node, node05 )
        self.assertEqual( edge_05_06.src_node,     node05 )
        self.assertEqual( edge_05_06.dst_node,     node06 )

    def test_find_strong_components_empty(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        list01 = graph01.find_strong_components()

        self.assertEqual( len(list01) , 0 )

    def test_find_strong_components_k1(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        list01 = graph01.find_strong_components()

        self.assertEqual( len( list01      ), 1      )
        self.assertEqual( len( list01[0]   ), 1      )
        self.assertEqual(      list01[0][0] , node01 )


    def test_find_strong_components_3k1(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        list01 = graph01.find_strong_components()

        self.assertEqual( len( list01      ), 3      )

        self.assertEqual( len( list01[0]   ), 1      )
        self.assertEqual(      list01[0][0] , node01 )

        self.assertEqual( len( list01[1]   ), 1      )
        self.assertEqual(      list01[1][0] , node02 )

        self.assertEqual( len( list01[2]   ), 1      )
        self.assertEqual(      list01[2][0] , node03 )


    def test_find_strong_components_k2(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        list01 = graph01.find_strong_components()

        self.assertEqual( len( list01      ), 2      )

        self.assertEqual( len( list01[0]   ), 1      )
        self.assertEqual(      list01[0][0] , node02 )
        self.assertEqual( len( list01[1]   ), 1      )
        self.assertEqual(      list01[1][0] , node01 )

    def test_find_strong_components_p3(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03_dir.add_to_graph(graph01, node02, node03, "directed" )

        list01 = graph01.find_strong_components()

        self.assertEqual( len( list01      ), 3      )

        self.assertEqual( len( list01[0]   ), 1      )
        self.assertEqual(      list01[0][0] , node03 )
        self.assertEqual( len( list01[1]   ), 1      )
        self.assertEqual(      list01[1][0] , node02 )
        self.assertEqual( len( list01[2]   ), 1      )
        self.assertEqual(      list01[2][0] , node01 )


    def test_find_strong_components_k3(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03_dir.add_to_graph(graph01, node02, node03, "directed" )

        edge_03_01_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_01_dir.add_to_graph(graph01, node03, node01, "directed" )

        list01 = graph01.find_strong_components()

        self.assertEqual( len( list01      ), 1      )

        self.assertEqual( len( list01[0]   ), 3      )
        self.assertEqual(      list01[0][0] , node03 )
        self.assertEqual(      list01[0][1] , node02 )
        self.assertEqual(      list01[0][2] , node01 )


    def test_find_strong_components_patten01(self):

        #                      ----->
        # 01 ----> 02 ----> 03        04
        #  ^      / |        | <----- |^
        #  |     /  |        |        ||
        #  |   _/   |        |        ||
        #  | <-     v ---->  v        v|
        # 05 ----> 06       07 <----- 08
        #             <----
        # Strongly connected components
        # {01, 02, 05}
        # {03, 04, 08}
        # {06, 07}

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

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03_dir.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_05_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_05_dir.add_to_graph(graph01, node02, node05, "directed" )

        edge_02_06_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_06_dir.add_to_graph(graph01, node02, node06, "directed" )

        edge_03_04_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_04_dir.add_to_graph(graph01, node03, node04, "directed" )

        edge_03_07_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_07_dir.add_to_graph(graph01, node03, node07, "directed" )

        edge_04_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_03_dir.add_to_graph(graph01, node04, node03, "directed" )

        edge_04_08_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_04_08_dir.add_to_graph(graph01, node04, node08, "directed" )

        edge_05_01_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_05_01_dir.add_to_graph(graph01, node05, node01, "directed" )

        edge_05_06_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_05_06_dir.add_to_graph(graph01, node05, node06, "directed" )

        edge_06_07_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_06_07_dir.add_to_graph(graph01, node06, node07, "directed" )

        edge_07_06_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_07_06_dir.add_to_graph(graph01, node07, node06, "directed" )

        edge_08_04_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_08_04_dir.add_to_graph(graph01, node08, node04, "directed" )

        edge_08_07_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_08_07_dir.add_to_graph(graph01, node08, node07, "directed" )


        list01 = graph01.find_strong_components()

        self.assertEqual( len( list01      ), 3      )
        self.assertEqual( len( list01[0]   ), 2      )
        self.assertEqual(      list01[0][0] , node06 )
        self.assertEqual(      list01[0][1] , node07 )
        self.assertEqual( len( list01[1]   ), 3      )
        self.assertEqual(      list01[1][0] , node08 )
        self.assertEqual(      list01[1][1] , node04 )
        self.assertEqual(      list01[1][2] , node03 )
        self.assertEqual( len( list01[2]   ), 3      )
        self.assertEqual(      list01[2][0] , node05 )
        self.assertEqual(      list01[2][1] , node02 )
        self.assertEqual(      list01[2][2] , node01 )


    def test_find_strong_components_self_loops_multi_edges(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_01_02_dir2  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir2.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03_dir.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_03_dir2  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03_dir2.add_to_graph(graph01, node02, node03, "directed" )

        edge_01_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03_dir.add_to_graph(graph01, node01, node03, "directed" )

        edge_01_03_dir2  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03_dir2.add_to_graph(graph01, node01, node03, "directed" )

        edge_01_01_dir2  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_01_dir2.add_to_graph(graph01, node01, node01, "directed" )

        edge_02_02_dir2  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_02_dir2.add_to_graph(graph01, node02, node02, "directed" )

        edge_03_03_dir2  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_03_dir2.add_to_graph(graph01, node03, node03, "directed" )


        list01 = graph01.find_strong_components()


        self.assertEqual( len( list01      ), 3      )
        self.assertEqual( len( list01[0]   ), 1      )
        self.assertEqual(      list01[0][0] , node03 )
        self.assertEqual( len( list01[1]   ), 1      )
        self.assertEqual(      list01[1][0] , node02 )
        self.assertEqual( len( list01[2]   ), 1      )
        self.assertEqual(      list01[2][0] , node01 )


    def test_find_reachable_nodes_one_node(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        list01 = graph01.find_reachable_nodes(node01)

        self.assertEqual( len( list01), 1)
        self.assertEqual( list01[0], node01)


    def test_find_reachable_nodes_k2(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        list01 = graph01.find_reachable_nodes(node01)

        self.assertEqual( len( list01), 2)
        self.assertEqual( list01[0], node01)
        self.assertEqual( list01[1], node02)

        list02 = graph01.find_reachable_nodes(node02)

        self.assertEqual( len( list02), 1)
        self.assertEqual( list02[0], node02)


    def test_find_reachable_nodes_k2_multi(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_01_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_01_dir.add_to_graph(graph01, node02, node01, "directed" )

        list01 = graph01.find_reachable_nodes(node01)

        self.assertEqual( len( list01), 2)
        self.assertEqual( list01[0], node01)
        self.assertEqual( list01[1], node02)

        list02 = graph01.find_reachable_nodes(node02)

        self.assertEqual( len( list02), 2)
        self.assertEqual( list02[0], node02)
        self.assertEqual( list02[1], node01)


    def test_find_reachable_nodes_k3(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03_dir.add_to_graph(graph01, node02, node03, "directed" )

        edge_03_01_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_03_01_dir.add_to_graph(graph01, node03, node01, "directed" )

        list01 = graph01.find_reachable_nodes(node01)

        self.assertEqual( len( list01), 3)
        self.assertEqual( list01[0], node01)
        self.assertEqual( list01[1], node02)
        self.assertEqual( list01[2], node03)

        list02 = graph01.find_reachable_nodes(node02)

        self.assertEqual( len( list02), 3)
        self.assertEqual( list02[0], node02)
        self.assertEqual( list02[1], node03)
        self.assertEqual( list02[2], node01)

        list03 = graph01.find_reachable_nodes(node03)

        self.assertEqual( len( list03), 3)
        self.assertEqual( list03[0], node03)
        self.assertEqual( list03[1], node01)
        self.assertEqual( list03[2], node02)



    def test_find_reachable_nodes_k3_2(self):

        graph01 = nlpregex.abs_graph.graph.BaseGraph()

        node01  = nlpregex.abs_graph.node.BaseNode()
        node01.add_to_graph(graph01)

        node02  = nlpregex.abs_graph.node.BaseNode()
        node02.add_to_graph(graph01)

        node03  = nlpregex.abs_graph.node.BaseNode()
        node03.add_to_graph(graph01)

        edge_01_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_02_dir.add_to_graph(graph01, node01, node02, "directed" )

        edge_02_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_03_dir.add_to_graph(graph01, node02, node03, "directed" )

        edge_02_02_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_02_02_dir.add_to_graph(graph01, node02, node02, "directed" )

        edge_01_03_dir  = nlpregex.abs_graph.edge.BaseEdge()
        edge_01_03_dir.add_to_graph(graph01, node01, node03, "directed" )

        list01 = graph01.find_reachable_nodes(node01)

        self.assertEqual( len( list01), 3)
        self.assertEqual( list01[0], node01)
        self.assertEqual( list01[1], node02)
        self.assertEqual( list01[2], node03)

        list02 = graph01.find_reachable_nodes(node02)

        self.assertEqual( len( list02), 2)
        self.assertEqual( list02[0], node02)
        self.assertEqual( list02[1], node03)

        list03 = graph01.find_reachable_nodes(node03)

        self.assertEqual( len( list03), 1)
        self.assertEqual( list03[0], node03)


if __name__ == '__main__':
    unittest.main()
