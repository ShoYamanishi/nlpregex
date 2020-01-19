#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Grpah Node:"""

from nlpregex.abs_graph import double_link

class BaseNode:

    def __init__( self ):
        self.graph              = None
        self.graph_delg         = None
        self.in_neighbors_list  = double_link.List()
        self.out_neighbors_list = double_link.List()
        self.undirected_neighbors_list = double_link.List()

    def in_neighbors(self):
        return [ n for n in self.in_neighbors_list ]

    def in_degree(self):
        return self.in_neighbors_list.cnt()

    def in_neighbor_head(self):
        if self.in_neighbors_list.head:
            return self.in_neighbors_list.head.elem
        else:
            return None

    def in_neighbor_tail(self):
        if self.in_neighbors_list.tail:
            return self.in_neighbors_list.tail.elem
        else:
            return None


    def out_neighbors(self):
        return [ n for n in self.out_neighbors_list ]


    def out_degree(self):
        return self.out_neighbors_list.cnt()


    def out_neighbor_head(self):
        if self.out_neighbors_list.head:
            return self.out_neighbors_list.head.elem
        else:
            return None


    def out_neighbor_tail(self):
        if self.out_neighbors_list.tail:
            return self.out_neighbors_list.tail.elem
        else:
            return None


    def undirected_neighbors(self):
        return [ n for n in self.undirected_neighbors_list ]


    def undirected_degree(self):
        return self.undirected_neighbors_list.cnt()


    def undirected_neighbor_head(self):
        if self.undirected_neighbors_list.head:
            return self.undirected_neighbors_list.head.elem
        else:
            return None


    def undirected_neighbor_tail(self):
        if self.undirected_neighbors_list.tail:
            return self.undirected_neighbors_list.tail.elem
        else:
            return None


    def all_neighbors(self):
        return self.in_neighbors() + self.out_neighbors() + self.undirected_neighbors()


    def add_to_graph( self, g ):

        self.graph = g
        self.graph_delg = double_link.ElemDelegate(self)
        self.graph.nodes_list.append_tail( self.graph_delg )


    # It returns the removed incident edges in the list of
    # (BaseEdge, ( BaseNode, BaseNode ) )
    #     ^           ^         ^
    #     |           |         |
    #  removed edge   |      dst node                               
    #              src node  
    def remove_from_graph( self ):

        removed_edges = self.all_neighbors()
        
        removed_info = []
        for e in removed_edges:
            old_incident_nodes = e.remove_from_graph()
            removed_info.append( (e, old_incident_nodes) )

        self.graph.nodes_list.remove( self.graph_delg )
        self.graph_delg.clean_refs()
        self.graph_delg = None
        self.graph = None

        return removed_info
