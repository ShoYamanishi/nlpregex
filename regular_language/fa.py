#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph

from graphviz import Digraph
import re

import subprocess
import os


SYM_EPSILON = "<eps>"

# @class FA
#
# Represents a finite-state automaton FA=(A, S, s, D, F) where
#    A: set of alphabets
#    S: set of states
#    s: start state
#    F: set of final states
#    D: S x A -> S: Transition from a state to the next upon
#                   receiving an alphabet.
#
# It is represented by directed graph FA=(N,E).
#   N: set of states in FANode.
#   E: represents transition D in FAEdge.
#
# The transition is defined as in_token and out_token.
# Epsilon transition is represented by empty string ''.
#
#
# Standalone functions
# --------------------
#
# - DFA_from_NFA( nfa , optimize = False)
#
#     generates an equivalent DFA from given NFA
#     It assumes the availability of the following commands and libs from OpenFST.
#         - fstcompile
#         - fstdeterminize
#         - fstrmepsilon
#         - fstminimize
#         - fstprint
#
#     @param nfa       : input NFA
#     @param optimize  : True if you want to run fstminimize 
#                        it will change the relative position of output token
#                        relative to the input token.
#     @return DFA in FA.
#
#
# 
# # Following functions are provided to generate a primitive automata.
#
#
# - make_unit_epsilon()#
#
#       creates an FA that has the unit epsilon transition only
#       s ---[eps]---> f
#
#
# - make_unit_transition(in_token, out_token):
#
#       creates an FA that accepts a single token.
#
#       s --- in_token/out_token ---> f
#
#
# - ttsp_concatenate( S )
#
#       creates an FA which accepts the sequence serially in the
#       FAs specified in S in that order.
#       Let S = [Sstart, S2, S3, ..., Send]
#       Then the resultant FA's start state is Start's start, and
#       the final states correspond to the final states of Send.
#
#       Sstart.s ---<Sstart>---> n1 ---<S2>---> n2 ... ---<Send>--->Send.F
#
#
# - ttsp_bundle( P )
#
#       creates an FA which accepts any sequence by FA specified in P.
#       Let P = [P1, P2, ..., PN]
#
#          +---<P1>---+
#          |          |
#        s-+---<P2>---+-F
#          | ...  ... |
#          |          |
#          +---<Pn>---+
#
#
# - enclose_in_cycle( g, plus_or_star )
#
#       Make the FA a Kleene closure or a positive closure.
#
#       @param g : FA to be processed
#       @param plus_or_star : '+' - add a backward edge from f to s.
#                             '*' - add a backward edge and forward edge 
#
#       Add a backward edge from the finish node to the start node
#      
#      ________                          ________
#     /        \                        /        \
#    s----------f  =>   s_new -<eps>-> s----------f -<eps>-> f_new
#     \________/           |           ^\________/|            ^
#                          |           |          |            |
#                          |            --<eps>---             |
#                           --------------<eps>----------------
#                                         ('*')
#
# # Convertion to/from OpenFST
#
# FA has a functionality to convert to/from OpenFST text format files.
#
# FST's text representation consists of three files.
#
# - FST file
#     This describest the graph structure and their edges.
#     It consists of three parts.
#
#     The first part has the following line.
#
#         0 dst_node_id in_sym_id [out_sym_id] [weight]
#
#     The first 0 represents the intial node ID and it is reserved for
#     the initial state.
#
#     The second part has the follwing format per line.
#
#         src_node_id dst_node_id in_sym_id [out_sym_id] [weight]
#
#     They are all decimal numbers.
#     The src_node_id in the first line designates the start state.
#
#     The third part has the following format per line.     
#
#         final_node_id
#
# - Input symbol file
#      This describest the mapping from in_sym_id in the FST file to an actual symbol.
#      Each line has the following format.
#      in_sym_id  in_sym_str
#
#      0 is reserved for epsilon and it is by customary the first line as follows.
#
#          0 <eps>
#
# - Output symbol file
#      This describest the mapping from out_sym_id in the FST file to an actual symbol.
#      It has the same format as the input symbol file.
#
# To avoid potential problems caused by certain characters in unicode in in_token and out_token of FAEdge,
# we make a mapping from the strings in in_token/out_token to in_sym_str/out_sym_str.
#
# The mapping from in_token/out_token to in_sym_str/out_sym_str is as follows
#
#     in_token/out_token <===>  in_sym{:08d}".format(id) / out_sym{:08d}".format(id)
#
#
# The conversion is provided by the following two member functions of FA.
#
# 
# Conversion to OpenFST:
# ( str0, str1, str2, str3, str4 ) = FA.to_open_fst()
#
# str0 : contents of FST file for OpenFST
# str1 : contents of Input symbol file for OpenFST
# str2 : contents of Output symbol file for OpenFST
# str3 : contents of mapping from in_sym_str to real in_token
# str4 : contents of mapping from out_sym_str to real out_token
#
#
# Conversion from OpenFST:
# FA.from_open_fst( fst, sym_in, sym_out )
#
# FA must be empty before calling this.
# @param fst     : conetnts of OpenFST file (text version, not compiled binary version.)
# @param sym_in  : mapping from in_sym_str to real in_token
# @param sym_out : mapping from out_sym_str to real out_token
#
class FANode(nlpregex.abs_graph.node.BaseNode):

    def __init__( self ):

        super().__init__()
        self.start_node    = False
        self.final_node   = False
        self.node_id       = 0


class FAEdge(nlpregex.abs_graph.edge.BaseEdge):

    def __init__(self):
        super().__init__()
        self.in_token        = ""
        self.out_token       = ""

    def is_epsilon(self):
        return self.in_token == ""


class FA(nlpregex.abs_graph.graph.BaseGraph):

    def __init__(self):
        super().__init__()
        self.start_node  = None
        self.final_nodes = []
        self.re_balanced_token_patten = re.compile( r'^\[(PRE|POST) [0-9]+\]$' )


    def set_start_node( self, n ):
        self.start_node = n
        n.srart_node = True


    def get_start_node( self ):
        return self.start_node


    def remove_start_node( self ):
        if self.start_node:
            n = self.start_node
            n.srart_node = False
            return n
        else:
            return None


    def add_final_node( self, n ):
        self.final_nodes.append( n )
        n.final_node = True


    def first_final_node( self ):
        if len( self.final_nodes ) != 0:
            return self.final_nodes[0]
        else:
            return None

    def remove_final_nodes( self ):
        final_nodes_copy = self.final_nodes
        self.final_nodes = []
        for n in final_nodes_copy:
            n.final_node = False

        return final_nodes_copy


    def draw( self, comment_string, show_out_token = False, view_now = True, out_format = "svg" ):

        self.reassign_node_ids()

        g_dot = Digraph( comment = comment_string )
        g_dot.graph_attr['rankdir'] = 'LR'

        for n in self.nodes():

            label_out = str(n.node_id)

            if n in self.final_nodes:
                g_dot.node( str(n.node_id), label=label_out,  shape='doublecircle' )

            else:
                g_dot.node( str(n.node_id), label=label_out, shape='circle'        ) 


        for e in self.directed_edges():
            e.in_token
            in_token  = e.in_token.replace('"', '')
            out_token = e.out_token.replace('"', '')

            if in_token == "":
                in_token = "ε"
            if out_token == "":
                out_token = "ε"

            if show_out_token:
                label_out =  '"' +in_token + " / " + out_token + '"'
            else:
                label_out = '"' + in_token + '"'

            g_dot.edge( str(e.src_node.node_id), str(e.dst_node.node_id), label=label_out )

        for n in self.nodes():
            delattr( n, 'node_id' )

        g_dot.render( comment_string, view=view_now, format=out_format )


    def reassign_node_ids(self):

        node_id = 1
        for n in self.nodes():

            if n == self.start_node:
                n.node_id = 0
            else:
                n.node_id = node_id
                node_id += 1


    # This FA must be empty before calling this.
    # @param
    # lines   : List of phrases
    def from_flat_list( self, lines ):

        s_f_created = False

        lines = lines.split("\n")
        for line in lines:

            fields = line.strip().split()
            fields_cleaned = []
            for e in fields:
                if len(e)>0:
                    fields_cleaned.append(e)

            if len(fields_cleaned)== 1:

                if not s_f_created:

                    s = FANode()
                    s.add_to_graph(self)
                    self.set_start_node(s)    

                    f = FANode()
                    f.add_to_graph(self)
                    self.add_final_node(f)

                    s_f_created = True

                e = FAEdge()
                e.in_token   = fields[0]
                e.out_token  = fields[0]
            
                e.add_to_graph( self, s, f, "directed" )

            elif len(fields_cleaned) > 1:

                if not s_f_created:

                    s = FANode()
                    s.add_to_graph(self)
                    self.set_start_node(s)    

                    f = FANode()
                    f.add_to_graph(self)
                    self.add_final_node(f)

                    s_f_created = True

                prev_node = s

                for i in range(0, len(fields_cleaned)-1):

                    n = FANode()
                    n.add_to_graph(self)
                    
                    e = FAEdge()
                    e.in_token   = fields_cleaned[i]
                    e.out_token  = fields_cleaned[i]
                    e.add_to_graph( self, prev_node, n, "directed" )

                    prev_node = n

                e = FAEdge()
                e.in_token   = fields_cleaned[-1]
                e.out_token  = fields_cleaned[-1]
                e.add_to_graph( self, prev_node, f, "directed" )

        self.reassign_node_ids()


    #
    # Generates file contents that describes this FA for OpenFST.
    #
    # @param retain_balanced_in_token : 
    #           True  : in_token is passed as is.
    #           False : if in_token matches '^\[(PRE|POST) [0-9]+\]$'
    #                   then it will be replaced with ''
    #           This must be set to False for decoder.
    #
    # @return
    #
    # fst_str : file content for OpenFST in AT&T FSM format
    #           It consists of three parts. (Optional weights are not shown.)
    #
    #           First part. (Initial state and its transitions)
    #           0 <new state id> <open fst in_token> <open fst out_token>
    #
    #           Second part.
    #           <cur state id> <new state id> <open fst in_token> <open fst out_token>
    #
    #           Third part
    #           <final state>
    #           NOTE: Id 0 is reserved for the initial state.
    #
    # fst_sym_in_str  : file content for OpenFST symbol table for in tokens.
    # fst_sym_out_str : file content for OpenFST symbol table for out tokens.
    #           Format:
    #           <open fst token> <token ID>
    #           NOTE: ID 0 is reserved for epsilon transition.
    #
    # real_sym_in_str :  file content to convert OpenFST token ID to the real token ID
    # real_sym_out_str : file content to convert OpenFST token ID to the real token ID
    #           Format:
    #           <open fst token><TAB><real token>
    #           NOTE: Those last two files are needed for re_tool.FA.FA to restore info.
    #
    # NOTE The reason for the last two files is to avoid potential issues around
    #      unicodes in OpenFST.
    #
    def to_open_fst( self, retain_balanced_in_token = True ):
        self.reassign_node_ids()

        # Create symbol tables.
        # As OpenFST does not handle unicode well, we 
        # arrenge two tables for each of in_tokens and out_tokens.
        sym_map_in  , sym_id_in  = self.create_in_token_map()
        sym_map_out , sym_id_out = self.create_out_token_map()

        fst_str = self.create_fst_file( sym_map_in, sym_map_out, retain_balanced_in_token )

        fst_sym_in_str  , real_sym_in_str  = self.create_in_sym_files ( sym_map_in,  sym_id_in  )
        fst_sym_out_str , real_sym_out_str = self.create_out_sym_files( sym_map_out, sym_id_out )

        return [ fst_str, fst_sym_in_str, fst_sym_out_str, real_sym_in_str, real_sym_out_str ]

    #
    # Generates file contents that describes this FA for OpenFST.
    # It uses the symbol tables defined in another FA specified by fa_base
    #
    # @param real_sym_in_str  : file content to convert OpenFST token ID to the real token ID
    # @param real_sym_out_str : file content to convert OpenFST token ID to the real token ID
    #           Format:
    #           <open fst token><TAB><real token>
    #           NOTE: Those last two files are needed for re_tool.FA.FA to restore info.
    #
    # @return : file content for OpenFST in AT&T FSM format
    #
    # NOTE This implementation is not optimal.
    #
    def to_open_fst_using_existing_sym_map( self, real_sym_in_str, real_sym_out_str, retain_balanced_in_token = False ):

        self.reassign_node_ids()

        real_to_openfst_in  = self.create_reverse_token_map_from_string( real_sym_in_str )
        real_to_openfst_out = self.create_reverse_token_map_from_string( real_sym_in_str )

        out_str = ''

        # First part
        # cur_state new_state in_token/out_token
        # We don't use real tokens store in in_token and out_token
        # to avoid unicode related issues in OpenFST.
        # Instead, we use ID also as symbol.
        for e in self.directed_edges():
            if e.src_node.node_id == 0:
                out_str += str(e.src_node.node_id)
                out_str += "\t"
                out_str += str(e.dst_node.node_id)
                out_str += "\t"

                if retain_balanced_in_token:
                    out_str += real_to_openfst_in[ e.in_token  ]

                elif not re.match( self.re_balanced_token_patten, e.in_token ):
                    out_str += real_to_openfst_in[ e.in_token  ]

                else:
                    # Epsilon
                    out_str += real_to_openfst_in[ '' ]

                out_str += "\t"
                out_str += real_to_openfst_out[ e.out_token  ]
                out_str += "\n"

        # Second part
        for e in self.directed_edges():
            if e.src_node.node_id != 0:
                out_str += str(e.src_node.node_id)
                out_str += "\t"
                out_str += str(e.dst_node.node_id)
                out_str += "\t"

                if retain_balanced_in_token:
                    out_str += real_to_openfst_in[ e.in_token  ]

                elif not re.match( self.re_balanced_token_patten, e.in_token ):
                    out_str += real_to_openfst_in[ e.in_token  ]

                else:
                    # Epsilon
                    out_str += real_to_openfst_in[ '' ]

                out_str += "\t"
                out_str += real_to_openfst_out[ e.out_token  ]
                out_str += "\n"


        # Third part
        # List of final states.
        for f in self.final_nodes:
            out_str += str(f.node_id)
            out_str += "\n"
        return out_str



    # This FA must be empty before calling this.
    # @param
    # fst     : OpenFST file (text version, not compiled binary version.)
    # sym_in  : Real symbol file content for in_tokens   
    # sym_out : Real symbol file content for out_tokens

    def from_open_fst( self, fst, sym_in, sym_out ):

        fst_cleaned     = self.remove_comments(fst)
        sym_in_cleaned  = self.remove_comments(sym_in)
        sym_out_cleaned = self.remove_comments(sym_out)
        
        sym_map_in  = self.create_token_map_from_string(sym_in_cleaned)
        sym_map_out = self.create_token_map_from_string(sym_out_cleaned)

        node_set, final_node_set = self.get_node_sets_from_fst_file(fst_cleaned)

        node_map = {}
        for id in node_set:
            n = FANode()
            n.add_to_graph(self)
            node_map[id] = n
            if id == 0:
                self.start_node = n

            if id in final_node_set:
                self.final_nodes.append(n)

        edge_list = self.get_edge_list_from_fst_file(fst_cleaned)

        for quad in edge_list:        
            src_id            = int(quad[0])
            dst_id            = int(quad[1])
            openfst_in_token  = quad[2]
            openfst_out_token = quad[3]            

            e = FAEdge()
            e.in_token   = sym_map_in  [ openfst_in_token  ]
            e.out_token  = sym_map_out [ openfst_out_token ]
            
            e.add_to_graph( self, node_map[src_id], node_map[dst_id], "directed" )

        self.reassign_node_ids()

    # Create two sym files. One for OpenFST, the other for real mapping
    #
    # Open FST symbol file format: 
    #      <open fst token> <id>
    #
    # Real symbol file format
    #      <open fst token><TAB><real token>
    #
    def create_in_sym_files( self, sym_map, max_id_plus_one ):

        out_str_fst = ''
        out_str_fst += (SYM_EPSILON + " 0\n")
        for i in range (1, max_id_plus_one):
            out_str_fst += self.open_fst_in_sym_from_id( i )
            out_str_fst += "\t"
            out_str_fst += str( i )
            out_str_fst += "\n"


        out_str_real = ''
        for k in sym_map:
            out_str_real += self.open_fst_in_sym_from_id( sym_map[k] )
            out_str_real += "\t"
            out_str_real += k
            out_str_real += "\n"

        return out_str_fst, out_str_real


    def create_out_sym_files( self, sym_map, max_id_plus_one ):

        out_str_fst = ''
        out_str_fst += (SYM_EPSILON + " 0\n")
        for i in range (1, max_id_plus_one):
            out_str_fst += self.open_fst_out_sym_from_id( i )
            out_str_fst += "\t"
            out_str_fst += str( i )
            out_str_fst += "\n"


        out_str_real = ''
        for k in sym_map:
            out_str_real += self.open_fst_out_sym_from_id( sym_map[k] )
            out_str_real += "\t"
            out_str_real += k
            out_str_real += "\n"

        return out_str_fst, out_str_real


    def create_fst_file( self, sym_map_in, sym_map_out, retain_balanced_in_token = True  ):

        out_str = ''

        # First part
        # cur_state new_state in_token/out_token
        # We don't use real tokens store in in_token and out_token
        # to avoid unicode related issues in OpenFST.
        # Instead, we use ID also as symbol.
        for e in self.directed_edges():
            if e.src_node.node_id == 0:
                out_str += str(e.src_node.node_id)
                out_str += "\t"
                out_str += str(e.dst_node.node_id)
                out_str += "\t"

                if retain_balanced_in_token:
                    out_str += self.open_fst_in_sym_from_id( sym_map_in [ e.in_token  ] )

                elif not re.match( self.re_balanced_token_patten, e.in_token ):
                    out_str += self.open_fst_in_sym_from_id( sym_map_in [ e.in_token  ] )

                else:
                    # Epsilon
                    out_str += self.open_fst_in_sym_from_id( sym_map_in [ '' ] )

                out_str += "\t"
                out_str += self.open_fst_out_sym_from_id( sym_map_out[ e.out_token ] )
                out_str += "\n"

        # Second part
        for e in self.directed_edges():
            if e.src_node.node_id != 0:
                out_str += str(e.src_node.node_id)
                out_str += "\t"
                out_str += str(e.dst_node.node_id)
                out_str += "\t"

                if retain_balanced_in_token:
                    out_str += self.open_fst_in_sym_from_id( sym_map_in [ e.in_token  ] )

                elif not re.match( self.re_balanced_token_patten, e.in_token ):
                    out_str += self.open_fst_in_sym_from_id( sym_map_in [ e.in_token  ] )

                else:
                    # Epsilon
                    out_str += self.open_fst_in_sym_from_id( sym_map_in [ '' ] )

                out_str += "\t"
                out_str += self.open_fst_out_sym_from_id( sym_map_out[ e.out_token ] )
                out_str += "\n"

        # Third part
        # List of final states.
        for f in self.final_nodes:
            out_str += str(f.node_id)
            out_str += "\n"
        return out_str


    # k : token v(string): id (integer)
    def create_in_token_map(self):

        sym_map = {}
        token_id = 1
        sym_map[""] = 0 # epsilon
        for e in self.directed_edges():
            if not e.in_token in sym_map:
                sym_map[e.in_token]= token_id
                token_id += 1

        # map, the max id + 1
        return sym_map, token_id 


    def create_out_token_map(self):

        sym_map = {}
        token_id = 1
        sym_map[""] = 0 # epsilon
        for e in self.directed_edges():
            if not e.out_token in sym_map:
                sym_map[e.out_token]= token_id
                token_id += 1

        # map, the max id + 1
        return sym_map, token_id


    # k : open fst token v: real token
    def create_token_map_from_string( self, sym_str ):
        sym_map = {}
        lines = sym_str.split("\n")
        for line in lines:
            if line == '':
                continue
            fields = line.strip().split("\t")
            if len(fields) == 2:
                openfst_sym = fields[0]
                real_sym    = fields[1]
                sym_map[openfst_sym] = real_sym
            elif len(fields) == 1:
                openfst_sym = fields[0]
                sym_map[openfst_sym] = ""


        return sym_map


    def create_reverse_token_map_from_string( self, sym_str ):
        sym_map = {}
        lines = sym_str.split("\n")
        for line in lines:
            if line == '':
                continue

            fields = line.strip().split("\t")
            if len(fields) == 2:
                openfst_sym = fields[0]
                real_sym    = fields[1]
                sym_map[real_sym] = openfst_sym
            elif len(fields) == 1:
                openfst_sym = fields[0]
                sym_map[''] = openfst_sym


        return sym_map


    def get_node_sets_from_fst_file( self, fst ):

        node_set       = set()
        final_node_set = set()
        lines = fst.split("\n")
        for line in lines:
            fields = line.strip().split("\t")
            if len(fields) >= 4:
                node_set.add( int(fields[0]) )
                node_set.add( int(fields[1]) )

            elif len(fields) >= 1 and fields[0]:
                node_set.add( int(fields[0]) )
                final_node_set.add( int(fields[0]) )

        return node_set, final_node_set


    def open_fst_in_sym_from_id( self, id ):

         if id == 0:
             return SYM_EPSILON

         else:
             return "in_sym{:08d}".format(id)

    def open_fst_out_sym_from_id( self, id ):

         if id == 0:
             return SYM_EPSILON

         else:
             return "out_sym{:08d}".format(id)



    def get_id_from_open_fst_sym( self, sym_str ):

        if sym_str == SYM_EPSILON:
            return 0

        else:
            num_part = re.sub( r'(in|out)_sym0+', '', sym_str)
            return int(num_part)

    def get_edge_list_from_fst_file( self, fst ):

        edge_list = []
        lines = fst.split('\n')

        for line in lines:
            fields = line.strip().split("\t")
            if len(fields) >= 2:
                quad = []
                quad.append(int(fields[0]))
                quad.append(int(fields[1]))
                quad.append(fields[2])
                quad.append(fields[3])
                edge_list.append(quad)

        return edge_list
 

    # Removes /**/, //... and #...
    # Comments can be best handled separately from the parser.
    def remove_comments( self, s ):

        def replacer(match):
            s = match.group(0)
            if s.startswith('/'):
                return " "
            elif s.startswith('#'):
                return ""
            else:
                return s

        pattern = re.compile(
            r'^#.*?$|//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        return re.sub(pattern, replacer, s)



# Make a FA that has only one epsilon transition from s to f.
def make_unit_epsilon():

    g_new = FA()

    s_new = FANode() # start node
    f_new = FANode() # final node

    s_new.add_to_graph( g_new )
    f_new.add_to_graph( g_new )

    e = FAEdge()
    e.in_token = ""
    e.out_token = ""
    e.add_to_graph( g_new, s_new, f_new, "directed" )

    g_new.set_start_node( s_new )
    g_new.add_final_node( f_new )

    g_new.reassign_node_ids()
    return g_new


def make_unit_transition( in_token, out_token ):

    g_new = FA()

    s_new = FANode() # start node
    f_new = FANode() # final node

    s_new.add_to_graph( g_new )
    f_new.add_to_graph( g_new )

    e = FAEdge()
    e.in_token  = in_token
    e.out_token = out_token
    e.add_to_graph( g_new, s_new, f_new, "directed" )

    g_new.set_start_node( s_new )
    g_new.add_final_node( f_new )

    g_new.reassign_node_ids()
    return g_new


def unify_nodes_start_and_final( g, f, s ):

    E  = s.out_neighbors()
    AN = [ e.other_node_of(s) for e in E ]
    s.remove_from_graph()

    for i in range( 0, len(E) ):
        E[i].add_to_graph( g, f, AN[i], "directed" )


def unify_nodes_two_starts( g, s_retain, s_discarded ):

    E  = s_discarded.out_neighbors()
    AN = [ e.other_node_of(s_discarded) for e in E ]
    s_discarded.remove_from_graph()

    for i in range( 0, len(E) ):
        E[i].add_to_graph( g, s_retain, AN[i], "directed" )


def unify_nodes_two_finals( g, f_retain, f_discarded ):

    E  = f_discarded.in_neighbors()
    AN = [ e.other_node_of(f_discarded) for e in E ]
    f_discarded.remove_from_graph()

    for i in range( 0, len(E) ):
        E[i].add_to_graph( g, AN[i], f_retain, "directed" )


# Concatenate the TTSP graphs in the list S serially.
def ttsp_concatenate( S ):

    g_new = FA()

    # Transfer the nodes and edges of S to g_new
    for g in S:
        g_new.transfer_from( g )

    # Af this point g.start_node and g.final_nodes
    # still hold valid nodes.
    g_new.set_start_node  ( S[ 0].get_start_node()   )
    g_new.add_final_node  ( S[-1].first_final_node() )

    current_final_node = S[ 0].first_final_node()

    for g in S[1:]:

        # f: current_final_node
        # s: g.start_node
        # -->            -->       -->    -->
        #    \          /             \  /
        # ---->(f)...(s)--->    => ---->f--->
        #    /          \             /  \
        # -->            -->       -->    -->
        unify_nodes_start_and_final( g_new, current_final_node, g.get_start_node() )

        current_final_node = g.first_final_node()

        g.remove_start_node()
        g.remove_final_nodes()

    g_new.reassign_node_ids()

    return g_new


# Bundle the TTSP graphs in the list P in parallel
def ttsp_bundle( P ):

    g_new = FA()

    # Transfer the nodes and edges of S to g_new
    for g in P:
        g_new.transfer_from( g )

    s_new = FANode() # start node
    f_new = FANode() # final node

    s_new.add_to_graph(g_new)
    f_new.add_to_graph(g_new)

    g_new.set_start_node( s_new )
    g_new.add_final_node( f_new )

    for g in P:

        # s: g.start_node
        #        +------->                +------->
        # s_new -+------->                +------->
        #        +------->                +------->
        #                     =>   s_new -+
        #        +------->                +------->
        #     s -+------->                +------->
        #        +------->                +------->
        unify_nodes_two_starts ( g_new, s_new, g.get_start_node()   )
        unify_nodes_two_finals ( g_new, f_new, g.first_final_node() )

        g.remove_start_node()
        g.remove_final_nodes()

    g_new.reassign_node_ids()

    return g_new


#      
#      ________                          ________
#     /        \                        /        \
#    s----------f  =>   s_new -<eps>-> s----------f -<eps>-> f_new
#     \________/           |           ^\________/|            ^
#                          |           |          |            |
#                          |            --<eps>---             |
#                           --------------<eps>----------------
#                                         ('*')
#
def enclose_in_cycle( g, plus_or_star ):

    s_new = FANode() # start node
    f_new = FANode() # final node

    s_new.add_to_graph(g)
    f_new.add_to_graph(g)

    e = FAEdge()
    e.in_token = ""
    e.out_token = ""
    e.add_to_graph( g, s_new, g.start_node, "directed" )

    for f in g.final_nodes:
        e = FAEdge()
        e.in_token = ""
        e.out_token = ""
        e.add_to_graph( g, f, f_new,"directed" )

        e_back = FAEdge()
        e_back.in_token = ""
        e_back.out_token = ""
        e_back.add_to_graph( g, f, g.start_node, "directed" )

    g.start_node = s_new
    g.final_nodes = [f_new]
        
    if plus_or_star == '*':
        e = FAEdge()
        e.in_token = ""
        e.out_token = ""
        e.add_to_graph( g, s_new, f_new, "directed" )

    return g


# Generates an equivalent DFA from given NFA
# It assumes the availability of the following commands and libs from OpenFST.
# - fstcompile
# - fstdeterminize
# - fstrmepsilon
# - fstminimize
# - fstprint
#
# @param nfa       : input NFA
# @param optimize  : True if you want to run fstminimize 
#                    it will change the relative position of output token
#                    relative to the input token.
def DFA_from_NFA( nfa , optimize = False):

    nfa_contents = nfa.to_open_fst( retain_balanced_in_token = True )

    nfa_fst_str      = nfa_contents[0]
    fst_sym_in_str   = nfa_contents[1]
    fst_sym_out_str  = nfa_contents[2]
    real_sym_in_str  = nfa_contents[3]
    real_sym_out_str = nfa_contents[4]
    
    with open( 'nfa_fst.txt', 'w', encoding='utf-8' ) as nfa_fst_fh:
        nfa_fst_fh.write( nfa_fst_str )

    with open( 'fst_sym_in.txt',  'w',  encoding='utf-8' ) as fst_sym_in_fh:
        fst_sym_in_fh.write( fst_sym_in_str )

    with open( 'fst_sym_out.txt',  'w', encoding='utf-8' ) as fst_sym_out_fh:
        fst_sym_out_fh.write( fst_sym_out_str )

    subprocess.run([ "fstcompile", "--isymbols=fst_sym_in.txt",  "--osymbols=fst_sym_out.txt",  "nfa_fst.txt", "nfa.fst" ])
    subprocess.run([ "fstdeterminize", "nfa.fst",            "dfa.fst"            ])
    subprocess.run([ "fstrmepsilon",   "dfa.fst",            "dfa_epsremoved.fst" ])

    if optimize:
        subprocess.run([ "fstminimize",    "dfa_epsremoved.fst", "dfa_minimized.fst"  ])
        subprocess.run([ "fstrmepsilon",   "dfa_minimized.fst",  "dfa_minimized_epsremoved.fst" ])
        subprocess.run([ "fstprint", "--isymbols=fst_sym_in.txt",  "--osymbols=fst_sym_out.txt",  "dfa_minimized.fst", "dfa_fst.txt" ])
    else:
        subprocess.run([ "fstprint", "--isymbols=fst_sym_in.txt",  "--osymbols=fst_sym_out.txt",  "dfa_epsremoved.fst", "dfa_fst.txt" ])

    with open('dfa_fst.txt', 'r', encoding='utf-8') as dfa_fst_fh:
        dfa_fst_str = dfa_fst_fh.read()

    dfa = FA()

    dfa.from_open_fst( dfa_fst_str, real_sym_in_str, real_sym_out_str )

    os.remove( "nfa_fst.txt"        )
    os.remove( "nfa.fst"            )
    os.remove( "dfa.fst"            )
    os.remove( "dfa_epsremoved.fst" )
    if optimize:
        os.remove( "dfa_minimized.fst"  )
        os.remove( "dfa_minimized_epsremoved.fst"  )
    os.remove( "fst_sym_in.txt"     )
    os.remove( "fst_sym_out.txt"    )

    return dfa


# It decodes given sequence of input tokens 
# into a sequence of output tokens.
#
# It first creates a single-path FA (fa_input) that corresponds to
# the list of input tokes makking the output
# tokens the same as input.
# Then it composes FA (fa_base) into FA using OpenFST's fstcompose.
# The resultant FA (fa_output) will be either empty (not accepted)
# or a single path.
# If fa_output is not empty, it traverses fa_output to collect output tokens.
# 
# @param fa_base : FA
#
# @param in_tokens : list of input_tokens
#
# @return list of output_tokens
#         None if the input is not accepted
#
def decode( fa_base , in_tokens):

    sym_map_in , sym_id_in = fa_base.create_in_token_map()

    fa_list = []
    for t in in_tokens:

        if t in sym_map_in:
            fa_list.append( make_unit_transition( t, t ) )
        else:
            
            # Token not found in the symbol table
            # of fa_base. Rejecting
            return None


    fa_input = ttsp_concatenate( fa_list )

    fa_base_contents          = fa_base.to_open_fst( retain_balanced_in_token = False )
    fa_base_fst_str           = fa_base_contents[0]
    fa_base_fst_sym_in_str    = fa_base_contents[1]
    fa_base_fst_sym_out_str   = fa_base_contents[2]
    fa_base_real_sym_in_str   = fa_base_contents[3]
    fa_base_real_sym_out_str  = fa_base_contents[4]

    fa_input_fst_str = fa_input.to_open_fst_using_existing_sym_map( fa_base_real_sym_in_str, fa_base_real_sym_out_str, retain_balanced_in_token = False )

    with open( 'fa_base_fst.txt',  'w', encoding='utf-8' ) as fa_base_fst_fh:
        fa_base_fst_fh.write( fa_base_fst_str )

    with open( 'fst_sym_in.txt',   'w', encoding='utf-8' ) as fst_sym_in_fh:
        fst_sym_in_fh.write( fa_base_fst_sym_in_str )

    with open( 'fst_sym_out.txt',  'w', encoding='utf-8' ) as fst_sym_out_fh:
        fst_sym_out_fh.write( fa_base_fst_sym_out_str )

    with open( 'fa_input_fst.txt', 'w', encoding='utf-8' ) as fa_input_fst_fh:
        fa_input_fst_fh.write( fa_input_fst_str )

    subprocess.run([ "fstcompile", "--isymbols=fst_sym_in.txt", "--osymbols=fst_sym_out.txt", "fa_base_fst.txt",  "fa_base.fst"  ])
    subprocess.run([ "fstcompile", "--isymbols=fst_sym_in.txt", "--osymbols=fst_sym_in.txt",  "fa_input_fst.txt", "fa_input.fst" ])
    subprocess.run([ "fstcompose", "fa_input.fst", "fa_base.fst", "fa_output.fst" ])
    subprocess.run([ "fstprint",   "--isymbols=fst_sym_in.txt",  "--osymbols=fst_sym_out.txt", "fa_output.fst", "fa_output_fst.txt" ])

    with open('fa_output_fst.txt', 'r', encoding='utf-8') as fa_output_fst_fh:
        fa_output_fst_str = fa_output_fst_fh.read()

    os.remove( "fa_base_fst.txt" )
    os.remove( "fa_base.fst" )
    os.remove( "fst_sym_in.txt" )
    os.remove( "fst_sym_out.txt" )
    os.remove( "fa_input_fst.txt" )
    os.remove( "fa_input.fst" )
    os.remove( "fa_output_fst.txt" )
    os.remove( "fa_output.fst" )

    fa_output = FA()

    fa_output.from_open_fst( fa_output_fst_str, fa_base_real_sym_in_str, fa_base_real_sym_out_str )

    if fa_output.num_nodes() == 0:
        return None

    cur_s = fa_output.start_node

    output_tokens = []
    while cur_s not in fa_output.final_nodes:
        edges  = cur_s.out_neighbors()
        e      = edges[0]
        next_s = e.other_node_of(cur_s)
        if e.out_token != '':
            output_tokens.append( e.out_token )
        cur_s = next_s

    return output_tokens        
    
