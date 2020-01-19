#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Grpah Edge"""

from nlpregex.abs_graph import double_link

class BaseEdge:

    def __init__(self):

        self.graph      = None
        self.src_node   = None
        self.dst_node   = None
        self.graph_delg = None
        self.src_delg   = None
        self.dst_delg   = None


    def add_to_graph( self, g, src, dst, dir="undirected" ):

        self.directedness = dir
        self.graph_delg   = double_link.ElemDelegate(self)
        self.src_delg     = double_link.ElemDelegate(self)
        self.dst_delg     = double_link.ElemDelegate(self)

        self.graph    = g
        self.src_node = src
        self.dst_node = dst

        if dir == "directed":
            self.src_node. out_neighbors_list.  append_tail( self.src_delg )
            self.dst_node. in_neighbors_list.   append_tail( self.dst_delg )
            self.graph.    directed_edges_list. append_tail( self.graph_delg )

        else:
            self.src_node. undirected_neighbors_list. append_tail( self.src_delg )
            self.dst_node. undirected_neighbors_list. append_tail( self.dst_delg )
            self.graph.    undirected_edges_list.     append_tail( self.graph_delg )


    # the edge is inserted to the adjacency list of src right before the edge specified with src_next_sib.
    # and to the adjacency list of dst right before the edge specified with dst_next_sib.

    def add_to_graph_at_specific_positions( self, g, src, dst, dir="undirected", src_next_sib=None, dst_next_sib=None ):

        self.directedness = dir
        self.graph_delg   = double_link.ElemDelegate(self)
        self.src_delg     = double_link.ElemDelegate(self)
        self.dst_delg     = double_link.ElemDelegate(self)

        self.graph    = g
        self.src_node = src
        self.dst_node = dst

        if dir == "directed":

            next_src_delg = None
            if src_next_sib:
                next_src_delg = src_next_sib.src_delg

            next_dst_delg = None
            if dst_next_sib:
                next_dst_delg = dst_next_sib.dst_delg

            self.src_node. out_neighbors_list.  append_before( self.src_delg, next_src_delg )
            self.dst_node. in_neighbors_list.   append_before( self.dst_delg, next_dst_delg )
            self.graph.    directed_edges_list. append_tail  ( self.graph_delg )

        else:
            next_src_delg = None
            if src_next_sib:
                if src_next_sib.src_node == src:
                    next_src_delg = src_next_sib.src_delg
                else:
                    next_src_delg = src_next_sib.dst_delg

            self.src_node.undirected_neighbors_list.append_before( self.src_delg, next_src_delg )

            next_dst_delg = None
            if dst_next_sib:
                if dst_next_sib.dst_node == dst:
                    next_dst_delg = dst_next_sib.dst_delg
                else:
                    next_dst_delg = dst_next_sib.src_delg

            self.dst_node.undirected_neighbors_list.append_before( self.dst_delg, next_dst_delg )

            self.graph.undirected_edges_list.append_tail( self.graph_delg )


    def remove_from_graph( self ):

        if self.directedness == "directed":

            self.src_node. out_neighbors_list.  remove( self.src_delg )
            self.dst_node. in_neighbors_list.   remove( self.dst_delg )
            self.graph.    directed_edges_list. remove( self.graph_delg )
        else:
            self.src_node. undirected_neighbors_list. remove( self.src_delg )
            self.dst_node. undirected_neighbors_list. remove( self.dst_delg )
            self.graph.    undirected_edges_list.     remove( self.graph_delg )

        self.src_delg.  clean_refs()
        self.dst_delg.  clean_refs()
        self.graph_delg.clean_refs()

        self.src_delg   = None
        self.dst_delg   = None
        self.graph_delg = None

        src = self.src_node
        dst = self.dst_node

        self.src_node = None
        self.dst_node = None
        self.graph    = None        

        return (src, dst)


    def other_node_of( self, n ):

        if n == self.src_node:
            return self.dst_node

        else:
            return self.src_node

        
