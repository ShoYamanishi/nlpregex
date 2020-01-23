#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph


# @brief represents a AST node for sseASTForrest
# 
#     @member ast_node_type
#         - types used when node is created from FA
#             't1'--'t9999999' : terminals
#             'u'              : union
#             's'              : sequence
#             '*'              : repeat
#             'e'              : epsilon
#
#         - types introduced after the SSE is solved.
#             '?'              : option (this is introduced later
#                                as a result of removing epsilon child
#                                from a union
#
#         - types introduced for common subexpression reduction
#
#             'r'              : root or the forrest under which
#                                all the AST trees for the nonterminals are hung.
#
#             'n0'             : special nonterminal to represent the 
#                                main (top-level) tree.
#
#             'n1'--'n9999999' : nonterminals and nonterminals
#                                this is introduced as an outcome
#                                of common tree reduction
#
#     @member regex : represents the regular expression at this node
#                     as a subtree. please note the spaces between items
#                     for easy tokenization.
#
#                     - type 'u'    => '( item1 | item2 | ... | itemX )'
#                     - type 's'    => 'item1 item2 ... itemX'
#                     - type '*'    => 'item1 *' or '( items ) *'
#                     - type '?'    => 'item1 ?' or '( items ) ?'
#                     - type others =>  ast_node_type
#
#     @member children_map : used by 'u' for faster access to children by regex,
#                            and by 'r' to associate nonterminals to their
#                            corresponding AST subtrees under 'r'
#
#     @member num_terms : number of terminals under this node
#
#     @member height    : height of the subtree whose root is this node
#
#     @member node_id   : ASTForrest-wide unique ID assigned to this node
#                         used by __hash__(), __eq__(), __ne__() for children_map
#                        
class sseASTNode( nlpregex.abs_graph.node.BaseNode ):


    def __init__( self, ast_node_type ):

        super().__init__()

        # type explained above.
        self.ast_node_type  = ast_node_type 

        # string that represents the AST subtree whose root is this node
        self.regex          = ast_node_type

        # key:   regex for a child AST subtree
        #        or, if this is 'r', then correcponding nonterminal
        # value: node to the root of the AST subtree
        self.children_map   = {}

        # Number of terms under the subtree whose root is this node
        self.num_terms      = 0 

        # height of the subtree whose root is this node
        self.height         = 0

        # node unique id. this is assigned by sseASForrest
        # when unassigned it is -1
        self.node_id        = -1

        # The terminal transferred from the balanced children used
        # for attributes/output tokens
        self.balanced_out_pre  = ''
        self.balanced_out_post = ''


    def get_children( self ):
        return [ e.other_node_of( self ) for e in  self.out_neighbors() ]


    def clone( self ):

        c               = sseASTNode( self.ast_node_type )
        c.regex         = self.regex
        c.num_terms     = self.num_terms
        c.height        = self.height
        c.children_map  = {}

        return c


    def reset(self, ast_node_type ):
        self.ast_node_type  = ast_node_type 
        self.regex          = ast_node_type
        self.num_terms      = 0
        self.height         = 0
        self.children_map   = {}
        

    def generate_children_map_for_union( self ):
        if self.ast_node_type == 'u':
            self.children_map = {}
            children = [ e.other_node_of( self ) for e in self.out_neighbors() ]
            for c in children:
                self.children_map[c.regex] = c


    def generate_regex(self):

        children = [ e.other_node_of( self ) for e in self.out_neighbors() ]

        if self.ast_node_type == 'u':
            regex_str = '( '
            first = True
            for c in children:

                if first:
                    first = False

                else:
                    regex_str += ' | '

                regex_str += c.regex

            regex_str += ' )'
            self.regex = regex_str

        elif self.ast_node_type == 's':

            regex_str = ''
            first = True
            for c in children:

                if first:
                    first = False

                else:
                    regex_str += ' '

                regex_str += c.regex

            self.regex = regex_str

        elif self.ast_node_type == '*':

            c = children[0]

            if c.ast_node_type == 's' and c.out_degree() > 1:
                self.regex = '( ' + c.regex + ' ) *'

            else:
                self.regex = c.regex + ' *'

        elif self.ast_node_type == '?':

            c = children[0]

            if c.ast_node_type == 's' and c.out_degree() > 1:
                self.regex = '( ' + c.regex + ' ) ?'

            else:
                self.regex = c.regex + ' ?'

        else: # tXXXX, nXXXX, and 'r'
            self.regex = self.ast_node_type


    def has_epsilon_child(self):
        children = [ e.other_node_of( self ) for e in self.out_neighbors() ]
        for c in children:
            if c.ast_node_type == 'e':
                return True
        return False


    def __hash__( self ):
        return self.node_id


    def __eq__( self, other ):
        return self.node_id == other.node_id


    def __ne__( self, other ):
        return self.node_id != other.node_id


    def __lt__( self, other ):
        return self.node_id < other.node_id


    def __repr__( self ):
        return self.__str__()


    def __str__( self ):
        out_str = ''
        out_str += 'node_id: '
        out_str += str(self.node_id)
        out_str += ' type: ' 
        out_str += self.ast_node_type
        out_str += ' re:[' 
        out_str += self.regex
        out_str += ']' 
        return out_str


    def diag_str(self):
        out_str = ''
        out_str += 'type: ' 
        out_str += self.ast_node_type
        out_str += ' re:[' 
        out_str += self.regex
        out_str += ']' 
        return out_str


#
# @brief represents a AST node for sseASTForrest
#
class sseASTEdge( nlpregex.abs_graph.edge.BaseEdge ):

    def __init__(self):
        super().__init__()


# @brief represents a set of AST trees, each of which corresponds
#        to a coefficient in a symbolic simultaneous equation.
#
#        After SSE is solved, there is only one remaining AST,
#        which is linked to RootedTree.root by:
#            create_tree_root_for_reduction()
#        After this call, the forrest will be:
#        root -> 'r' -> 'n0' -> ... where 'n0' is the root node
#        of the main tree.
#
# @note  on epsilon : an epsilon may be introduced already by the 
#                     conversion from FA, and through the SSE solving
#                     process, '*' is introduced by Arden's rule.
#                     After the SSE is solved, epsilon is eliminated
#                     by the following rules.
#                     - epsilon under '*' is removed
#                     - epsilon under 'u' is removed, and '?' is inserted
#                       between 'u' and its parent
#                     - epsilon under 's' is removed
#                     this is done by the folowing:
#
#                     - throughout solving SSE
#                         repeat_AST()
#                             remove_epsilon_child_from_union_node()
#
#                         concat_two_ASTs( self, t1, t2 ):
#                             remove_epsilon_from_series()
#
#                     - after solving SSE
#                         remove_epsilons_from_unions()
#                             visit_and_remove_epsilon_from_union()
#                                 remove_epsilon_child_from_union_node()
#
# @functions manifest
#
#   - ID allocator
#        next_node_id_allocation()
#
#   - Nonterminal allocator
#
#        reset_nonterminal_num_allocation() # Not used
#
#        allocate_nonterminal()
#            used by CommonSubtreeReducer.            reduce_best_common_subtree(),
#                    CommonSubstringReducer.          reduce_best_common_substring(), and
#                    CommonUnionSubexpressionReducer. reduce_best_common_subexpression()
#
#   - Regex generator
#
#        generate_regex()
#            visit_and_generate_regex()
#
#   - Initial tree factories
#        create_initial_node()
#        create_initial_union_node()
#        union_two_ASTs()
#        concat_two_ASTs()
#            remove_epsilon_from_series()
#        repeat_AST()
#
#   - cloning and removal
#
#        remove_AST()
#            remove_AST_r()
#
#        clone_AST()
#            clone_AST_r1()
#            clone_AST_r2()
#
#   - After SSE is solved
#        create_tree_root_for_reduction()
#        remove_epsilons_from_unions()
#            visit_and_remove_epsilon_from_union()
#
#   - Before every tree reduction
#        prepare_for_reduction()
#            visit_and_prepare_for_reduction()
#
#   - Printing
#        print_tree()
#            make_indent()
#
#   - Utility
#        remove_duplication_and_order_children()
#
class sseASForrest( nlpregex.abs_graph.graph.RootedTree ):


    def __init__(self):

        super().__init__()

        # @brief used to generate a new nonterminal
        self.next_nonterminal_num = 1

        # @brief allocator for a temporary id used to clone nodes.
        self.node_id_next         = 0


    #############################
    #        ID ALLOCATOR       #
    #############################

    def next_node_id_allocation(self):

        rtn = self.node_id_next
        self.node_id_next += 1

        return rtn


    #############################
    #   NONTERMINAL ALLOCATOR   #
    #############################


    def reset_nonterminal_num_allocation(self):
        self.next_nonterminal_num = 1 

    def allocate_nonterminal(self):
        nonterminal = 'n' + str( self.next_nonterminal_num )
        self.next_nonterminal_num += 1 
        return nonterminal


    #############################
    #       REGEX GENERATOR     #
    #############################


    # @brief regenerate regex at each node.
    #        self.root must be set before calling this.
    def generate_regex(self):
        self.visit_and_generate_regex(self.root)


    def visit_and_generate_regex( self, n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            self.visit_and_generate_regex( c )
        n.generate_regex()        


    #############################
    #   CHILDREN_MAP GENERATOR  #
    #############################
    def generate_children_map_for_union( self ):
        self.visit_and_generate_children_map_for_union( self.root )


    def visit_and_generate_children_map_for_union( self, n ):


        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            self.visit_and_generate_children_map_for_union( c )

        if n.ast_node_type == 'u':
            n.generate_children_map_for_union()



    #############################
    #  INITIAL TREE FACTORIES   #
    #############################

    # @brief convenient routine to creaet a tree that consists
    #        of only one initial node.
    #
    # @param term : terminal, which is expected to be in 'tXXXXX'
    #
    # @return the node created.
    def create_initial_node( self, term ):

        n = sseASTNode( term )
        n.add_to_graph( self )
        n.node_id = self.next_node_id_allocation()
        n.regex = term;

        return n


    # @brief convenient routine to create a tree that consists
    #        of a union whose children are terms.
    #        if there is only one element in param_children,
    #        this is equivalent to create_initial_node([param_children[0])
    #
    # @param param_children : list of terms.
    #
    # @return the root (union) of the tree created
    def create_initial_union_node( self, param_children ):

        # sanitize input.
        children = self.remove_duplication_and_order_children( param_children )

        if len( children ) == 0:
            return None

        if len( children )== 1:
            return self.create_initial_node( children[0] )

        r = self.create_initial_node('u' )

        for c in children:
            n = self.create_initial_node( c )
            e =sseASTEdge()
            e.add_to_graph( self, r, n, "directed" )

        r.generate_regex()
        r.generate_children_map_for_union()

        return  r


    # @brief convenient routine to merge two union subtrees into one,
    #        taking care of removal of duplications
    #
    # @param t1: tree whose root is union or a single node of terminal type.
    # @param t2: tree whose root is union or a single node of terminal type.
    #
    # @return the root (union) of the tree created.
    def union_two_ASTs( self, t1, t2 ):

        children_retain = {}
        children_removed = {}

        if t1.ast_node_type == 'u':
            # Keep the children and remove the top union node
            children_retain = t1.children_map
            t1.remove_from_graph()

        else:
            children_retain[ t1.regex ] = t1

        if t2.ast_node_type == 'u':
            # Keep the children and remove the top union node
            children_removed = t2.children_map
            t2.remove_from_graph()

        else:
            children_removed[ t2.regex ] = t2

        # Merge children_removed into children1
        for candidate in children_removed:
            if candidate not in children_retain:
                children_retain[ candidate ] = children_removed[ candidate ]
            else:
                self.remove_AST( children_removed[ candidate ] ) # redundant. removing.

        children_new = self.remove_duplication_and_order_children( children_retain.keys() )
        
        if len( children_new ) == 0:
            return self.create_initial_node( e )

        elif len( children_new ) == 1:
            return children_retain[ children_new[0] ]

        else:
            r = self.create_initial_node('u' )
            r.children_map = children_retain

            for c in children_new:
                n = r.children_map[ c ]
                e =sseASTEdge()
                e.add_to_graph( self, r, n, "directed" )

            r.generate_regex()

            return r


    # @brief concatenate two ASTs serially and create a new 's' node.
    #
    # @param t1: AST that will become the first child
    # @param t2: AST that will become the second child
    #
    # @return root (series) of the tree created
    def concat_two_ASTs( self, t1, t2 ):

        children1 = []
        children2 = []

        # The first AST is epsilon. returning t2.
        if t1.ast_node_type == 'e':
            t1.remove_from_graph()
            return t2

        # The second AST is epsilon. returning t1.
        if t2.ast_node_type == 'e':
            t2.remove_from_graph()
            return t1

        if t1.ast_node_type == 's':
            # Keep the children and remove the top serial node
            children1 = [ e.other_node_of( t1 ) for e in  t1.out_neighbors() ]
            t1.remove_from_graph()  

        else:
            children1 = [t1]

        if t2.ast_node_type == 's':
            # Keep the children and remove the top serial node
            children2 = [ e.other_node_of( t2 ) for e in  t2.out_neighbors() ]
            t2.remove_from_graph()  

        else:
            children2 = [t2]

        cleaned_children = self.remove_epsilon_from_series( children1 + children2 )

        if len(cleaned_children) == 0:
            return self.create_initial_node( 'e' )

        elif len(cleaned_children) == 1:
            return cleaned_children[0]

        else:
            r = self.create_initial_node( 's' )

            for c in cleaned_children:
                e =sseASTEdge()
                e.add_to_graph( self, r, c, "directed" )

            r.generate_regex()
            return r


    def remove_epsilon_from_series( self, children ):
        cleaned_children = []
        for c in children:
            if c.ast_node_type != 'e':
                cleaned_children.append(c)
            else:
                c.remove_from_graph()

        return cleaned_children


    # @brief add repeat '*' to the given AST
    #
    # @param t: AST to which '*' will be added
    #
    # @return root of the tree created
    def repeat_AST( self, t ):
        
        if t.ast_node_type == 'e' or t.ast_node_type == '*':
            # no need to add '*'
            return t

        elif t.ast_node_type == '?':
            # Change '?' to '*'
            t.ast_node_type = '*'
            t.generate_regex()
            return t

        elif t.ast_node_type == 'u':
            # epsilon child is redundant after adding '*'
            self.remove_epsilon_child_from_union_node( t )

        r = self.create_initial_node( '*' )

        e = sseASTEdge()
        e.add_to_graph( self, r, t, "directed" )
        r.generate_regex()

        return r


    #############################
    #    CLONING AND REMOVAL    #
    #############################


    # @brief remove an AST from this forrest
    def remove_AST( self, t):

        self.remove_AST_r( t )

        if self.root and self.root == t:
                self.root = None


    # @brief recursive accompanying function to remove_AST.
    def remove_AST_r( self, n ):
        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        for c in children:
            self.remove_AST_r(c)
        n.remove_from_graph()


    # @brief clone an AST in this forrest.
    #
    # @param t : root of the tree to be cloned
    #
    # @return root to the cloned tree
    def clone_AST( self, t ):

        cloned_nodes_map = {}

        self.clone_AST_r1 ( t, cloned_nodes_map )
        r = self.clone_AST_r2 ( t, cloned_nodes_map )

        return r


    # @brief recursive accompanying function to clone_AST.
    def clone_AST_r1( self, n, cloned_nodes_map ):

        nclone   = n.clone()
        nclone.add_to_graph(self)
        nclone.node_id = self.next_node_id_allocation()
        cloned_nodes_map[n] = nclone

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        for c in children:      
            self.clone_AST_r1( c, cloned_nodes_map )


    # @brief recursive accompanying function to remove_AST.
    def clone_AST_r2( self, n, cloned_nodes_map ):

        nclone = cloned_nodes_map[n]

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:      
            cclone = self.clone_AST_r2( c, cloned_nodes_map )
            eclone = sseASTEdge()
            eclone.add_to_graph( self, nclone, cclone, "directed" )


        if nclone.ast_node_type == 'u':
            # for 'u' node, construct the children map.
            children_clone = [ eclone.other_node_of( nclone ) for eclone in  nclone.out_neighbors() ]
            for cclone in children_clone:
                nclone.children_map[cclone.regex] = cclone

        return nclone


    ##############################
    # REMOVE EPSILON FROM UNIONS #
    ##############################


    # @brief remove epsilon nodes from the children of the unions and 
    #        introduce option ('?') nodes above the unions.
    def remove_epsilons_from_unions(self, r):

        self.visit_and_remove_epsilon_from_union( r )


    def visit_and_remove_epsilon_from_union(self, n):

        tree_changed = False
        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        for c in children:
            changed = self.visit_and_remove_epsilon_from_union( c )
            if changed:
                tree_changed = True

        if tree_changed:
            n.generate_regex()

        if n.ast_node_type == 'u':

            if n.has_epsilon_child():
                tree_changed = True
                self.remove_epsilon_child_from_union_node( n )
                self.push_down_children_and_put_under_question( n )

            elif tree_changed:
                n.generate_children_map_for_union()
        return tree_changed


    def pull_up_only_child( self, n ):

        children = [ e.other_node_of( n ) for e in n.out_neighbors() ]
        c0       = children[0]

        n.ast_node_type = c0.ast_node_type
        n.regex         = c0.regex
        n.num_terms     = c0.num_terms
        n.height        = c0.height
        n.children_map  = c0.children_map

        grand_children = [ e.other_node_of( c0 ) for e in c0.out_neighbors() ]

        c0.remove_from_graph()

        for gc in grand_children:
            e =sseASTEdge()
            e.add_to_graph( self, n, gc, "directed" )
        

    def remove_epsilon_child_from_union_node( self, n ):

        children = [ e.other_node_of( n ) for e in n.out_neighbors() ]
        has_epsilon = False
        for c in children:
            if c.ast_node_type == 'e':
                c.remove_from_graph()
                has_epsilon = True

        if has_epsilon:
            children = [ e.other_node_of( n ) for e in n.out_neighbors() ]
            if len(children) == 1:
                self.pull_up_only_child( n )

            n.generate_regex()
            n.generate_children_map_for_union()


    def push_down_children_and_put_under_question( self, n ):

        children = [ e.other_node_of( n ) for e in n.out_neighbors() ]

        edges = [ e for e in n.out_neighbors() ]

        for e in edges:
            e.remove_from_graph()         

        # n '?' -> new_c -> children
        new_c = n.clone()
        new_c.add_to_graph( self )
        new_c.node_id = self.next_node_id_allocation()

        for gc in children:
            e =sseASTEdge()
            e.add_to_graph( self, new_c, gc, "directed" )

        new_c.generate_regex()
        new_c.generate_children_map_for_union()

        e =sseASTEdge()            
        e.add_to_graph( self, n, new_c, "directed" )

        n.reset( '?' )
        n.generate_regex()


    # @brief construct initial rooted tree with 'r' node with 'n0'.
    #        self.root 'r' -> node1 ->...
    #        self.root.children_map['n0'] = node1
    def create_tree_root_for_reduction( self, n ):

        self.root = self.create_initial_node( 'r' )
        e =sseASTEdge()            
        e.add_to_graph( self, self.root, n, "directed" )

        self.root.children_map[ 'n0' ] = n
        self.reset_nonterminal_num_allocation()



    # @brief reflesh the following variables in all the sseASTNodes
    #        - num_terms
    #        - height
    #        - regex
    #        - children_map for 'u' nodes
    def prepare_for_reduction( self ):

        self.visit_and_prepare_for_reduction( self.root )


    def visit_and_prepare_for_reduction( self , n ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]

        if len( children ) == 0:
            n.num_terms = 1
            n.height    = 1

        else:

            max_height      = 0
            sum_descendents = 0
            for c in children:
                self.visit_and_prepare_for_reduction( c )
                max_height = max( max_height, c.height )
                sum_descendents += c.num_terms

            n.num_terms = sum_descendents
            n.height    = max_height + 1

        if n.ast_node_type != 'r':
            n.generate_regex()
            if n.ast_node_type == 'u':
                n.generate_children_map_for_union()


    # @brief balance the trees for output tokens
    #        
    def balance_trees_for_out_tokens( self, balanced_list ):

        balance_dic = {}

        for pre, post in balanced_list:
            balance_dic[pre] = post

        self.visit_and_balance_trees_for_out_tokens( self.root, balance_dic )


    def visit_and_balance_trees_for_out_tokens( self, n, balance_dic ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        for c in children:
            self.visit_and_balance_trees_for_out_tokens( c, balance_dic )

        if n.ast_node_type == 's':

            while True:

                children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
                balance_stack = []
                pos_begin = -1
                pos_end   = -1

                for i in range(0, len(children)):

                    t = children[i].ast_node_type
                    if t in balance_dic:
                        balance_stack.append( (i, balance_dic[t]) )
                   
                    elif len(balance_stack) > 0:
                        if t == balance_stack[-1][1]:
                            pos_begin = balance_stack[-1][0]
                            pos_end   = i
                            break

                if pos_begin == -1:
                    # No balance found.
                    break

                self.isolate_balanced_children( n, pos_begin, pos_end )


    def isolate_balanced_children( self, n, pos_begin, pos_end ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        
        balanced_child_0 = children[pos_begin + 1]

        # Isolate the children between pos_begin and pos_end
        if pos_begin == 0 and pos_end == len(children) -1:                
            # The outer most pair. No need to create a subtree.
                  
            n.balanced_out_pre  = children[  0 ].ast_node_type
            n.balanced_out_post = children[ -1 ].ast_node_type

            self.remove_AST( children[  0 ] )
            self.remove_AST( children[ -1 ] )

        elif self.child_can_absorb_balanced_out( pos_begin, pos_end, balanced_child_0 ):
            # There is only child between balanced children and it is clean.
            balanced_child_0.balanced_out_pre  = children[ pos_begin ].ast_node_type
            balanced_child_0.balanced_out_post = children[ pos_end   ].ast_node_type

            self.remove_AST( children[ pos_begin ] )
            self.remove_AST( children[ pos_end   ] )

        else:
            edges = [ e for e in  n.out_neighbors() ]
            children_to_move = []
            edges_to_remove  = []
            insertion_before = None
            for i in range ( pos_begin + 1, pos_end ):

                children_to_move.append ( children [ i ] )
                edges_to_remove .append ( edges    [ i ] )

            c_new = self.create_initial_node( 's' )
            e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
            c_new.balanced_out_pre  = children[ pos_begin ].ast_node_type
            c_new.balanced_out_post = children[ pos_end   ].ast_node_type

            if pos_end == len(children) - 1:
                e.add_to_graph( self, n, c_new, "directed" )
            else:
                e.add_to_graph_at_specific_positions( self, n, c_new, "directed", edges[pos_end  + 1], None )

            for e in edges_to_remove:
                e.remove_from_graph()

            for gc in children_to_move:
                e = nlpregex.regular_language.sse_forrest.sseASTEdge() 
                e.add_to_graph( self, c_new, gc, "directed" )

            self.remove_AST( children[ pos_begin ] )
            self.remove_AST( children[ pos_end   ] )

    def child_can_absorb_balanced_out( self, pos_begin, pos_end, c ):
        return pos_end - pos_begin == 2 and c.ast_node_type[0] == 't' and c.balanced_out_pre == '' and c.balanced_out_post == ''


    # @brief remove trees in the following form <NT_X> : <NT_Y>.
    #        it can happen as a result of common subexpression reduction.
    #        Remove this tree, and replace all the occurrence of NT_X with NT_Y.
    def remove_nt_only_trees( self ):
        map_badNT_to_newNT = self.find_nt_only_trees()
        for nt in map_badNT_to_newNT:
            self.remove_AST (self.root.children_map[nt] )
            del ( self.root.children_map[nt] )
        self.visit_and_replace_old_nt_with_new_nt(self.root, map_badNT_to_newNT)

    def visit_and_replace_old_nt_with_new_nt( self, n, map_badNT_to_newNT ):

        if n.ast_node_type in map_badNT_to_newNT:
            n.ast_node_type = map_badNT_to_newNT[n.ast_node_type]

        else:
            children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
            for c in children:
                self.visit_and_replace_old_nt_with_new_nt( c, map_badNT_to_newNT ) 

    def find_nt_only_trees( self ):
        map_badNT_to_newNT = {}
        for nt in self.root.children_map:
            ast = self.root.children_map[nt]
            if ast.ast_node_type[0] == 'n':
                 map_badNT_to_newNT[nt] = ast.ast_node_type
        return map_badNT_to_newNT
 



    def find_nonterminals( self ):

        nonterminals = set( self.root.children_map )

        self.visit_and_find_nonterminals( self.root, nonterminals )
        return list(nonterminals)


    def visit_and_find_nonterminals( self, n, nonterminals ):

        children = [ e.other_node_of( n ) for e in  n.out_neighbors() ]
        for c in children:
            self.visit_and_find_nonterminals( c, nonterminals )

        if n.ast_node_type[0] == 'n':
            nonterminals.add( n.ast_node_type )

        return nonterminals


    # @brief diag/debug function to print out tree with indents
    #        each line represents a node and indent represents the tree depth
    def print_tree( self, r, depth ):

        out_str  = ''
        out_str += self.make_indent( depth )
        out_str += r.diag_str()
        out_str += '\n'

        children = [ e.other_node_of( r ) for e in  r.out_neighbors() ]
        for c in children:
            out_str += self.print_tree( c, depth + 4 )

        return out_str


    def make_indent( self, depth ):

        out_str = ''
        for i in range( 0, depth ):
            out_str += ' '

        return out_str


    def remove_duplication_and_order_children( self, children ):
        return sorted( list( set( children ) ) )

