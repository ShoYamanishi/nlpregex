#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Doubly linked list. The main purpose is torepresent incidence at each node.
It is used to manage an ordered list of elements for:
- dynamic insertion and deletion of elements at specific point in O(|1|).
- iteration in both forwards and backwards.
- desctuctive iteration where some elements are removed or inserted during iteration
- elements is able to belong to multiple lists with designated identifier.
"""


# Instance linked in a list as a delegate
# Actual element (owner) is maintained in self.elem.

class ElemDelegate:

    def __init__( self, elem ):

        self.prev = None
        self.next = None
        self.elem = elem


    def link_this_before( self, next_elem ):

        self.next      = next_elem
        next_elem.prev = self


    def unlink_next_delg(self):

        current_next      = self.next
        self.next         = None
        current_next.prev = None
        return current_next


    def link_this_after( self, prev_elem ):

        self.prev      = prev_elem
        prev_elem.next = self


    def unlink_prev_delg(self):

        current_prev      = self.prev
        self.prev         = None
        current_prev.next = None
        return current_prev


    # Help invocation of __del()__.
    def clean_refs(self):
        self.prev = None
        self.next = None
        self.elem = None

    
class List:

    def __init__(self):

        self.head              = None
        self.tail              = None
        self.num_elems         = 0
        self.current_iteration = None


    def inc_num_elems(self):
        self.num_elems += 1


    def dec_num_elems(self):
        self.num_elems -= 1


    def append_head( self, delg ):

        if self.head:

            prev_head = self.head
            self.head = delg
            delg.link_this_before( prev_head )

        else:
            self.head = delg
            self.tail = delg

        self.inc_num_elems()


    def append_tail( self, delg ):

        if self.tail:

            prev_tail = self.tail
            self.tail = delg
            prev_tail.link_this_before( delg )

        else:
            self.head = delg
            self.tail = delg

        self.inc_num_elems()


    def append_before( self, delg_new, delg_next = None):

        if delg_next:

            if self.head == delg_next:

                prev_head = self.head
                self.head = delg_new
                delg_new.link_this_before( prev_head )

            else:

                delg_prev = delg_next.unlink_prev_delg()
                delg_prev.link_this_before( delg_new  )
                delg_new. link_this_before( delg_next )

            self.inc_num_elems()

        else:

            self.append_tail( delg_new )




    def remove( self, delg ):

        if self.head == delg:

            self.remove_head()

        elif self.tail == delg:

            self.remove_tail()

        else:
            self.dec_num_elems()
            next = delg.unlink_next_delg()
            prev = delg.unlink_prev_delg()
            prev.link_this_before( next )


    def remove_head(self):

        if self.head:

            self.dec_num_elems()

            if self.head == self.tail:

                delg      = self.head;
                self.head = None
                self.tail = None
                return delg

            else:
                delg      = self.head
                self.head = delg.next
                delg.unlink_next_delg()
                return delg

        else:
            return None


    def remove_tail(self):

        if self.tail:

            self.dec_num_elems()            

            if self.head == self.tail:
                delg      = self.tail
                self.head = None
                self.tail = None
                return delg

            else:
                delg      = self.tail
                self.tail = delg.prev
                delg.unlink_prev_delg()
                return delg

        else:
            return None


    def cnt(self):
        return self.num_elems


    def __iter__(self):

        self.current_iteration = self.head
        return self


    def __next__(self):

        if self.current_iteration:

            saved = self.current_iteration
            self.current_iteration = saved.next
            return saved.elem

        else:
            raise StopIteration


    def next(self):
        return self.__next__()

