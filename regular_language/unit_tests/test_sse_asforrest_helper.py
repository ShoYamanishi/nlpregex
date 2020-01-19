#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit test helper class for sse_*.py."""

import nlpregex.regular_language.sse_forrest


class test_sse_ASForrest_helper():


    def __init__( self ):
        pass

    def strip( self, spec ):
        out_str = ''
        lines = spec.split('\n')
        for line in lines:
            line = line.strip()
            if line == '':
                continue
            else:
                out_str += line
                out_str += '\n'
        return out_str


    def compare_specs( self, spec1, spec2 ):

        spec1_s = set(self.strip(spec1).split('\n'))
        spec2_s = set(self.strip(spec2).split('\n'))

        return spec1_s == spec2_s


    def construct_ast_from_spec( self, forrest, spec ):
        node_map = {}
        lines = spec.split('\n')
        first = True
        for line in lines:
            line = line.strip()
            if line == '':
                continue
            fields = line.split(':')
            parent_spec = fields[0]

            if parent_spec not in node_map:

                node_map[parent_spec] = self.construct_ast_node_from_spec( parent_spec, forrest )

            parent = node_map[parent_spec]
            
            if first:
                root = parent
                first = False

            if len(fields)==2:
                children_spec = fields[1]
                children_spec = fields[1].split(' ')

                for child_spec in children_spec:
                    child = self.construct_ast_node_from_spec( child_spec, forrest )
                    node_map[child_spec] = child
                    edge = nlpregex.regular_language.sse_forrest.sseASTEdge()
                    edge.add_to_graph(forrest, parent, child, "directed")
        forrest.visit_and_generate_regex( root )
        forrest.visit_and_generate_children_map_for_union( root )

        return root


    def construct_ast_node_from_spec( self, spec, forrest ):

        nodetype, numstr = spec.split('_')

        if nodetype[0] == 'R':
            node = forrest.create_initial_node('r')

        elif nodetype[0] == 'T':
            node = forrest.create_initial_node('t' + nodetype[1:])

        elif nodetype[0] == 'N':
            node = forrest.create_initial_node('n' + nodetype[1:])

        elif nodetype == 'E':
            node = forrest.create_initial_node('e')

        elif nodetype == 'S':
            node = forrest.create_initial_node('s')

        elif nodetype == '|':
            node = forrest.create_initial_node('u')

        elif nodetype == '*':
            node = forrest.create_initial_node('*')

        elif nodetype == '?':
            node = forrest.create_initial_node('?')

        node._original = True
        node.node_id = int(numstr)

        return node


    def get_node( self, forrest, node_id):
        for n in forrest.nodes():
            if n.node_id == node_id:
                return n
        return None


    def display_tree( self, root ):

        children = root.get_children()

        if len(children) == 0:
            return self.display_node( root ) + '\n'

        else:
            return self.visit_and_display_tree( root )


    def visit_and_display_tree( self, n ):
        children = n.get_children()
        if len(children) == 0:
            return ''

        out_str = self.display_node( n )

        first = True

        for c in children:

            if first:            
                out_str += ':'
                first = False

            else:
                out_str += ' '
            out_str += self.display_node( c )

        out_str += '\n'

        for c in children:
            out_str += self.visit_and_display_tree( c )

        return out_str


    def display_node( self, node ):

        out_str = ''

        if node.ast_node_type[0] == 'r':
            out_str += 'R'

        elif node.ast_node_type[0] == 't':
            out_str += ('T' + node.ast_node_type[1:] )

        elif node.ast_node_type[0] == 'n':
            out_str += ('N' + node.ast_node_type[1:] )

        elif node.ast_node_type == 'e':
            out_str += 'E'

        elif node.ast_node_type == 's':
            out_str += 'S'

        elif node.ast_node_type == 'u':
            out_str += '|'

        elif node.ast_node_type == '*':
            out_str += '*'

        elif node.ast_node_type == '?':
            out_str += '?'

        elif node.ast_node_type == 'r':
            out_str += 'R'

        out_str += '_'
        out_str += str(node.node_id)

        return out_str

