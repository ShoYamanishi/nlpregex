#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from graphviz import Digraph

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph

from nlpregex.regular_language import fa


# AST: abstract syntax tree.
#      inherited from nlpregex.abs_graph.RootedTree.
#      at each node, the children are specified by
#      the out-neighbors.
#      it uses ASTNode and ASTEdge
#
#      It is constructed by nlpregex.regular_language.lark_parser.LarkParser
#      or any other parsers.
#
# Supported operations
# ---------------------
#
# - AST.clone()      
#
#     returns a self-copy.
#
#
# - AST.flatten_children()
#
#     flatten reduce the depth of the tree by aggregating the
#     consecutive occurrence of sequence or union.
#
#    Ex.      s                       s
#            / \                      |
#           /   \                +--+-+-+--+
#          /     \               |  |   |  |
#         s       u        =>   t1 t2  t3  u  
#        / \     / \                       |
#       t1  s  t4  u                    +--+--+
#          / \    / \                  t4 t5 t6
#         t2 t3  t5 t6
#
#
# - AST.count_phrases()
#
#     at each ASTNode, count the maximum number of phrases the subtree from the node represents.
#     repeat node's count is considered 1.
#     nonterminals are considered to have count 1.
#     if you want to take the subexpression for the nontermnals into counting, then
#     those have to be expanded in the tree.
#
#
# - AST.expand_phrases()
#
#     returns a maximal set of flattened phrases this tree represents.
#     repeat nodes either of finite or infinite, will not be expanded.
#     if the repeat node has only one child and if it is nonterminal, then
#     it will be peresented as "!repeat(<nonterminal>, <min>,<max>).
#     otherwise, it will be given as "!repeat(___exp___, <min>, <max>)".
#
#                     
# - AST.replace_finite_repeat_with_union()
#
#     updates the tree by replacing the finite repeats nodes with 
#     union of repeated sequences.
#
#     ex.) (ab){0,4} => | (ε | ab | abab | ababab | abababab )
#
#
# - AST.expand_nonterminals( nonterminals, trees )
#
#     expand the nonterminals with the corresponding subtrees.
#     if there is cycle, the behavior is undefined.
#
#     @param nonterminals_expanded : list of nonterminals to be expanded
#     @param trees : dictionary {k: nonterminal v: AST}
#     
#     ex.) aa<m>bb<n>cc<p>dd, <m>: ee<n>e, <n>: fff
#         => aaeefffebbfffcceefffedd
#     If there is a self-reference, the behavior is undefined.
#
#
# - AST.generate_fst ( generate_out_tokens=True )
#
#     generates a finiste state automaton from this AST.
#
#     @param generate_out_tokens : Set to True, if you want to decode the input
#                                  with a finite state transducer.
#                                  Set to False, if you just want to accept/reject
#                                  the input with a finite state automaton.                                 
#
#
# - AST.draw( self, tree_name )
#
#     generates a pdf or svg file to visualise this AST.
#     It uses graphviz. The filename for the svg is specified by "tree_name"
#
#     @param tree_name  : output file name
#     @param view_now   : True/False launch viewer immediately
#     @param out_format : 'svg' or 'pdf'. Use 'svg' if window's PDF renders
#                         messes up UTF-8.
#     @param orientagion: 'vertical' or 'horizontal'. top to bottom or left to right.
#                         specifies the direction of 
#                         the tree from the root toward children.
#
#


# ASTNode: 
#
#   ast_node_type:
#       terminal    - terminal symbol
#                     the "content" member represents the string.
#
#       nonterminal - non-terminal symbol
#                     The "content" member represents the string.
#
#       epsilon     - indicates epsilon transiton
#
#       sequence    - concatenation
#
#       union       - selection (pipe)
#
#       infinite repeat
#                   - represents infinite repeat
#                     repeat_min is either 1 or 0.
#                     repeat_max is -1, which means inifinity.
#
#       finite repeat
#                   - represents finite repeat
#                     repeat_min  and repeat_max indicates
#                     the range of repeatition.
#
#   phrase_count:     the maximum number of combinations of the phrases that the subtree from this node represents
#                     the count for the repeat node is considered to be 1.
#
#   text_width:       the length of the text in the regular subexpression this node represents.
#                     it is used to format and indent the expression into a pretty text.
#
#   out_token_pre:    list of out_token for the transducer.
#                     the later in the list, more outword in the transducer
#
#   out_token_post:   list of out_token for the transducer
#                     the later in the list, more outword in the transducer
#
# ASTEdge: directed edge used in AST. it does not carry any information.
#  








# @brief
# make concatenate an item in list1 and an item in list2 
# with the specified delimiter in between.
#
# ex.)
# list1 = { "str1", "str2", "str3" }
# list2 = { "str4", "str5", "str6" }
# delim = " "
#
# return:
# { "str1 str4", "str1 str5", "str1 str6",
#   "str2 str4", "str2 str5", "str2 str6",
#   "str3 str4", "str3 str5", "str3 str6" }
#
# if both are empty, it returns an empty list.
# if either is empty, then it returns the other.
# when concatenating two strings, if either of them are empty, 
# then no delimiter is inserted.
# i.e.) '' + 'a'  => 'a' (not '<delim>a' )

def cross_product ( list1, list2, delim ):

    list_out = []

    if len(list1) == 0:
        return list2

    elif len(list2) == 0:
        return list1

    else:
        for e1 in list1:
            for e2 in list2:
                if e1 != '':
                    if e2 != '':
                        list_out.append( e1 + delim + e2 )
                    else:
                        list_out.append( e1 )
                else:
                    if e2 != '':
                        list_out.append( e2 )
                    else:
                        list_out.append( '' )

        return list_out



# @brief create a sequence node over two children
#
# @param left_child:  left child
# @param right_child: right child
# @param ast:         AST to which this node is added.
#
# @return new node created.
def create_sequence_subtree( left_child, right_child, ast ):

    new_node = nlpregex.regular_language.ast.ASTNode( 'sequence', '' )
    new_node.add_to_graph( ast )

    # left first, and then right. order is important

    left_edge  = nlpregex.regular_language.ast.ASTEdge()
    left_edge.add_to_graph(  ast, new_node, left_child,  dir="directed" )

    right_edge = nlpregex.regular_language.ast.ASTEdge()
    right_edge.add_to_graph( ast, new_node, right_child, dir="directed" )

    return new_node



# @brief create a union node over two children
#
# @param left_child:  left child
# @param right_child: right child
# @param ast:         AST to which this node is added.
#
# @return new node created.
def create_union_subtree( left_child, right_child, ast ):

    new_node = nlpregex.regular_language.ast.ASTNode( 'union', '' )
    new_node.add_to_graph( ast )

    # left first, and then right. order is important

    left_edge  = nlpregex.regular_language.ast.ASTEdge()
    left_edge.add_to_graph(  ast, new_node, left_child,  dir="directed" )

    right_edge = nlpregex.regular_language.ast.ASTEdge()
    right_edge.add_to_graph( ast, new_node, right_child, dir="directed" )

    return new_node




# @brief create a finite repeat node over a child.
#
# @param child_node: child node
# @param repeat_min: minimum repetition
# @param repeat_max: maximum repetition
# @param ast:        AST to which this node is added.
#
# @return new node created.
def create_finite_repeat_subtree( child_node, repeat_min, repeat_max, ast ):

    new_node = nlpregex.regular_language.ast.ASTNode( 'finite repeat', '' )
    new_node.add_to_graph( ast )

    new_node.set_repeat( repeat_min, repeat_max )

    new_edge = nlpregex.regular_language.ast.ASTEdge()
    new_edge.add_to_graph( ast, new_node, child_node, dir="directed" )

    return new_node


# @brief create a infinite repeat node over a child.
#
# @param child_node: child node
# @param rtype:      'PLUS' or 'STAR'
# @param ast:        AST to which this node is added.
#
# @return new node created.
def create_infinite_repeat_subtree( child_node, rtype, ast ):

    new_node = nlpregex.regular_language.ast.ASTNode( 'infinite repeat', '' )
    new_node.add_to_graph( ast )

    if rtype == 'STAR':
        new_node.set_repeat( 0, -1 )

    elif rtype == 'PLUS':
        new_node.set_repeat( 1, -1 )

    new_edge = nlpregex.regular_language.ast.ASTEdge()
    new_edge.add_to_graph( ast, new_node, child_node, dir="directed" )

    return new_node


class ASTNode(nlpregex.abs_graph.node.BaseNode):


    def __init__( self, ast_node_type, content):

        super().__init__()

        self.ast_node_type  = ast_node_type 
        self.content        = content
        self.repeat_min     = 1
        self.repeat_max     = 1
        self.phrase_count   = 1
        self.text_width     = 0
        self.out_token_pre  = [] # later in the list, the closer to the root of AST
        self.out_token_post = [] # later in the list, the closer to the root of AST


    def set_repeat( self, b, e ):
        self.repeat_min = b
        self.repeat_max = e


    def append_out_token_pre(self, t):
        self.out_token_pre.append(t)


    def append_out_token_post(self, t):
        self.out_token_post.append(t)


    def get_children( self ):
        return [ e.other_node_of( self ) for e in  self.out_neighbors() ]


    def get_parent( self ):
        if len(self.in_neighbors())==1:
            return self.in_neighbors()[0].other_node_of( self )
        else:
            return None


    # @virtual
    # @brief deep copies the contents from the other node
    def copy_from( self, n ):
        self.ast_node_type  = n.ast_node_type
        self.content        = n.content
        self.repeat_min     = n.repeat_min
        self.repeat_max     = n.repeat_max
        self.phrase_count   = n.phrase_count
        self.text_width     = n.text_width
        self.out_token_pre  = list( n.out_token_pre  )
        self.out_token_post = list( n.out_token_post )


    # @virtual
    # @brief reset the values of the node, keeping it in the tree
    def reset( self ):
        self.ast_node_type  = '' # Must be filled immediately after this call
        self.content        = ''
        self.repeat_min     = 1
        self.repeat_max     = 1
        self.phrase_count   = 1
        self.text_width     = 0
        self.out_token_pre  = []
        self.out_token_post = []


    # @virtual
    # @brief returns true if this node can be removed to flatten the tree.
    def can_be_flattened(self):
        return len(self.out_token_pre) == 0 and len(self.out_token_post) == 0


    # @virtual
    # @brief
    # returns a string if the node has other string to be added before and after
    # for generating expanded phrases.
    #
    # @param id: unique number assigned to each invocation of a pair of those calls
    #            the callee can use this to emit unique string.
    def attribute_for_expansion_before( self, id ):
        if len(self.out_token_pre) > 0:
            rev = list( reversed(self.out_token_pre) )
            content = ' '.join( rev )
            return '[ ' + content + ' ]'
        else:
            return ''

    def attribute_for_expansion_after ( self, id ):
        if len(self.out_token_post) > 0:
            content = ' '.join(self.out_token_post)
            return '[ ' + content + ' ]'
        else:
            return ''


    # @virtual
    # @brief
    # returns a string if the node has other string to be added before and after
    # for emiiting formatted rules.
    def prologue_for_formatted_text(self):
        if len(self.out_token_pre) > 0:
            rev = list( reversed(self.out_token_pre) )
            content = ' '.join( rev )
            return '[ ' + content + ' ]'
        else:
            return ''

    def epilogue_for_formatted_text(self):
        if len(self.out_token_post) > 0:
            content = ' '.join(self.out_token_post)
            return '[ ' + content + ' ]'
        else:
            return ''


    # @virtual
    # @brief
    # returns a list of extra out_tokens for the epsilon transitions 
    #         prepended and appended to the main transition.
    #
    def extra_epsilon_nodes_before (self):

        rev = list( reversed( self.out_token_pre ) )

        return ' '.join( rev )

    def extra_epsilon_nodes_after (self):

        return ' '.join( self.out_token_post )


    # @virtual
    # @brief
    # returns the in_token and out_token for the main transition
    def node_content_for_fst_main(self, id):
        return (self.content, '')


    # @virtual
    # @brief
    # saves the attributes of this node to be removed.
    # used when a nonterminal node is replaced with a subtree.
    # saved attributes are merged to the replacing node
    #
    # @return attributes saved
    def save_attributes(self):
        return ( self.out_token_pre, self.out_token_post )

    # @virtual
    # @brief
    # merges saved attributes to this node.
    # used when a nonterminal node is replaced with a subtree.
    #
    # @param attributes returned by saved_attributes
    def merge_attributes(self, saved_attrib):

        for t in saved_attrib[0]:
            self.out_token_pre.append(t)

        for t in saved_attrib[1]:
            self.out_token_post.append(t)


    # @virtual
    # @brief
    # returns a string to be used a a node label for graphviz
    # 
    # @param show_attributes : display attributes.
    #
    # @return (string to be shown, True/False) 
    #         The 2nd param shows if the children must be 
    #         visited or not.
    def generate_string_for_drawing(self, show_attributes):

        label_out = ""
        should_visit_children = True
        if self.ast_node_type == 'terminal':
            label_out += self.content.replace('"','')

        elif self.ast_node_type == 'nonterminal':
            label_out += self.content.replace('"','')

        elif self.ast_node_type == 'epsilon':
            label_out += "ε"

        elif self.ast_node_type == 'sequence':
            if self.are_children_all_terminals(show_attributes):
                should_visit_children = False
                label_out += self.aggregate_child_labels()
            else:
                label_out += "SEQ"

        elif self.ast_node_type == 'union':
            label_out += "|"

        elif self.ast_node_type == 'infinite repeat':
            if self.repeat_min == 0:
                label_out += "*"
            else:
                label_out += "+"

        elif self.ast_node_type == 'finite repeat':
            label_out += ( "{ " + str(self.repeat_min) + ", " + str(self.repeat_max) + " }" )

        if self.phrase_count > 1:
            label_out += ( ' (' +  str(self.phrase_count) + ')' )

        if show_attributes:

            prologue = self.prologue_for_formatted_text()
            if prologue != '':
                label_out = prologue + ' ' + label_out 

            epilogue = self.epilogue_for_formatted_text()
            if epilogue != '':
                label_out = label_out + ' ' + epilogue

        return '"' + label_out + '"', should_visit_children


    # @brief subroutine for generate_string_for_drawing()
    #        if there is no children, return False.
    # @param show_attributes : display attributes.
    def are_children_all_terminals(self, show_attributes):
        
        children  = [ e.other_node_of( self ) for e in self.out_neighbors() ]

        if len(children) == 0:
            return False

        for c in children:
            if c.ast_node_type != 'terminal':
                return False

            if show_attributes:
                attr_str = c.prologue_for_formatted_text() + c.epilogue_for_formatted_text()
                if attr_str != '':
                    return False

        return True


    # @brief subroutine for generate_string_for_drawing()
    def aggregate_child_labels(self):

        out_str = ''
        
        children  = [ e.other_node_of( self ) for e in self.out_neighbors() ]
        first = True
        for c in children:
            if first:
                first = False
            else:
                out_str += ' '
            
            out_str += c.content.replace('"','')

        return out_str


    # @brief diag string
    def __str__(self):

        out_str = "Type: ["
        out_str += self.ast_node_type
        out_str += "] Token: ["
        out_str += self.content
        out_str += "] Repeat: ("
        out_str += str(self.repeat_min)
        out_str += ", "
        out_str += str(self.repeat_max)
        out_str += ") Count: "
        out_str += str (self.phrase_count)
        out_str += " Text Width: "
        out_str += str (self.text_width)
        out_str += " Out Token Pre: ["
        out_str += self.prologue_for_formatted_text()
        out_str += "] Out Token Post: ["
        out_str += self.epilogue_for_formatted_text()
        out_str += "]"
        return out_str






class ASTEdge(nlpregex.abs_graph.edge.BaseEdge):

    def __init__(self):
        super().__init__()







class AST(nlpregex.abs_graph.graph.RootedTree):


    def __init__(self):
        super().__init__()
        self.node_attribute_id_next = 0



    # @public
    # @brief incidence oder preserving clone
    def clone( self ):

        gclone = AST();

        node_id = 1

        id_to_clone_node = {}

        for n in self.nodes():

            nclone = type(n)("","") # subclass of ASTNode
            nclone.copy_from(n)

            n.node_id      = node_id
            nclone.node_id = node_id

            id_to_clone_node[node_id] = nclone

            nclone.add_to_graph(gclone)

            if n == self.root:
                gclone.add_root(nclone)

            node_id += 1


        for n in self.nodes():

            src_clone = id_to_clone_node[n.node_id]

            for c in [ e.other_node_of(n) for e in n.out_neighbors() ]:

                dst_clone = id_to_clone_node[c.node_id] 

                eclone = ASTEdge()                
                eclone.add_to_graph( gclone, src_clone, dst_clone, "directed" )

        for n in self.nodes():
            delattr( n, 'node_id' )

        for n in gclone.nodes():
            delattr( n, 'node_id' )


        return gclone



    ########################################
    #                                      #
    #         remove & clone subtree       #
    #                                      #
    ########################################

    # @public
    # @brief remove subtree from this AST.
    # @param root: root of the subtree to be removed
    def remove_subtree( self, root ):

        self.visit_and_remove_subtree( root )
        if root == self.root:
            self.root = None


    # @brief recursive subroutine of remove_subtree
    def visit_and_remove_subtree( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        for c in children:
            self.visit_and_remove_subtree( c )
        n.remove_from_graph()


    # @public
    # @brief creates a clone of the subtree from this AST.
    # @param root: root of the subtree
    # @return cloned subtree
    def clone_subtree(self, root):

        subtree_nodes = self.visit_and_gather_subtree_nodes( root )

        g_clone = AST();

        node_id = 1
        id_to_original_node = {}
        id_to_clone_node    = {}
        for n_org in subtree_nodes:

            n_clone = type(n_org)("","") # subclass of ASTNode()
            n_clone.copy_from(n_org)

            n_org.node_id   = node_id
            n_clone.node_id = node_id

            id_to_clone_node   [node_id] = n_clone
            id_to_original_node[node_id] = n_org

            n_clone.add_to_graph(g_clone)

            if n_org == root:
                g_clone.add_root(n_clone)

            node_id += 1

        self.visit_and_clone_edges(root, g_clone, id_to_clone_node)

        org_nodes = [id_to_original_node[k]  for k in id_to_original_node ]

        for n in org_nodes:
            delattr( n, 'node_id' )

        for n in g_clone.nodes():
            delattr( n, 'node_id' )


        return g_clone


    # @brief recursive subroutine of clone_subtree
    def visit_and_gather_subtree_nodes(self, n):
        node_list = [n]
        children  = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            node_list += self.visit_and_gather_subtree_nodes(c)

        return node_list


    # @brief recursive subroutine of clone_subtree
    def visit_and_clone_edges(self, n, gclone, id_to_clone_node):

        for e in n.out_neighbors():
            src_clone = id_to_clone_node[e.src_node.node_id]
            dst_clone = id_to_clone_node[e.dst_node.node_id]

            eclone = ASTEdge()                
            eclone.add_to_graph( gclone, src_clone, dst_clone, "directed" )
        
        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        for c in children:
            self.visit_and_clone_edges(c, gclone, id_to_clone_node)


    # @brief keeping the node n at its current position, copy
    #        the contents of the only child into n, remove the child
    #        and pull up grand children under n.
    def pullup_only_child(self, n):

        child_nodes = [ e.other_node_of( n ) for e in n.out_neighbors() ]
        c  = child_nodes[0]

        grand_child_nodes = [ e.other_node_of( c ) for e in c.out_neighbors() ]


        # Migrate all the contents of c to n
        saved_attrib = n.save_attributes()
        n.copy_from( c )
        n.merge_attributes( saved_attrib )

        c.remove_from_graph()

        for gc in grand_child_nodes:

            e = ASTEdge()
            e.add_to_graph( self, n, gc, "directed" )


    ########################################
    #                                      #
    #           clean_epsilon()            #
    #                                      #
    ########################################


    # @public
    # @brief eliminate epsilon node from the tree
    #       
    # case n is a sequence
    #       - remove child epsilons
    #       - if there is no child, remove n
    #       - if there is only one child, pull up the child to n.
    #          
    # case n is a union    
    #       - remove child epsilons
    #       - if there is no child, remove n
    #       - if epsilon is removed
    #           - if there is only one child, update n to {0,1}
    #           - otherwise, update n to {0,1}  create new only child c
    #             make c to union, and put the child of n under c.
    #       - if epsilon is not removed
    #           - if there is only one child, pull up the child to n
    #
    # case n is a finite repeat
    #       - remove child epsilon
    #       - if there is no child, remove n
    #       - if n is {1,1}, pull up c to n.
    #       - if n is {x,y} and c is {1,1}, pull up c to n and mekt it to {x,y}
    #       - if n is {0,1} and c is {1,x}, pull up c to n and make it to {0,x}
    #       - if n is {1,x} and c is {0,1}, pull up c to n and make it to {0,x}
    #       - if n is {0,1} and c is + pull up c to n and make it *
    #       - if n is {0,1} and c is * pull up c to n.
    #
    # case n is a infinite repeat
    #       - remove child epsilon
    #       - if there is no child, remove n
    #       - if c is {0,1}, pull up c to n and make it to *
    #       - if n is *, and c is *, pull up c to n
    #       - if n is +, and c is *, pull up c to n
    #       - if + is *, and c is +, pull up c to n and make it to *
    #       - if + is +, and c is +, pull up c to n
    def clean_epsilon(self):
        if self.root:
            if self.root.ast_node_type == 'epsilon':
                self.root.remove_from_graph()
                self.root = None
            else:
                self.visit_and_clean_epsilon( self.root )


    def visit_and_clean_epsilon(self, n):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:

            self.visit_and_clean_epsilon( c )

        epsilon_removed = False
        for c in children:
            if c.ast_node_type == 'epsilon':
                c.remove_from_graph()
                epsilon_removed = True

        updated_edges    = [ e for e in n.out_neighbors() ] # Makind a copy
        updated_children = [ e.other_node_of( n ) for e in updated_edges ]

        if n.ast_node_type == 'sequence':
            self.clean_epsilon_sequence( n, updated_children )

        elif n.ast_node_type == 'union':
            self.clean_epsilon_union( n, updated_children, epsilon_removed )

        elif n.ast_node_type == 'finite repeat':
            self.clean_epsilon_finite_repeat( n, updated_children )

        elif n.ast_node_type == 'infinite repeat':
            self.clean_epsilon_infinite_repeat( n, updated_children )


    # @brief subroutine of visit_and_clean_epsilon()
    def clean_epsilon_sequence(self, n, children):

        if len(children) == 0:
            if n == self.root:
                self.root = None
            n.remove_from_graph()

        elif len(children) == 1:
            self.pullup_only_child(n)


    # @brief subroutine of visit_and_clean_epsilon()
    def clean_epsilon_union( self, n, children, epsilon_removed ):

        if len(children) == 0:
            if n == self.root:
                self.root = None
            n.remove_from_graph()

        elif len(children) == 1 and not epsilon_removed:
            self.pullup_only_child(n)

        elif len(children) == 1 and epsilon_removed:
            n.ast_node_type = 'finite repeat'
            n.repeat_min    = 0
            n.repeat_max    = 1

        elif epsilon_removed:
            n_edges     = n.out_neighbors()
            for e in n_edges:
                e.remove_from_graph()

            new_child = type(n)("finite repeat", "") # subclass of ASTNode()
            new_child.copy_from(n)
            n.reset()
            n.ast_node_type = 'finite repeat'
            n.repeat_min    = 0
            n.repeat_max    = 1

            e_child = ASTEdge()
            e_child.add_to_graph( self, n, new_child, dir="directed" )

            for c in children:
                e = ASTEdge()
                e.add_to_graph( self, new_child, c, dir="directed" )

            # Re-clean under n after changing n to finit repeat
            self.visit_and_clean_epsilon( n )


    # @brief subroutine of visit_and_clean_epsilon()
    def clean_epsilon_finite_repeat( self, n, children ):

        if len(children) == 0:
            if n == self.root:
                self.root = None

            n.remove_from_graph()

        else:
            c = children[0]

            if n.repeat_min == 1 and  n.repeat_max == 1:
                self.pullup_only_child(n)


            elif c.ast_node_type == 'finite repeat' and c.repeat_min == 1 and c.repeat_max == 1:
                n_repeat_min = n.repeat_min
                n_repeat_max = n.repeat_max
                self.pullup_only_child(n)
                n.repeat_min = n_repeat_min
                n.repeat_max = n_repeat_max


            elif c.ast_node_type == 'finite repeat' and c.repeat_min == 0 and c.repeat_max == 1 and n.repeat_min == 0:
                n_repeat_max = n.repeat_max
                self.pullup_only_child(n)
                n.repeat_max = n_repeat_max

            elif c.ast_node_type == 'finite repeat' and n.repeat_min == 0 and n.repeat_max == 1 and c.repeat_min == 0:
                self.pullup_only_child(n)


            elif c.ast_node_type == 'finite repeat' and c.repeat_min == 0 and c.repeat_max == 1 and n.repeat_min == 1:
                n_repeat_max = n.repeat_max
                self.pullup_only_child(n)
                n.repeat_max = n_repeat_max
                n.repeat_min = 0


            elif c.ast_node_type == 'finite repeat' and n.repeat_min == 0 and n.repeat_max == 1 and c.repeat_min == 1:
                self.pullup_only_child(n)
                n.repeat_min = 0

            elif c.ast_node_type == 'infinite repeat' and c.repeat_min == 1 and  n.repeat_min == 1:
                self.pullup_only_child(n)


            elif c.ast_node_type == 'infinite repeat' and c.repeat_min == 0 and  n.repeat_min == 1:
                self.pullup_only_child(n)
                n.repeat_min = 0


            elif c.ast_node_type == 'infinite repeat' and c.repeat_min == 1 and  n.repeat_min == 0:
                self.pullup_only_child(n)
                n.repeat_min = 0


            elif c.ast_node_type == 'infinite repeat' and c.repeat_min == 0 and  n.repeat_min == 0:
                self.pullup_only_child(n)



    # @brief subroutine of visit_and_clean_epsilon()
    def clean_epsilon_infinite_repeat( self, n, children ):

        if len(children) == 0:
            if n == self.root:
                self.root = None
            n.remove_from_graph()

        else:
            c = children[0]

            if c.ast_node_type == 'finite repeat' and c.repeat_min == 1 and n.repeat_min == 0:
                self.pullup_only_child(n)
                n.ast_node_type = 'infinite repeat'
                n.repeat_min    = 0


            elif c.ast_node_type == 'finite repeat' and c.repeat_min == 0 and n.repeat_min == 0:
                self.pullup_only_child(n)
                n.ast_node_type = 'infinite repeat'


            elif c.ast_node_type == 'finite repeat' and c.repeat_min == 1 and n.repeat_min == 1:
                self.pullup_only_child(n)
                n.ast_node_type = 'infinite repeat'


            elif c.ast_node_type == 'finite repeat' and c.repeat_min == 0 and n.repeat_min == 1:
                self.pullup_only_child(n)
                n.ast_node_type = 'infinite repeat'


            elif c.ast_node_type == 'infinite repeat':
                new_min = min(n.repeat_min, c.repeat_min)
                self.pullup_only_child(n)
                n.repeat_min = new_min


    ########################################
    #                                      #
    #           flatten_children()         #
    #                                      #
    ########################################


    # @public
    # @brief try flattening the tree by aggregating the chain
    #        of the same type of nodes into a single layer.
    #        used for union and sequence.
    def flatten_children( self ):
        if self.root:
            self.visit_and_flatten_children( self.root )


    # @brief recursive subroutine used by flatten_children
    def visit_and_flatten_children( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:

            self.visit_and_flatten_children( c )

        if n.ast_node_type == 'union' or n.ast_node_type == 'sequence':

            same_type_found = False

            for c in children:
                
                if c.ast_node_type == n.ast_node_type and c.can_be_flattened():
                    same_type_found = True

            if same_type_found:

                self.replace_child_with_grand_children( n )


    # @brief replace the children with grandchildren keeping the order
    #        recursive subroutine used by flatten_children
    # 1.
    #             (n)
    #              |
    #     +--------+-------+  <= incident_edges (to be removed)
    #     c        c       c  
    #    /|\      /|\     /|\
    #  g1 g2 g3 g4 g5 g6 g7 g8 g9
    #
    #
    # 2.
    #             (n)
    #
    #   [ c        c       c ] <= adjacent_nodes_of_c (to be removed)
    #    /|\      /|\     /|\  <= incident_edges_of_c (to be removed)
    #  g1 g2 g3 g4 g5 g6 g7 g8 g9
    #
    #
    # 3.
    #             (n)
    #
    # [g1 g2 g3 g4 g5 g6 g7 g8 g9] <= new_children
    #
    # 4.
    #             (n)
    #   +--+--+--+-+-+--+--+--+--+
    #   |  |  |  |   |  |  |  |  |
    #  g1 g2 g3 g4  g5 g6 g7 g8 g9
    #
    def replace_child_with_grand_children( self, n ):

        incident_edges = [ e for e in  n.out_neighbors() ]
        adjacnt_nodes  = [ e.other_node_of( n ) for e in incident_edges ]

        for e in incident_edges:        
            e.remove_from_graph()

        new_children = []

        for c in adjacnt_nodes:

            if c.ast_node_type == n.ast_node_type:
                
                incident_edges_of_c = [ e for e in  c.out_neighbors() ]
                adjacnt_nodes_of_c  = [ e.other_node_of( c ) for e in incident_edges_of_c ]

                for e in incident_edges_of_c:
                    e.remove_from_graph()

                c.remove_from_graph()
                new_children = new_children + adjacnt_nodes_of_c

            else:
                new_children.append(c)

        for c in new_children:
            new_edge = ASTEdge()
            new_edge.add_to_graph( n.graph, n, c, dir="directed" )


    ########################################
    #                                      #
    #   replace_fixed_repeat_with_union()  #
    #                                      #
    ########################################


    # @public
    # @brief replace fixed repetition node with a union of 
    #        repeated sequences other than {0,1}.
    #        this must be done  before generating FST.
    #        otherwise, the finite repeat nodes are treated as
    #        inifinite repeat in FST
    def replace_finite_repeat_with_union( self ):
        if self.root:
            self.visit_and_replace_fixed_repeat_with_union( self.root )
            self.clean_epsilon()
            self.flatten_children()

    # @brief recursive subroutine of replace_fixed_repeat_with_union()
    def visit_and_replace_fixed_repeat_with_union( self, n ):

        if n.ast_node_type != 'finite repeat':
            return

        if n.repeat_min == 0 and n.repeat_max == 1:
            return


        if n.repeat_min == 1 and n.repeat_max == 1:
            # removed by clean_epsilon()
            return


        if n.repeat_min == 0 and n.repeat_max == 0:
            self.remove_subtree(n)
            if n == self.root:
                self.root = None
            return


        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:

            self.visit_and_replace_fixed_repeat_with_union( c )

        if n.ast_node_type == 'finite repeat' and n.repeat_max > 1:

            original_repeat_min = n.repeat_min
            
            c0 = children[0]

            new_sequences = []

            for i in range ( max( n.repeat_min, 1 ), n.repeat_max + 1 ):
                seq = self.create_sequence_of_repeated( c0, i )
                new_sequences.append(seq)

            for c in children:
                self.remove_subtree(c)

            if len(new_sequences) == 0:
                # Make this a dead node.
                n.ast_node_type = 'epsilon'
                n.content       = ''

            elif len(new_sequences) == 1:
                seq_root = new_sequences[0]
                if original_repeat_min == 0:
                    # replace n with {0,1}
                    n.repeat_min = 0
                    n.repeat_max = 1
                    e = ASTEdge()
                    e.add_to_graph( self, n, seq_root, dir="directed" )

                else:                     
                    # replace n with  new_sequences[0]
                    new_children = [ e.other_node_of( seq_root ) for e in seq_root.out_neighbors() ]

                    n.copy_from(seq_root)
                    seq_root.remove_from_graph()

                    for c in new_children:
                        e = ASTEdge()
                        e.add_to_graph( self, n, c, dir="directed" )

            else:

                if original_repeat_min == 0:
                    # replace n with {0,1}
                    n.repeat_min = 0
                    n.repeat_max = 1

                    n_child = type(n)("union", "") # subclass of ASTNode()
                    e_child = ASTEdge()
                    e_child.add_to_graph( self, n, n_child, dir="directed" )
                    for c in new_sequences:
                        e = ASTEdge()
                        e.add_to_graph( self, n_child, c, dir="directed" )

                else:
                    n.ast_node_type = 'union'
                    n.content = ''
                    n.repeat_min == 1
                    n.repeat_max == 1
                    for c in new_sequences:
                        e = ASTEdge()
                        e.add_to_graph( self, n, c, dir="directed" )


    # @brief subroutine of visit_and_replace_fixed_repeat_with_union()
    def create_sequence_of_repeated( self, node, num ):

        if num == 0:
            n_new = type(node)("epsilon", "") # subclass of ASTNode()
            n_new.add_to_graph(self)
            return n_new

        if num == 1:
            g = self.clone_subtree(node)
            n_new = g.root
            self.transfer_from( g )
            return n_new

        else:
            n_new = type(node)("sequence", "") # subclass of ASTNode()
            n_new.add_to_graph(self)
            for i in range (0, num):
                g = self.clone_subtree(node)
                c = g.root
                self.transfer_from( g )
                e_new = ASTEdge()
                e_new.add_to_graph( self, n_new, c, dir="directed" )

            return n_new


    ########################################
    #                                      #
    #         expand_nonterminals()        #
    #                                      #
    ########################################


    # @public
    # @brief returns the set of names of nonterminals found in the tree.
    def find_dependent_nonterminals( self ):
        if self.root:
            return self.visit_and_find_dependent_nonterminals( self.root )
        else:
            return set()


    # @brief recursive subroutine of find_dependent_nonterminals().
    def visit_and_find_dependent_nonterminals( self, n ):

        S = set()

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            S_returned = self.visit_and_find_dependent_nonterminals( c )
            S = S.union( S_returned )

        if n.ast_node_type == 'nonterminal':
            S.add(n.content)

        return S


    # @public
    # @brief expand the nonterminals with the corresponding subtrees.
    #        if there is cycle, the behavior is undefined.
    #
    # @param nonterminals_expanded : list of nonterminals expanded
    # @param trees : dictionary {k: nonterminal v: AST}

    def expand_nonterminals( self, nonterminals_expanded, trees ):

        if self.root:

            self.expand_nonterminals_root( nonterminals_expanded, trees )
            self.visit_and_expand_nonterminals( self.root, nonterminals_expanded, trees )


    # @brief subroutine of expand_nonterminal()
    #        special case where the root itself is the nonterminal to be replaced.
    def expand_nonterminals_root( self, nonterminals_expanded, trees ): 

        if self.root:

            r_content = self.root.content

            if self.root.ast_node_type == 'nonterminal' and r_content in nonterminals_expanded:

                if r_content in trees:
                    saved_attrib = self.root.save_attributes()
                    self.root.remove_from_graph()
                    t = trees[ r_content ].clone()
                    self.root = t.root
                    self.transfer_from(t)
                    t.root.merge_attributes(saved_attrib)
                    self.expand_nonterminals(nonterminals_expanded, trees )


    # @brief recursive subroutine of expand_nonterminal()
    def visit_and_expand_nonterminals( self, n, nonterminals_expanded, trees ):

        incident_edges = [ e for e in  n.out_neighbors() ]
        adjacent_nodes = [ e.other_node_of( n ) for e in incident_edges ]

        for i in range(0,len(incident_edges)):

            c = adjacent_nodes[i]

            if c.ast_node_type == 'nonterminal':

                if c.content in nonterminals_expanded:
                    if c.content in trees:
                        next_edge = None
                        if i < len(incident_edges) - 1:
                            next_edge = incident_edges[i+1]
                        saved_attrib = c.save_attributes()
                        c.remove_from_graph()
                      
                        t = trees[ c.content ].clone()
                        c_new = t.root
                        self.transfer_from(t)
                        c_new.merge_attributes(saved_attrib)
                        e_new = ASTEdge()
                        e_new.add_to_graph_at_specific_positions( self, n, c_new, "directed", next_edge, None )

        # Refresh the incident and adjacent features.
        incident_edges = [ e for e in  n.out_neighbors() ]
        adjacent_nodes = [ e.other_node_of( n ) for e in incident_edges ]

        for i in range(0,len(incident_edges)):
            c = adjacent_nodes[i]
            self.visit_and_expand_nonterminals( c, nonterminals_expanded, trees )



    ########################################
    #                                      #
    #        emit_formatted_text()         #
    #                                      #
    ########################################


    # @public
    # @brief emit formatted rule of this AST
    #        the tree must be epsilon-cleaned.
    #
    # @param width_hint: hint for the maximum width at which 
    #                    the text is folded with carriage return
    #                    0 for single line formatting.
    # @param indent:     indent width for each depth
    # @param print_attr: True/False
    def emit_formatted_text(self, width_hint, indent, print_attr=True):
        depth = self.calculate_text_width(print_attr)

        if self.root:
            return self.visit_and_emit_formatted_text( self.root, depth, width_hint, indent, print_attr )

        else:
            return ''


    # @brief calculate the text width of subtree at each node.
    def calculate_text_width(self, print_attr):
        
        if self.root:
            return self.visit_and_calculate_text_width( self.root, print_attr )
        else:
            return 0


    # @brief recursive subroutine of calculate_text_width()
    #        this is a bottom-up accummulative process.
    #        the width is stored to ASTNode.text_width.
    def visit_and_calculate_text_width( self, n, print_attr ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        width = 0

        if n.ast_node_type == 'union':

            width += len('()')
            width += ( max(0, len(children) - 1) * len(' | ') )

        elif n.ast_node_type == 'sequence':

            width += ( max(0, len(children) - 1) * len(' ') )

        elif n.ast_node_type == 'terminal':
            width += len(n.content)

        elif n.ast_node_type == 'nonterminal':
            width += len(n.content)

        elif n.ast_node_type == 'finite repeat':

            width += len( '(  ){ ' + str(n.repeat_min)  + ', ' + str(n.repeat_max) + ' }' )

        elif n.ast_node_type == 'infinite repeat':

            width += len( '(  )*' )

        if print_attr:
            width += len( self.add_prologue_and_epilogue( n, '', True ) )

        for c in children:
            width += self.visit_and_calculate_text_width( c, print_attr )

        n.text_width = width

        return width 


    # @brief subroutine to visit_and_emit_formatted_text()
    def make_indent(self, indent):
        out_str = ""
        for i in range ( 0, indent ):
            out_str += " "
        return out_str


    # @brief recursive subroutine of emit_formatted_text()
    def visit_and_emit_formatted_text( self, n, depth, width_hint, indent, print_attr ):
        out_str = ''

        need_paren_for_attr = False

        if n.ast_node_type == 'terminal':
            out_str += n.content

        elif n.ast_node_type == 'nonterminal':
            out_str += n.content

        elif n.ast_node_type == 'union':
            rtn_str, need_paren_for_attr = self.visit_and_emit_formatted_text_union( n, depth, width_hint, indent, print_attr )
            out_str += rtn_str

        elif n.ast_node_type == 'sequence':
            rtn_str, need_paren_for_attr = self.visit_and_emit_formatted_text_sequence( n, depth, width_hint, indent, print_attr )
            out_str += rtn_str

        elif n.ast_node_type == 'finite repeat':
            rtn_str, need_paren_for_attr = self.visit_and_emit_formatted_text_finite_repeat( n, depth, width_hint, indent, print_attr )
            out_str += rtn_str

        elif n.ast_node_type == 'infinite repeat':
            rtn_str, need_paren_for_attr = self.visit_and_emit_formatted_text_infinite_repeat( n, depth, width_hint, indent, print_attr )
            out_str += rtn_str


        if print_attr:
            out_str = self.add_prologue_and_epilogue( n, out_str, need_paren_for_attr )
        return out_str


    # @brief subroutine of visit_and_emit_formatted_text()
    def add_prologue_and_epilogue( self, n, out_str, need_paren ):

        prologue = n.prologue_for_formatted_text()
        epilogue = n.epilogue_for_formatted_text()

        if n.ast_node_type == 'terminal' or n.ast_node_type == 'nonterminal':
            if epilogue != '':
                out_str += ' '
                out_str += epilogue

        elif n.ast_node_type == 'union' or n.ast_node_type == 'sequence' or n.ast_node_type == 'finite repeat' or n.ast_node_type == 'infinite repeat':

            prologue_insert_pos = 0
            new_out_str = ''
            if n.ast_node_type == 'union' and len(out_str)>0 and out_str[0] == '\n':
                prologue_insert_pos = 1
                while prologue_insert_pos < len(out_str) and out_str[prologue_insert_pos] == ' ':
                    prologue_insert_pos += 1

            if prologue != '':
                new_out_str += out_str[0:prologue_insert_pos]
                new_out_str += prologue
                new_out_str += ' '

            if need_paren and ( epilogue != '' or prologue != '' ):
                new_out_str += '( ' + out_str[prologue_insert_pos:] + ' )'
            else:
                new_out_str += out_str[prologue_insert_pos:]

            if epilogue != '':
                new_out_str += ' ' 
                new_out_str += epilogue

            out_str = new_out_str

        return out_str

    # @brief recursive subroutine of visit_and_emit_formatted_text()
    def visit_and_emit_formatted_text_union( self, n, depth, width_hint, indent, print_attr ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        out_str = ""
        need_paren_for_attr = False

        if width_hint != 0 and width_hint < n.text_width and len(children)>1:

            out_str += '\n'
            out_str += self.make_indent( (depth)*indent )
            out_str += '('

            first = True
            for c in children:
                if first:
                    first = False
                    out_str += '\n'
                    out_str += self.make_indent( (depth+1)*indent )

                else:
                    out_str += ' |\n'
                    out_str += self.make_indent( (depth+1)*indent )

                out_str += self.visit_and_emit_formatted_text( c, depth + 1, width_hint, indent, print_attr )

            out_str += '\n'
            out_str += self.make_indent( depth*indent )
            out_str += ')'
        else:
            c0_epilogue = children[0].epilogue_for_formatted_text()
            if len(children)>1 or c0_epilogue != '':
                out_str += '( '

                first = True
                for c in children:
                    if first:
                        first = False

                    else:
                        out_str += ' | '

                    out_str += self.visit_and_emit_formatted_text(c, depth + 1, width_hint, indent, print_attr )

                out_str += ' )'

            else: # len(children) == 1 and prologue == '' and epilogue == ''
                out_str += self.visit_and_emit_formatted_text(children[0], depth + 1, width_hint, indent, print_attr )
                need_paren_for_attr = True

        return out_str, need_paren_for_attr


    # @brief recursive subroutine of visit_and_emit_formatted_text()
    def visit_and_emit_formatted_text_sequence( self, n, depth, width_hint, indent, print_attr ):

        out_str = ''

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        first = True
        for c in children:

            if first:
                first = False
            else:
                out_str += ' '

            out_str += self.visit_and_emit_formatted_text( c, depth, width_hint, indent, print_attr )

        need_paren_for_attr = True
        
        return out_str, need_paren_for_attr



    # @brief recursive subroutine of visit_and_emit_formatted_text()
    def visit_and_emit_formatted_text_finite_repeat( self, n, depth, width_hint, indent, print_attr ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        child_prologue = children[0].prologue_for_formatted_text()
        child_epilogue = children[0].epilogue_for_formatted_text()

        if  ( children[0].ast_node_type == 'terminal' or children[0].ast_node_type == 'nonterminal' ) and child_prologue == '' and child_epilogue == '':
            out_str = self.visit_and_emit_formatted_text( children[0] , depth , width_hint, indent, print_attr )
        else:
            out_str = '( '
            out_str += self.visit_and_emit_formatted_text( children[0] , depth , width_hint, indent, print_attr )
            out_str += ' )'


        if n.repeat_min == 0 and n.repeat_max == 1:
            out_str += '?'
        else:
            out_str += '{ '
            out_str += str(n.repeat_min )
            out_str += ', '
            out_str += str(n.repeat_max)
            out_str += ' }'

        need_paren_for_attr = True
        return out_str, need_paren_for_attr


    # @brief recursive subroutine of visit_and_emit_formatted_text()
    def visit_and_emit_formatted_text_infinite_repeat( self, n, depth, width_hint, indent, print_attr ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        child_prologue = children[0].prologue_for_formatted_text()
        child_epilogue = children[0].epilogue_for_formatted_text()

        if ( children[0].ast_node_type == 'terminal' or children[0].ast_node_type == 'nonterminal' or children[0].ast_node_type == 'union' ) and child_prologue == '' and child_epilogue == '':
            out_str = self.visit_and_emit_formatted_text( children[0] , depth , width_hint, indent, print_attr )

        else:
            out_str = '( '
            out_str += self.visit_and_emit_formatted_text( children[0] , depth , width_hint, indent, print_attr )
            out_str += ' )'


        if n.repeat_min == 0:
            out_str += '*'
        else:
            out_str += '+'

        need_paren_for_attr = True
        return out_str, need_paren_for_attr


    ########################################
    #                                      #
    #            expand_phrases()          #
    #                                      #
    ########################################


    # @public
    # @brief generate expanded phrases
    def expand_phrases( self, gen_attributes = True ):

        self.node_attribute_id_next = 0
        if self.root:
            return self.visit_and_expand_phrases( self.root , gen_attributes )
        else:
            return []


    def visit_and_expand_phrases( self, n , gen_attributes ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        

        main_list = []
        need_paren_for_attr = False

        if n.ast_node_type == 'union':
            phrases = []
            for c in children:
                phrases = phrases + self.visit_and_expand_phrases( c, gen_attributes )
            main_list = phrases

        elif n.ast_node_type == 'sequence':
            phrases = []
            for c in children:
                phrases = cross_product( phrases, self.visit_and_expand_phrases( c,  gen_attributes ), ' ' )
            main_list = phrases
            need_paren_for_attr = True

        elif n.ast_node_type == 'terminal':
            main_list = [ n.content ]

        elif n.ast_node_type == 'nonterminal':
            main_list = [ n.content ]

        elif n.ast_node_type == 'epsilon':
            main_list = [ '' ]

        elif n.ast_node_type == 'finite repeat':
            if n.repeat_min == 0 and n.repeat_max == 1:
                phrases = [ '' ]
                phrases = phrases + self.visit_and_expand_phrases( children[0], gen_attributes )
                main_list = phrases
            else:
                # We don't further expand into repetition.
                phrase, need_paren_for_attr = self.visit_and_emit_formatted_text_finite_repeat( n, 0, 0, 0, gen_attributes )
                main_list = [ phrase ]

        elif n.ast_node_type == 'infinite repeat':
            # We don't further expand into repetition.
            phrase, need_paren_for_attr = self.visit_and_emit_formatted_text_infinite_repeat( n, 0, 0, 0, gen_attributes )
            main_list = [ phrase ]

        if gen_attributes:
            prologue = ''
            if n.ast_node_type == 'union' or n.ast_node_type == 'sequence' or n.ast_node_type == 'finite repeat' or n.ast_node_type == 'infinite repeat':
                prologue = n.attribute_for_expansion_before( self.node_attribute_id_next )

            epilogue = ''
            if  n.ast_node_type == 'terminal' or n.ast_node_type == 'nonterminal' or n.ast_node_type == 'union' or n.ast_node_type == 'sequence' or n.ast_node_type == 'finite repeat' or n.ast_node_type == 'infinite repeat':
                epilogue = n.attribute_for_expansion_after( self.node_attribute_id_next )
            if prologue != '' or epilogue != '':
                self.node_attribute_id_next += 1

            updated_main_list = []
            if prologue != '':
                if epilogue != '':

                    for m in main_list:
                        if m != '':
                            if need_paren_for_attr:
                                updated_main_list.append( '( ' + prologue + ' ( ' + m + ' ) ' + epilogue + ' )' )
                            else:
                                updated_main_list.append( '( ' + prologue + ' ' + m + ' ' + epilogue + ' )' )
                        else:
                            updated_main_list.append( '( ' + prologue + ' __EPS__ ' + epilogue  + ' )' )
                else:

                    for m in main_list:
                        if m != '':
                            if need_paren_for_attr:
                                updated_main_list.append( '( ' + prologue + ' ( ' + m  + ' ) )' )
                            else:
                                updated_main_list.append( '( ' + prologue + ' ' + m + ' )' )
                        else:
                            updated_main_list.append( '( ' + prologue + ' __EPS__ )' )

            else:           
                if epilogue != '':
                    for m in main_list:
                        if m != '':
                            if need_paren_for_attr:
                                updated_main_list.append( '( ( ' + m + ' ) ' + epilogue + ' )' )
                            else:
                                updated_main_list.append( '( ' + m + ' ' + epilogue + ' )' )
                        else:
                            updated_main_list.append( '( __EPS__ ' + epilogue  + ' )' )
                else:
                    for m in main_list:
                        updated_main_list.append( m )

            return updated_main_list

        else:
            return main_list


    ########################################
    #                                      #
    #                draw()                #
    #                                      #
    ########################################


    # @public
    # @brief draws AST with graphviz
    # @param tree_name  : output file name
    # @param view_now   : True/False launch viewer immediately
    # @param out_format : 'svg' or 'pdf'. Use 'svg' if window's PDF renders
    #                     messes up UTF-8.
    # @param orientagion: 'vertical' or 'horizontal'. top to bottom or left to right.
    #                     specifies the direction of 
    #                     the tree from the root toward children.
    def draw( self, tree_name, view_now = True, out_format ="svg", orientation ="vertical" ):

        g_dot = Digraph( comment = tree_name )
        if orientation == 'horizontal':
            g_dot.graph_attr['rankdir'] = 'LR'
        node_set = set()

        self.node_id = 1

        self.visit_and_draw( self.root, g_dot , -1, node_set )

        for n in self.nodes():
            if hasattr(n, 'node_id'):
                delattr( n, 'node_id' )

        g_dot.render(tree_name.strip('<>'), view=view_now, format=out_format)


    # @brief recursive subroutine of draw()
    def visit_and_draw( self, n, dot , parent_id, node_set ):
        
        n.node_id = self.node_id
        should_visiting_children = True

        self.node_id += 1
        if n.node_id not in node_set:

            label_out, should_visit_children = n.generate_string_for_drawing(True)
            dot.node( str(n.node_id), label_out  )

            node_set.add(n.node_id)


        if parent_id != -1:
            dot.edge( str(parent_id), str(n.node_id) )

        
        if should_visit_children:

            children  = [ e.other_node_of( n ) for e in n.out_neighbors() ]

            for c in children:
                self.visit_and_draw( c , dot, n.node_id, node_set )

            # Add horizontal edges to force ordering among children.
            for i in range( 0, len(children)-1 ):
                dot.edge( str(children[i].node_id), str(children[i+1].node_id) ,style='invis' )

            with dot.subgraph() as s:
                s.attr(rank = 'same')
                for c in children:
                    s.node(str(c.node_id))


    ########################################
    #                                      #
    #            generate_fst()            #
    #                                      #
    ########################################


    # @brief generate FST
    #        finite repeat must be expanded into union
    #
    # @param generate_out_tokens
    #
    # @param generate_balancedids
    def generate_fst ( self, generate_out_tokens = True ):

        if self.root:
            self.node_attribute_id_next = 0
            return self.visit_and_generate_fst( self.root, generate_out_tokens )

        else:
            return None


    # @brief recursive subroutine to generate_fst()
    def visit_and_generate_fst( self, n, generate_out_tokens ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        g_main = None

        if n.ast_node_type == 'union': 
            graphs = []
            for c in children:
                graphs.append( self.visit_and_generate_fst( c, generate_out_tokens ) )
            g_main = fa.ttsp_bundle( graphs )

        elif n.ast_node_type == 'sequence':
            graphs = []
            for c in children:
                graphs.append( self.visit_and_generate_fst( c, generate_out_tokens ) )
            g_main = fa.ttsp_concatenate( graphs )

        elif n.ast_node_type == 'terminal':
            in_token, out_token = n.node_content_for_fst_main( self.node_attribute_id_next )
            self.node_attribute_id_next += 1

            g_main = fa.make_unit_transition( in_token, out_token )

        elif n.ast_node_type == 'nonterminal':
            in_token, out_token = n.node_content_for_fst_main( self.node_attribute_id_next )
            self.node_attribute_id_next += 1

            g_main = fa.make_unit_transition( in_token, out_token )

        elif n.ast_node_type == 'epsilon':
            g_main = fa.make_unit_epsilon()

        elif n.ast_node_type == 'infinite repeat' or n.ast_node_type == 'finite repeat':

            if n.repeat_min == 0:
                if n.repeat_max == 1:
                    graphs = []
                    graphs.append( self.visit_and_generate_fst( children[0], generate_out_tokens ) )
                    graphs.append( fa.make_unit_epsilon() )
                    g_main = fa.ttsp_bundle( graphs )
                else:
                    graphs = []
                    graphs.append( self.visit_and_generate_fst( children[0], generate_out_tokens ) )
                    graphs.append( fa.make_unit_epsilon() )
                    g_inside = fa.ttsp_bundle( graphs )
                    g_main = fa.enclose_in_cycle( g_inside, n.repeat_max )
            else:
                g_inside = self.visit_and_generate_fst( children[0], generate_out_tokens )
                g_main = fa.enclose_in_cycle( g_inside, n.repeat_max )

        else:
            return None


        if generate_out_tokens:

            # pair-up the attributes by using the same attribute ID.
            out_token_pre  = n.extra_epsilon_nodes_before ( )
            out_token_post = n.extra_epsilon_nodes_after  ( )

            if out_token_pre != '' or  out_token_post != '':

                marker_pre  = '[PRE {:d}]'.format(self.node_attribute_id_next)
                marker_post = '[POST {:d}]'.format(self.node_attribute_id_next)
                self.node_attribute_id_next += 1

                serial_graphs = []
                serial_graphs.append( fa.make_unit_transition( marker_pre, out_token_pre ) )
                serial_graphs.append( g_main )
                serial_graphs.append( fa.make_unit_transition( marker_post, out_token_post ) )
                return fa.ttsp_concatenate( serial_graphs )

            else:
                return g_main

        else:
            return g_main


    ########################################
    #                                      #
    #           count_phrases()            #
    #                                      #
    ########################################


    # @public
    # @brief count the number of phrases the node accepts
    #        as a root of the subtree.
    #        under the repeat nodes are not explored
    def count_phrases(self):
        if self.root:
            self.visit_and_count_phrases( self.root )


    # @brief recursive subroutine of count_phrases()
    def visit_and_count_phrases( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            self.visit_and_count_phrases( c )

        if n.ast_node_type == 'union':
            n.phrase_count = 0
            for c in children:
                n.phrase_count += c.phrase_count
            
        elif n.ast_node_type == 'sequence':

            n.phrase_count = 1
            for c in children:
                n.phrase_count *= c.phrase_count

        else:
            n.phrase_count = 1
