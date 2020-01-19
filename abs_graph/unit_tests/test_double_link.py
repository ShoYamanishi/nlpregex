#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Unit Tests for Doubly linked list."""

import unittest
import nlpregex.abs_graph.double_link

class dummy_obj:
    pass


class test_ElemDelegate( unittest.TestCase ):

    def test_constructor(self):

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )
        self.assertEqual ( delg01.elem , elem01 )


    def test_link_this_before(self):

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        delg01.link_this_before( delg02 )

        self.assertEqual ( delg01.elem , elem01 )
        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.elem , elem02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertIsNone( delg02.next )


    def test_unlink_next_delg(self):

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        delg01.link_this_before( delg02 )        

        delg01.unlink_next_delg()

        self.assertEqual ( delg01.elem , elem01 )
        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertEqual ( delg02.elem , elem02 )
        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )


    def test_link_this_after(self):

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        delg01.link_this_after( delg02 )

        self.assertEqual ( delg02.elem , elem02 )
        self.assertIsNone( delg02.prev )
        self.assertEqual ( delg02.next, delg01 )

        self.assertEqual ( delg01.elem , elem01 )
        self.assertEqual ( delg01.prev, delg02 )
        self.assertIsNone( delg01.next )


    def test_unlink_prev_delg(self):

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        delg01.link_this_after( delg02 )

        delg01.unlink_prev_delg()

        self.assertEqual ( delg01.elem , elem01 )
        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertEqual ( delg02.elem , elem02 )
        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )


    def test_clean_refs(self):

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )
        delg01.prev = elem01
        delg01.next = elem01

        delg01.clean_refs()

        self.assertIsNone( delg01.elem )
        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )



class testList( unittest.TestCase ):

    def test_constructor(self):

        list01 = nlpregex.abs_graph.double_link.List()

        self.assertIsNone( list01.head )
        self.assertIsNone( list01.tail )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 0 )


    def test_inc_num_elems(self):

        list01 = nlpregex.abs_graph.double_link.List()
        list01.num_elems = 123

        list01.inc_num_elems()

        self.assertEqual ( list01.num_elems, 124 )


    def test_inc_num_elems_from_minus_1_to_0(self):

        list01 = nlpregex.abs_graph.double_link.List()
        list01.num_elems = -1

        list01.inc_num_elems()

        self.assertEqual ( list01.num_elems, 0 )


    def test_inc_num_elems_from_0_to_plus_1(self):

        list01 = nlpregex.abs_graph.double_link.List()
        list01.num_elems = 0

        list01.inc_num_elems()

        self.assertEqual ( list01.num_elems, 1 )


    def test_dec_num_elems(self):

        list01 = nlpregex.abs_graph.double_link.List()
        list01.num_elems = 123

        list01.dec_num_elems()

        self.assertEqual ( list01.num_elems, 122 )


    def test_dec_num_elems_from_plus_1_to_0(self):

        list01 = nlpregex.abs_graph.double_link.List()
        list01.num_elems = 1

        list01.dec_num_elems()

        self.assertEqual ( list01.num_elems, 0 )


    def test_dec_num_elems_from_0_to_minus_1(self):

        list01 = nlpregex.abs_graph.double_link.List()
        list01.num_elems = 0

        list01.dec_num_elems()

        self.assertEqual ( list01.num_elems, -1 )


    def test_append_head_empty(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_head( delg01 )
        
        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg01 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 1 )

        self.assertIsNone( delg01.next )
        self.assertIsNone( delg01.prev )


    def test_append_head_one_delg(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_head( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_head( delg02 )

        self.assertEqual ( list01.head, delg02 )
        self.assertEqual ( list01.tail, delg01 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertIsNone( delg02.prev )
        self.assertEqual ( delg02.next, delg01 )
        self.assertEqual ( delg01.prev, delg02 )
        self.assertIsNone( delg01.next )


    def test_append_head_two_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_head( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_head( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_head( delg03 )

        self.assertEqual ( list01.head, delg03 )
        self.assertEqual ( list01.tail, delg01 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 3 )

        self.assertIsNone( delg03.prev )
        self.assertEqual ( delg03.next, delg02 )
        self.assertEqual ( delg02.prev, delg03 )
        self.assertEqual ( delg02.next, delg01 )
        self.assertEqual ( delg01.prev, delg02 )
        self.assertIsNone( delg01.next )


    def test_append_tail_empty(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_head( delg01 )
        
        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg01 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 1 )

        self.assertIsNone( delg01.next )
        self.assertIsNone( delg01.prev )


    def test_append_tail_one_delg(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg02 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertIsNone( delg02.next )


    def test_append_tail_two_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg03 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 3 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )
        self.assertEqual ( delg03.prev, delg02 )
        self.assertIsNone( delg03.next )


    def test_remove_head_empty(self):

        list01 = nlpregex.abs_graph.double_link.List()

        rtn01 = list01.remove_head()

        self.assertIsNone( list01.head )
        self.assertIsNone( list01.tail )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 0 )

        self.assertIsNone( rtn01 )


    def test_remove_head_one_delg(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        rtn01 = list01.remove_head()

        self.assertIsNone( list01.head )
        self.assertIsNone( list01.tail )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 0 )

        self.assertEqual ( rtn01, delg01 )
        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )


    def test_remove_head_two_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        rtn01 = list01.remove_head()

        self.assertEqual( list01.head, delg02 )
        self.assertEqual( list01.tail, delg02 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 1 )

        self.assertEqual ( rtn01, delg01 )
        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )


    def test_remove_head_three_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        rtn01 = list01.remove_head()

        self.assertEqual( list01.head, delg02 )
        self.assertEqual( list01.tail, delg03 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertEqual ( rtn01, delg01 )
        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertIsNone( delg02.prev )
        self.assertEqual ( delg02.next, delg03 )
        self.assertEqual ( delg03.prev, delg02 )
        self.assertIsNone( delg03.next )


    def test_remove_tail_empty(self):

        list01 = nlpregex.abs_graph.double_link.List()

        rtn01 = list01.remove_tail()

        self.assertIsNone( list01.head )
        self.assertIsNone( list01.tail )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 0 )

        self.assertIsNone( rtn01 )


    def test_remove_tail_one_delg(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        rtn01 = list01.remove_tail()

        self.assertIsNone( list01.head )
        self.assertIsNone( list01.tail )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 0 )

        self.assertEqual ( rtn01, delg01 )
        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )


    def test_remove_tail_two_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        rtn01 = list01.remove_tail()

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg01 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 1 )

        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertEqual ( rtn01, delg02 )
        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )


    def test_remove_head_three_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        rtn01 = list01.remove_tail()

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg02 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertEqual ( rtn01, delg03 )
        self.assertIsNone( delg03.prev )
        self.assertIsNone( delg03.next )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertIsNone( delg02.next )


    def test_remove_one_delg(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        list01.remove(delg01)

        self.assertIsNone( list01.head )
        self.assertIsNone( list01.tail )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 0 )

        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )


    def test_remove_two_delgs_head(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        list01.remove(delg01)

        self.assertEqual( list01.head, delg02 )
        self.assertEqual( list01.tail, delg02 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 1 )

        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )


    def test_remove_two_delgs_tail(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        list01.remove(delg02)

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg01 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 1 )

        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )


    def test_remove_three_delgs_head(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        list01.remove(delg01)

        self.assertEqual( list01.head, delg02 )
        self.assertEqual( list01.tail, delg03 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertIsNone( delg02.prev )
        self.assertEqual ( delg02.next, delg03 )
        self.assertEqual ( delg03.prev, delg02 )
        self.assertIsNone( delg03.next )


    def test_remove_three_delgs_mid(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        list01.remove(delg02)

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg03 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg03 )
        self.assertEqual ( delg03.prev, delg01 )
        self.assertIsNone( delg03.next )


    def test_remove_three_delgs_tail(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        list01.remove(delg03)

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg02 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertIsNone( delg03.prev )
        self.assertIsNone( delg03.next )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertIsNone( delg02.next )


    def test_remove_five_delgs_head(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        list01.remove(delg01)

        self.assertEqual( list01.head, delg02 )
        self.assertEqual( list01.tail, delg05 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 4 )

        self.assertIsNone( delg01.prev )
        self.assertIsNone( delg01.next )

        self.assertIsNone( delg02.prev )
        self.assertEqual ( delg02.next, delg03 )
        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg04 )
        self.assertEqual ( delg04.prev, delg03 )
        self.assertEqual ( delg04.next, delg05 )
        self.assertEqual ( delg05.prev, delg04 )
        self.assertIsNone( delg05.next )


    def test_remove_five_delgs_2nd(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        list01.remove(delg02)

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg05 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 4 )

        self.assertIsNone( delg02.prev )
        self.assertIsNone( delg02.next )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg03 )
        self.assertEqual ( delg03.prev, delg01 )
        self.assertEqual ( delg03.next, delg04 )
        self.assertEqual ( delg04.prev, delg03 )
        self.assertEqual ( delg04.next, delg05 )
        self.assertEqual ( delg05.prev, delg04 )
        self.assertIsNone( delg05.next )


    def test_remove_five_delgs_3rd(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        list01.remove(delg03)

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg05 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 4 )

        self.assertIsNone( delg03.prev )
        self.assertIsNone( delg03.next )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg04 )
        self.assertEqual ( delg04.prev, delg02 )
        self.assertEqual ( delg04.next, delg05 )
        self.assertEqual ( delg05.prev, delg04 )
        self.assertIsNone( delg05.next )


    def test_remove_five_delgs_4th(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        list01.remove(delg04)

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg05 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 4 )

        self.assertIsNone( delg04.prev )
        self.assertIsNone( delg04.next )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )
        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg05 )
        self.assertEqual ( delg05.prev, delg03 )
        self.assertIsNone( delg05.next )


    def test_remove_five_delgs_tail(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        list01.remove(delg05)

        self.assertEqual( list01.head, delg01 )
        self.assertEqual( list01.tail, delg04 )

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 4 )

        self.assertIsNone( delg05.prev )
        self.assertIsNone( delg05.next )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )
        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )
        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg04 )
        self.assertEqual ( delg04.prev, delg03 )
        self.assertIsNone( delg04.next )


    def test_cnt(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        rtn01 = list01.cnt()

        self.assertEqual( rtn01, 5 )


    def test___iter__empty(self):

        list01 = nlpregex.abs_graph.double_link.List()

        rtn01 = list01.__iter__()
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( rtn01,                    list01 )

    def test___iter__one_delg(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        rtn01 = list01.__iter__()

        self.assertEqual ( list01.current_iteration, delg01 )
        self.assertEqual ( rtn01,                    list01 )


    def test___iter__two_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        rtn01 = list01.__iter__()

        self.assertEqual ( list01.current_iteration, delg01 )
        self.assertEqual ( rtn01,                    list01 )


    def test___next__one_delg(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        iter01 = list01.__iter__()

        rtn01 = iter01.__next__()

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( iter01, list01 )
        self.assertEqual ( rtn01,  elem01 )

        self.assertRaises(StopIteration , iter01.__next__)


    def test___next__two_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        iter01 = list01.__iter__()
        self.assertEqual ( iter01, list01 )

        rtn01 = iter01.__next__()

        self.assertEqual ( list01.current_iteration , delg02 )
        self.assertEqual ( rtn01, elem01 )

        rtn02 = iter01.__next__()

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( rtn02, elem02 )

        self.assertRaises(StopIteration , iter01.__next__)


    def test___next__three_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        iter01 = list01.__iter__()
        self.assertEqual ( iter01, list01 )

        rtn01 = iter01.__next__()

        self.assertEqual ( list01.current_iteration , delg02 )
        self.assertEqual ( rtn01, elem01 )

        rtn02 = iter01.__next__()

        self.assertEqual ( list01.current_iteration , delg03 )
        self.assertEqual ( rtn02, elem02 )

        rtn03 = iter01.__next__()

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( rtn03, elem03 )

        self.assertRaises(StopIteration , iter01.__next__)


    def test___next__five_delgs(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        iter01 = list01.__iter__()
        self.assertEqual ( iter01, list01 )

        rtn01 = iter01.__next__()

        self.assertEqual ( list01.current_iteration , delg02 )
        self.assertEqual ( rtn01, elem01 )

        rtn02 = iter01.__next__()

        self.assertEqual ( list01.current_iteration , delg03 )
        self.assertEqual ( rtn02, elem02 )

        rtn03 = iter01.__next__()

        self.assertEqual ( list01.current_iteration , delg04 )
        self.assertEqual ( rtn03, elem03 )

        rtn04 = iter01.__next__()

        self.assertEqual ( list01.current_iteration , delg05 )
        self.assertEqual ( rtn04, elem04 )

        rtn05 = iter01.__next__()

        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( rtn05, elem05 )

        self.assertRaises(StopIteration , iter01.__next__)


    def test_iterator_five_delgs_in_for(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_tail( delg01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        list01.append_tail( delg04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        list01.append_tail( delg05 )

        rtn01 = [ elem for elem in list01 ]        

        self.assertEqual( len( rtn01 ), 5 )
        self.assertEqual( rtn01[0], elem01 )
        self.assertEqual( rtn01[1], elem02 )
        self.assertEqual( rtn01[2], elem03 )
        self.assertEqual( rtn01[3], elem04 )
        self.assertEqual( rtn01[4], elem05 )


    def test_append_before_to_empty_list(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        list01.append_before( delg01, None )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg01 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 1 )

        self.assertIsNone( delg01.next )
        self.assertIsNone( delg01.prev )


    def test_append_before_to_one_elem_list_default(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg01 )

        list01.append_before( delg02, None )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg02 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertEqual ( delg01.next, delg02 )
        self.assertIsNone( delg01.prev )

        self.assertIsNone( delg02.next )
        self.assertEqual ( delg02.prev, delg01 )


    def test_append_before_to_one_elem_list_before_1st(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        list01.append_tail( delg01 )

        list01.append_before( delg02, delg01 )

        self.assertEqual ( list01.head, delg02 )
        self.assertEqual ( list01.tail, delg01 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 2 )

        self.assertIsNone( delg01.next )
        self.assertEqual ( delg01.prev, delg02 )

        self.assertEqual ( delg02.next, delg01 )
        self.assertIsNone( delg02.prev )


    def test_append_before_to_two_elems_list_default(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )

        list01.append_before( delg03, None )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg03 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 3 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )

        self.assertEqual ( delg03.prev, delg02 )
        self.assertIsNone( delg03.next )


    def test_append_before_to_two_elems_list_before_1st(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )

        list01.append_before( delg03, delg01 )

        self.assertEqual ( list01.head, delg03 )
        self.assertEqual ( list01.tail, delg02 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 3 )

        self.assertIsNone( delg03.prev )
        self.assertEqual ( delg03.next, delg01 )

        self.assertEqual ( delg01.prev, delg03 )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.prev, delg01 )
        self.assertIsNone( delg02.next )


    def test_append_before_to_two_elems_list_before_2nd(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )

        list01.append_before( delg03, delg02 )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg02 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 3 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg03 )

        self.assertEqual ( delg03.prev, delg01 )
        self.assertEqual ( delg03.next, delg02 )

        self.assertEqual ( delg02.prev, delg03 )
        self.assertIsNone( delg02.next )


    def test_append_before_to_five_elems_list_default(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        elem06 = dummy_obj()
        delg06 = nlpregex.abs_graph.double_link.ElemDelegate( elem06 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )
        list01.append_tail( delg03 )
        list01.append_tail( delg04 )
        list01.append_tail( delg05 )

        list01.append_before( delg06, None )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg06 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 6 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )

        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg04 )

        self.assertEqual ( delg04.prev, delg03 )
        self.assertEqual ( delg04.next, delg05 )

        self.assertEqual ( delg05.prev, delg04 )
        self.assertEqual ( delg05.next, delg06 )

        self.assertEqual ( delg06.prev, delg05 )
        self.assertIsNone( delg06.next )


    def test_append_before_to_five_elems_list_before_1st(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        elem06 = dummy_obj()
        delg06 = nlpregex.abs_graph.double_link.ElemDelegate( elem06 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )
        list01.append_tail( delg03 )
        list01.append_tail( delg04 )
        list01.append_tail( delg05 )

        list01.append_before( delg06, delg01 )

        self.assertEqual ( list01.head, delg06 )
        self.assertEqual ( list01.tail, delg05 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 6 )

        self.assertIsNone( delg06.prev )
        self.assertEqual ( delg06.next, delg01 )

        self.assertEqual ( delg01.prev, delg06 )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )

        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg04 )

        self.assertEqual ( delg04.prev, delg03 )
        self.assertEqual ( delg04.next, delg05 )

        self.assertEqual ( delg05.prev, delg04 )
        self.assertIsNone( delg05.next )


    def test_append_before_to_five_elems_list_before_2nd(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        elem06 = dummy_obj()
        delg06 = nlpregex.abs_graph.double_link.ElemDelegate( elem06 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )
        list01.append_tail( delg03 )
        list01.append_tail( delg04 )
        list01.append_tail( delg05 )

        list01.append_before( delg06, delg02 )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg05 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 6 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg06 )

        self.assertEqual ( delg06.prev, delg01 )
        self.assertEqual ( delg06.next, delg02 )

        self.assertEqual ( delg02.prev, delg06 )
        self.assertEqual ( delg02.next, delg03 )

        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg04 )

        self.assertEqual ( delg04.prev, delg03 )
        self.assertEqual ( delg04.next, delg05 )

        self.assertEqual ( delg05.prev, delg04 )
        self.assertIsNone( delg05.next )


    def test_append_before_to_five_elems_list_before_3rd(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        elem06 = dummy_obj()
        delg06 = nlpregex.abs_graph.double_link.ElemDelegate( elem06 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )
        list01.append_tail( delg03 )
        list01.append_tail( delg04 )
        list01.append_tail( delg05 )

        list01.append_before( delg06, delg03 )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg05 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 6 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg06 )

        self.assertEqual ( delg06.prev, delg02 )
        self.assertEqual ( delg06.next, delg03 )

        self.assertEqual ( delg03.prev, delg06 )
        self.assertEqual ( delg03.next, delg04 )

        self.assertEqual ( delg04.prev, delg03 )
        self.assertEqual ( delg04.next, delg05 )

        self.assertEqual ( delg05.prev, delg04 )
        self.assertIsNone( delg05.next )


    def test_append_before_to_five_elems_list_before_4th(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        elem06 = dummy_obj()
        delg06 = nlpregex.abs_graph.double_link.ElemDelegate( elem06 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )
        list01.append_tail( delg03 )
        list01.append_tail( delg04 )
        list01.append_tail( delg05 )

        list01.append_before( delg06, delg04 )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg05 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 6 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )

        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg06 )

        self.assertEqual ( delg06.prev, delg03 )
        self.assertEqual ( delg06.next, delg04 )

        self.assertEqual ( delg04.prev, delg06 )
        self.assertEqual ( delg04.next, delg05 )

        self.assertEqual ( delg05.prev, delg04 )
        self.assertIsNone( delg05.next )


    def test_append_before_to_five_elems_list_before_5th(self):

        list01 = nlpregex.abs_graph.double_link.List()

        elem01 = dummy_obj()
        delg01 = nlpregex.abs_graph.double_link.ElemDelegate( elem01 )

        elem02 = dummy_obj()
        delg02 = nlpregex.abs_graph.double_link.ElemDelegate( elem02 )

        elem03 = dummy_obj()
        delg03 = nlpregex.abs_graph.double_link.ElemDelegate( elem03 )

        elem04 = dummy_obj()
        delg04 = nlpregex.abs_graph.double_link.ElemDelegate( elem04 )

        elem05 = dummy_obj()
        delg05 = nlpregex.abs_graph.double_link.ElemDelegate( elem05 )

        elem06 = dummy_obj()
        delg06 = nlpregex.abs_graph.double_link.ElemDelegate( elem06 )

        list01.append_tail( delg01 )
        list01.append_tail( delg02 )
        list01.append_tail( delg03 )
        list01.append_tail( delg04 )
        list01.append_tail( delg05 )

        list01.append_before( delg06, delg05 )

        self.assertEqual ( list01.head, delg01 )
        self.assertEqual ( list01.tail, delg05 )
        self.assertIsNone( list01.current_iteration )
        self.assertEqual ( list01.num_elems, 6 )

        self.assertIsNone( delg01.prev )
        self.assertEqual ( delg01.next, delg02 )

        self.assertEqual ( delg02.prev, delg01 )
        self.assertEqual ( delg02.next, delg03 )

        self.assertEqual ( delg03.prev, delg02 )
        self.assertEqual ( delg03.next, delg04 )

        self.assertEqual ( delg04.prev, delg03 )
        self.assertEqual ( delg04.next, delg06 )

        self.assertEqual ( delg06.prev, delg04 )
        self.assertEqual ( delg06.next, delg05 )

        self.assertEqual ( delg05.prev, delg06 )
        self.assertIsNone( delg05.next )


if __name__ == '__main__':
    unittest.main()
