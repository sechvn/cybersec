'''
CIS 120 - Intro to Data Structures, UMA, Spring 2022

Program: Stack.py
Author: Eric Gimbel
Date Created: 4/15/2022

Implement a linked-list variant of a stack abstract data type.'''

from ListNode import ListNode


class Stack():

    def __init__(self):
        '''creates an empty LIFO stack'''
        self.head = None
        self.size = 0

    def push(self, item):
        '''pre: none
        post: places item on top of the stack'''
        firstnode = ListNode(item)
        if self.head is None:  # If our stack is empty make the start of the linked list of nodes our first node object
            # Sets top or start to first node object with data/item value supplied by client
            self.head = firstnode
        else:
            # There is already a node object in our stack, point the new node's link to the top of the stack
            firstnode.link = self.head
            self.head = firstnode  # Top of stack now equals first node

    def pop(self):
        '''pre: stack is not empty; IndexError is raised if empty
        post: removes and returns the top element of the stack'''
        if self.head is None:
            raise IndexError('Stack is Empty!')
        else:
            # Set variable to top node's data value to be deleted/popped.
            frontnode = self.head.item
            # Set the new top of the stack to the next node.
            self.head = self.head.link
            # Now return the first node's item that has been popped.
            return frontnode

    def top(self):
        '''pre: stack is not empty; IndexError is raised if empty
        post: returns the top element of the stack without removing it'''
        if self.head is None:
            raise IndexError('Stack is Empty!')
        else:
            # Simply return first item in the stack which the head points to.
            return self.head.item

    def size(self):
        '''pre: none
        post: returns the number of elements in the stack'''
        return self.size  # Return the size of the stack

#Sources: Please see on bottom of MyQueueADT.py
