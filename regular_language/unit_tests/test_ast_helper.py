#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit test helper class for ast. """

import nlpregex.regular_language.ast


class test_AST_helper():


    def __init__(self):
        pass


    def strip(self, spec):
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


    def compare_specs(self, spec1, spec2):
        spec1_s = set(self.strip(spec1).split('\n'))
        spec2_s = set(self.strip(spec2).split('\n'))
        return spec1_s == spec2_s


    def construct_ast_from_spec(self, spec):

        ast = nlpregex.regular_language.ast.AST()
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
                node_map[parent_spec] = self.construct_ast_node_from_spec(parent_spec, ast)
            parent = node_map[parent_spec]
            
            if first:
                ast.add_root(parent)
                first = False

            if len(fields)==2:
                children_spec = fields[1]
                children_spec = fields[1].split(' ')

                for child_spec in children_spec:
                    child = self.construct_ast_node_from_spec(child_spec, ast)
                    node_map[child_spec] = child
                    edge = nlpregex.regular_language.ast.ASTEdge()
                    edge.add_to_graph(ast, parent, child, "directed")

        return ast


    def construct_ast_node_from_spec(self, spec, ast):

        nodetype, numstr = spec.split('_')

        if nodetype == 'T':
            node = nlpregex.regular_language.ast.ASTNode('terminal', numstr )

        elif nodetype == 'N':
            node = nlpregex.regular_language.ast.ASTNode('nonterminal', numstr )

        elif nodetype == 'E':
            node = nlpregex.regular_language.ast.ASTNode('epsilon', numstr )

        elif nodetype == 'S':
            node = nlpregex.regular_language.ast.ASTNode('sequence', numstr )

        elif nodetype == '|':
            node = nlpregex.regular_language.ast.ASTNode('union', numstr )

        elif nodetype == '*':
            node = nlpregex.regular_language.ast.ASTNode('infinite repeat', numstr )
            node.set_repeat(0, -1)

        elif nodetype == '+':
            node = nlpregex.regular_language.ast.ASTNode('infinite repeat', numstr )
            node.set_repeat(1, -1)

        elif nodetype == '?':
            node = nlpregex.regular_language.ast.ASTNode('finite repeat', numstr )
            node.set_repeat(0, 1)

        elif nodetype[0] == '{':
            nums =  [ int(n) for n in nodetype[1:-1].split(',') ]
            node = nlpregex.regular_language.ast.ASTNode('finite repeat', numstr )
            node.set_repeat(nums[0], nums[1])

        node._original = True
        node.add_to_graph(ast)

        return node


    def display_tree(self, ast):
        if not ast.root:              
            return ''        

        children = ast.root.get_children()

        if len(children) == 0:
            return self.display_node( ast.root ) + '\n'

        else:
            return self.visit_and_display_tree( ast.root )


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

        if node.ast_node_type == 'terminal':
            out_str += 'T'

        elif node.ast_node_type == 'nonterminal':
            out_str += 'N'

        elif node.ast_node_type == 'epsilon':
            out_str += 'E'

        elif node.ast_node_type == 'sequence':
            out_str += 'S'

        elif node.ast_node_type == 'union':
            out_str += '|'

        elif node.ast_node_type == 'infinite repeat':
            if node.repeat_min == 0:
                out_str += '*'
            else:
                out_str += '+'

        elif node.ast_node_type == 'finite repeat':
            if node.repeat_min == 0 and node.repeat_max == 1:
                out_str += '?'
            else:
                out_str += ( '{' + str(node.repeat_min) + ',' + str(node.repeat_max) + '}' )
        out_str += '_'

        if node.content == '':
            out_str += '???'

        else:
            out_str += node.content

        return out_str


    def get_node(self, ast, node_spec):

        nodetype, numstr = node_spec.split('_')

        repeat_min = -1
        repeat_max = -1
        node_ast_type = ''

        if nodetype == 'T':
            node_ast_type = 'terminal'

        elif nodetype == 'N':
            node_ast_type = 'nonterminal'

        elif nodetype == 'E':
            node_ast_type = 'epsilon'

        elif nodetype == 'S':
            node_ast_type = 'sequence'

        elif nodetype == '|':
            node_ast_type = 'union'

        elif nodetype == '*':
            node_ast_type = 'infinite repeat'
            repeat_min = 0
            repeat_max = -1
        elif nodetype == '+':
            node_ast_type = 'infinite repeat'
            repeat_min = 1
            repeat_max = -1
        elif nodetype == '?':
            node_ast_type = 'finite repeat'
            repeat_min = 0
            repeat_max = 1
        elif nodetype[0] == '{':
            node_ast_type = 'finite repeat'
            nums =  [ int(n) for n in nodetype[1:-1].split(',') ]
            repeat_min = nums[0]
            repeat_max = nums[1]
            
        for n in ast.nodes():
            if n.ast_node_type == node_ast_type and numstr == n.content:
                return n
        return None
