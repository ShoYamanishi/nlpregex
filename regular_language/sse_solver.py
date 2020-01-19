#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import nlpregex.abs_graph.double_link
import nlpregex.abs_graph.node
import nlpregex.abs_graph.edge
import nlpregex.abs_graph.graph
import nlpregex.regular_language.sse_forrest


# @brief represents one symbolic equation that consists of LHS = RHS.
#        LHS is a variable (state)
#        RHS is a set of terms
#        a term consists of pair of variable and its coefficent.
#        a coefficient is an AST
class SymbolicEquation():


    def __init__( self, lhs, forrest ):
        self.lhs     = lhs # state
        self.rhs     = {}  # k: state, v: coeff (top node of AST )
        self.forrest = forrest # sseAST
            

    # @brief adding coefficienct to the RHS
    #
    # @param  j       : column number
    # @param  symbols : list of terminals i.e., list of strings that represent numbers.
    #                   e.g. 't0', 't1', ... 't999999'
    #                   if there is only one terminal specified, the resultant AST is the terminal.
    #                   if there are multiple terminals, then the resultant AST represents a selection
    #                   whose children are the terminals.
    #                   if there is a coefficient already present, then the symbols are added under 
    #                   the existing selection.
    def add_coeff( self, j, param_symbols ):

        if j not in self.rhs:
            r = self.forrest.create_initial_union_node( param_symbols )
            self.rhs[j] = r

        else:        

            t1 = self.rhs[j] # Assume it is a term or a union

            t2 = self.forrest.create_initial_union_node( param_symbols )

            self.rhs[j] = self.forrest.union_two_ASTs( t1, t2 )


    # @brief remove the self recursion from RHS using Arden's rule s1 = Ls1 | Rs2 |Ts3  =>  s1 = L*Rs2 | L*Ts3
    def remove_self_recursion(self):

        if self.lhs in self.rhs:

            if self.rhs[self.lhs].ast_node_type == 'e':

                self.remove_term( self.lhs )

            else:
                L_clone = self.forrest.clone_AST( self.rhs[self.lhs] )
                L_star = self.forrest.repeat_AST( L_clone )

                for s in self.rhs:
                    if s != self.lhs:
                        L_star_clone = self.forrest.clone_AST(L_star)
                        self.rhs[s] = self.forrest.concat_two_ASTs( L_star_clone, self.rhs[s] )

                self.remove_term( self.lhs )
                self.forrest.remove_AST(L_star)


    # @brief prepend copy of L (AST) to each in RHS
    # @param L : root node of AST
    def prepend_coeff(self, L):

        if L.ast_node_type != 'e':

            for state in self.rhs:
                L_clone = self.forrest.clone_AST(L)
                self.rhs[state] = self.forrest.concat_two_ASTs( L_clone, self.rhs[state] )


    # @brief merge the RHS of the specified equation into this RHS as part of row elimination
    # @param eq2 : the equation (SymbolidEquation) whose RHS are merged into.
    #              eq2 is completely consumed by this function, meaning the caller do not have to
    #              remove the residual coefficients in RHS.
    def merge_into( self, eq2 ):
        eq2_vars = list(eq2.rhs.keys())
        for s2 in eq2_vars:
            if s2 in self.rhs:
                t1 = self.rhs[s2]
                t2 = eq2. rhs[s2]
                merged_term = self.forrest.union_two_ASTs( t1, t2 )
                self.rhs[s2] = merged_term

            else:
                self.rhs[s2] = eq2.rhs[s2]

            del eq2.rhs[s2]

        # remove remaining terms in eq2
        eq2.clean_RHS()


    # @brief make a clone of this equation.
    def clone( self ):

        eq_copy = SymbolicEquation( self.lhs, self.forrest )
        for k in self.rhs:
            eq_copy.rhs[k] = self.forrest.clone_AST( self.rhs[k] )

        return eq_copy


    # @brief clean up RHS (ASTs)
    def clean_RHS(self):
        keys = list(self.rhs.keys())
        for k in keys:
            self.remove_term( k )


    # @brief remove the specified term from the RHS.
    def remove_term( self, i ):
        self.forrest.remove_AST( self.rhs[ i ] )
        del self.rhs[ i ]


    def diag_str(self):

        out_str = ""
        out_str += "S" 
        out_str += '{:02d}'.format(self.lhs)
        out_str += " =\t"
        sorted_keys = sorted( list( self.rhs.keys() ) )
        first = True
        for k in sorted_keys:

            if first:
                first = False

            else:
                out_str += " | "
            out_str += self.rhs[k].regex
            out_str += " S"
            out_str += '{:02d}'.format(k)

        return out_str

#
# @brief solve a set of simultaneous symbolic equations to transform
#        a finite automaton to an abstract syntax tree.
#        the variables are identified by an integer.
#        the coeffiients for the variables are represented 
#        by regular expressions in sseASForrest.
#        this solver uses the following types of nodes.
#        - selection/union   f     'u'
#        - sequence/concatenation  's'
#        - repetition              '*' 
#        - epsilon                 'e'
#        - alphabet (terminal)     't1'--'t9999999' (positive number in string)
#
#        Each equation has the following form.
#        V0 = C1 V1 | C2 V2 | ... | Cx Vx
#        V0 : variable on LHS
#        Ci : coefficient for variable Vi on RHS
#
class SymbolicSimultaneousEquations():


    # @param diag : if True, it generates diagnostics/debug info to console
    def __init__(self, diag = False):

        self.rows        = {} # k: state, v: equation
        self.start_state = -1
        self.final_state = -1
        self.forrest     = nlpregex.regular_language.sse_forrest.sseASForrest()
        self.diag        = diag


    # @brief adding coefficienct on the RHS of the specified equation
    #
    # @param  i       : row/equation number.
    # @param  j       : column number
    # @param  symbols : list of terminals i.e., list of strings that represent numbers.
    #                   e.g. 't0', 't1', ... 't999999'
    #                   if there is only one terminal specified, the resultant AST is the terminal.
    #                   if there are multiple terminals, then the resultant AST represents a selection
    #                   whose children are the terminals.
    #                   if there is a coefficient already present, then the symbols are added under 
    #                   the existing selection.
    def add_coeff( self, i, j, symbols ):

        if i not in self.rows:
            self.rows[i] = SymbolicEquation( i, self.forrest )

        if j not in self.rows:
            self.rows[j] = SymbolicEquation( j, self.forrest )

        self.rows[i].add_coeff( j, symbols )


    # @brief solve the equations into an AST
    #
    # @param  s : start variable in integer
    # @param  F : list of final variables in integer
    #
    # @return an AST in sseAST.
    def solve( self, s, F):

        # s : start state
        # F : set of final states
        # returns the single resultant regex.

        self.start_state = self.max_index() + 1

        self.rows[ self.start_state ] = SymbolicEquation( self.start_state, self.forrest )

        self.add_coeff( self.start_state, s, ['e'] )

        self.final_state = self.start_state + 1

        for f in F:
            self.add_coeff( f, self.final_state, ['e'] )

        if self.diag:
            print ("Initial State:")
            print (self.diag_str())

        while len(self.rows) > 2:
            if self.diag:
                print ( "Beginning of outer loop num rows: " + str(len(self.rows)) )

            keys = list(self.rows.keys())
            for i in keys:
                if i != self.start_state and i != self.final_state :
 
                   self.eliminate_row( i )

        # At this point only two rows for self.start_state and self.final_state exist.
        # The row for start state has only one coefficient for self.final_state
        # The row for final state has been always empty.
        final_coeff = self.rows[ self.start_state ].rhs[ self.final_state ]

        self.forrest.remove_epsilons_from_unions( final_coeff )

        self.forrest.create_tree_root_for_reduction( final_coeff ) 

        return self.forrest


    # @brief remove this row from the equations.
    #        this is similar to gaussuan elimination.
    def eliminate_row( self, i ):

        if self.diag:
            print ("Eliminate row " + str(i))
            print (self.diag_str())

        self.rows[i].remove_self_recursion()

        if self.diag:
            print ("After self-recursion")
            print (self.diag_str())


        for j in self.rows:
            if i != j:
                self.substitute(i, j)

        # remove all the ASTs from the row[i] and then remove the row itself.
        self.rows[i].clean_RHS()
        del self.rows[i]

        if self.diag:
            print ("After row-elimination of " + str(i))
            print (self.diag_str())


    # @brief substitute the term i in row j with row i.
    def substitute( self, i, j ):

        if self.diag:
            print ("Substitute " + str(i) + " into " + str(j) )

        row_j = self.rows[j]

        if i in row_j.rhs:

            row_i_copy = self.rows[i].clone()
            coeff_ji   = row_j.rhs[i]

            row_i_copy.prepend_coeff( coeff_ji )

            row_j.merge_into( row_i_copy )

            row_j.remove_term( i )


        if self.diag:
            print ("After substitution")
            print (self.rows[j].diag_str())


    def max_index( self ):

        max_row = 0
        for i in self.rows:
            max_row = max(i,max_row)
        return max_row


    def diag_str(self):

        out_str = ""
        out_str += 'Start: S{:02d}'.format(self.start_state)
        out_str += "\n"
        out_str += 'Final: S{:02d}'.format(self.final_state)
        out_str += "\n"       
        for i in self.rows:
            row = self.rows[i]
            out_str += row.diag_str()
            out_str += "\n"
        return out_str
