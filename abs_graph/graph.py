#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Base Grpah"""

from nlpregex.abs_graph import double_link
from nlpregex.abs_graph import node
from nlpregex.abs_graph import edge

class BaseGraph:

    def __init__( self ):
        self.directed_edges_list   = double_link.List()
        self.undirected_edges_list = double_link.List()
        self.nodes_list            = double_link.List()

    def directed_edges(self):
        return [ e for e in self.directed_edges_list ]

    def num_directed_edges(self):
        return self.directed_edges_list.cnt()

    def undirected_edges(self):
        return [ e for e in self.undirected_edges_list ]

    def num_undirected_edges(self):
        return self.undirected_edges_list.cnt()

    def edges(self):
        return self.directed_edges() + self.undirected_edges()

    def num_edges(self):
        return self.num_directed_edges() + self.num_undirected_edges()

    def nodes(self):
        return [ n for n in self.nodes_list ]

    def num_nodes(self):
        return self.nodes_list.cnt()

    def empty(self):
        for n in self.nodes():
            n.remove_from_graph()

    def transfer_from( self, G ):

        for n in G.nodes():
            G.nodes_list.remove( n.graph_delg )
            n.graph_delg.clean_refs()
            n.graph_delg = None
            n.graph      = None

            n.graph      = self
            n.graph_delg = double_link.ElemDelegate(n)
            self.nodes_list.append_tail( n.graph_delg )

        for e in G.directed_edges():
            G.directed_edges_list.remove( e.graph_delg )
            e.graph_delg.clean_refs()
            e.graph_delg = None
            e.graph      = None

            e.graph      = self
            e.graph_delg = double_link.ElemDelegate(e)
            self.directed_edges_list.append_tail( e.graph_delg )

        for e in G.undirected_edges():
            G.directed_edges_list.remove( e.graph_delg )
            e.graph_delg.clean_refs()
            e.graph_delg = None
            e.graph      = None

            e.graph      = self
            e.graph_delg = double_link.ElemDelegate(e)
            self.undirected_edges_list.append_tail( e.graph_delg )

        return G # empty


    # Tarjan's algorithm with DFS
    # Returns a list of list of BaseNodes
    def find_strong_components(self):

        # Prep
        self.dfs_stack     = []
        self.dfs_index     = 1
        self.sc_components = []       

        for n in self.nodes():
            n.dfs_index    = 0
            n.dfs_lowpt    = 0
            n.dfs_on_stack = False

        # Recurse
        for n in self.nodes():
            if n.dfs_index == 0:
                self.strong_connect(n)

        sc_comps = self.sc_components

        # Cleanup
        for n in self.nodes():
            delattr( n, 'dfs_index'    )
            delattr( n, 'dfs_lowpt'    )
            delattr( n, 'dfs_on_stack' )

        delattr( self, 'dfs_stack'     )
        delattr( self, 'dfs_index'     )
        delattr( self, 'sc_components' )
        return sc_comps


    def strong_connect(self, v):

        v.dfs_index    = self.dfs_index
        v.dfs_lowpt    = self.dfs_index
        v.dfs_on_stack = True

        self.dfs_index = self.dfs_index + 1
        self.dfs_stack.append(v)

        for e in v.out_neighbors():

            w = e.other_node_of(v)

            if w.dfs_index == 0:
                self.strong_connect(w)
                if v.dfs_lowpt > w.dfs_lowpt:
                    v.dfs_lowpt = w.dfs_lowpt 

            elif w.dfs_on_stack:
                if v.dfs_lowpt > w.dfs_index:
                    v.dfs_lowpt = w.dfs_index


        if v.dfs_lowpt == v.dfs_index:

            # Strong component found.
            sc_component_nodes = []

            while True:
                w = self.dfs_stack.pop()
                w.dfs_on_stack = False
                sc_component_nodes.append(w)
                if v == w:
                    break

            self.sc_components.append(sc_component_nodes)


    # Find reachable nodes from n with DFS
    # Returns a list of BaseNodes 
    def find_reachable_nodes(self, v):

        # Prep
        self.reachable      = []       

        for n in self.nodes():
            n.dfs_visited  = False

        # Recurse
        self.find_reachable_nodes_visit(v)

        reachable_nodes = self.reachable

        # Cleanup
        for n in self.nodes():
            delattr( n, 'dfs_visited' )

        delattr( self, 'reachable'  )

        return reachable_nodes


    def find_reachable_nodes_visit(self, v):

        v.dfs_visited = True
        self.reachable.append(v)

        for e in v.out_neighbors():
            w = e.other_node_of(v)
            if not w.dfs_visited:
                self.find_reachable_nodes_visit(w)



class RootedTree(BaseGraph):

    def __init__( self ):
        super().__init__()
        self.root = None

    def add_root(self, r):
        self.root = r


class Tree(BaseGraph):

    def __init__( self ):
        super().__init__()



    
