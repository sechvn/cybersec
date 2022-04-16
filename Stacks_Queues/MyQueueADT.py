'''
CIS 120 - Intro to Data Structures, UMA, Spring 2022

Program: MyQueueADT.py
Author: Eric Gimbel
Date Created: 4/16/2022

Implement a linked-list variant of a queue abstract data type'''

from ListNode import ListNode


class Queue():

    def __init__(self):
        '''create an empty FIFO queue'''
        self._size = 0
        self.head = None
        # Initialize the state of queue object to have both head and tail to keep track of front and back of linked list of nodes.
        self.tail = None

    def enqueue(self, item):
        '''pre: none
        post: item is added to the queue'''
        if self.tail is None:  # If the queue is empty, set both the head and tail to the first node.
            self.head = ListNode(item)
            self.tail = self.head  # Set tail to also first node object or item in the queue
        else:
            # Enforce concept of queue and add new node to end of linked list or queue
            self.tail.link = ListNode(item)
            self.tail = self.tail.link  # Adds new node object/item to end of the queue
            self._size += 1  # Increase the size of the queue

    def dequeue(self):
        '''pre: queue is not empty; IndexError is raised if empty
        post: removes and returns first item in the queue'''
        if self.head is None:
            raise IndexError('The Queue is Empty!')
        else:
            fpopped = self.head.item  # Set variable to the start or front of the queue
            self.head = self.head.link  # Move the pointer to the next node or item in the queue
            self._size -= 1  # Decrease the count or size of the queue
            return fpopped  # Return the popped first/item from the queue

    def front(self):
        '''pre: queue is not empty; IndexError is raised if empty
        post: returns first item in the queue without removing it'''
        if self.head is None:
            raise IndexError('The Queue is Empty!')
        else:
            # Returns the first item in the queue or linked list of nodes.
            return self.head.item

    def size(self):
        '''pre: none
        post: returns number of items in the queue'''
        return self._size  # Return the size or number of items in the queue

#This is finally starting to click. I need a lot more practice. One thing I found is that there are several ways to implement both stacks
#and queues using linked lists. I was going to try recursion on some of the methods but decided to keep that for the next project. I think
#what I kept losing track of was that a class is like a factory or template that sets the state or default properties and methods for the object
#so that the client/user can instantiate objects and utilitize that object's methods. I kept trying to visualize how python knew to walk forward
#just by setting for example self.head.link, but it's because there wasn't yet a whole bunch of nodes linked together but the fact we are creating the ability
#to produce these types of objects with methods that work on those objects. Probably explained that really bad but I understand what I was doing wrong. I still
#think it will take practice and my goal is to continue working with linked lists. They are a great way to not only learn but also improve runtime when dealing
#with certain data structures.
#Sources:
#Realpython.com
#towardsdatascience.com
#geeksforgeeks.com
#youtube.com/c/AmulsAcademy/videos
#Packt publishing - Same titles as other projects
#How to think like a Computer Scientist: Learning with Python 3
#stackoverflow.com
#Lastly, what helped me greatly with understanding Stack's was to think about stacking plates! Then the example you gave or someone gave when we queue up
#the next song or are standing in line at the DMV for queues.
