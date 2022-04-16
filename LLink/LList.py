# LList.py - CIS120, Intro to Data Structures

from ListNode import ListNode


class LList:

    def __init__(self):
        """create an LList"""

        self.head = None
        self.size = 0

    def __len__(self):
        """"post: returns number of items in the list"""

        return self.size

    def append(self, x):
        """appends x onto end of the list
        post: x is appended onto the end of the list"""

        # create a new node containing x
        newnode = ListNode(x)

        # add it to the end of the list
        if self.head is None:
            # empty list
            self.head = newnode
        else:
            # non-empty list
            curr = self.head
            while curr.link is not None:
                curr = curr.link
            curr.link = newnode

        self.size += 1

    def __str__(self):
        """Hook method which returns the string representation of,
           our linked list."""

        retstr = "< "
        curr = self.head
        while curr is not None:
            retstr += str(curr.item)
            if curr.link is not None:
                retstr += ", "
            curr = curr.link
        retstr += " >"

        return retstr

    def pop(self, i=None):
        """Returns and remove at position i.
            If i is not specified, return last item
            Pre: the list has at least one item
            Post: the item is removed and returned"""

        assert self.size > 0 and (i is None or (0 <= i < self.size))

        if i is None:
            i = self.size - 1

        if i == 0:  # removing the first item
            item = self.head.item
            self.head = self.head.link
        else:
            # removing from within the list
            node = self._find(i - 1)
            item = node.link.item
            node.link = node.link.link

        self.size -= 1

        return item

    def _find(self, position):
        """"private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list"""

        assert 0 <= position < self.size

        curr = self.head
        currpos = 0

        while currpos < position:
            curr = curr.link
            currpos += 1

        return curr

    def __getitem__(self, position):
        """return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position"""

        node = self._find(position)
        return node.item

    def __setitem__(self, position, value):
        """set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value"""

        node = self._find(position)
        node.item = value

    def insert(self, i, x):
        """inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and
              old elements from position i..oldsize-1 are at positions
              i+1..newsize-1"""

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = ListNode(x, self.head)
        else:
            # find item that node is to be inserted after
            node = self._find(i - 1)
            node.link = ListNode(x, node.link)
        self.size += 1

    def __delitem__(self, position):
        """delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from
        the list"""

        assert 0 <= position < self.size

        if position == 0:
            self.head = self.head.link
        else:
            node = self._find(position - 1)
            node.link = node.link.link

        self.size -= 1

    def __copy__(self):
        """post: returns a new LList object that is a shallow copy of self"""

        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    # Your work begins here. Complete these five methods, including
    #     -- their docstring (pre & post conditions)
    #     -- an implementation to satisfy the design
    #     -- don't forget to test the preconditions!

    def min(self):
        """ Find and return the minimum item in the list
            Complete this method
            pre: self.size is greater than zero, Node is not empty
            post: Finds minimum value in linked list of nodes, returns minval
            else returns None.
        """
        if self.size > 0:  # Checks the pre condition
            currpos = self.head  # Sets current position equal to head or start node
            minval = currpos.item  # sets variable to current node's data value
            while currpos is not None:  # Ensures Node is not empty
                if currpos.item < minval:  # Loops through each item in node, if item is less than current node's data value sets the minimum value to the current node's item
                    minval = currpos.item
                currpos = currpos.link  # Updates or points to next node in list
            return minval  # Returns the minimum value or item in the list of node objects
        return None

    def max(self):
        """ Find and return the maximum item in the list
            Complete this method
            pre: self.size is greater than zero, Node is not empty
            post: Finds maximum value in linked list of nodes, returns maxval
            else returns None.
        """

        if self.size > 0:  # Checks pre condition
            currpos = self.head
            maxval = currpos.item
            while currpos is not None:
                if currpos.item > maxval:  # Loops through each item in node, if item is more than current node's data value sets the maximum value to the current node's item
                    maxval = currpos.item
                currpos = currpos.link
            return maxval
        return None  # Ensures proper post condition return

    def index(self, value, start=0):
        """ Return the index of the node where node.item = value
            Start is an optional parameter, if provided, begin your
            search at the node in position start
            complete this method
            pre: self.size is greater than zero, Node is not empty
            post: Returns the index value of linked list node item's position
        """
        if self.size > 0:  # Checks pre-condition
            node = self.head  # Begins search at first node or head
            count = 0         # Initialize a counter variable to hold node item's index value

            for i in range(start):
                node = node.link
                count += 1



            while node is not None:
                if node.item == value and count >= start:# Loop through items in linked list nodes and return the index of the value's position
                   return count  # Completes post-condition
                count += 1
                node = node.link  # Update the pointer to the next node

    def count(self, value):
        """ Return the count of the number of times value may be
            found in the list
            complete this method
            pre: self.size is greater than zero, Node is not empty
            post: Returns the number of times a value is present in the linked list of node objects data field
        """
        if self.size > 0:  # Checks pre-condition

            currpos = self.head  # Set current position to head node or first node
            count = 0  # Initialize counter variable to hold the number of times a node's data item is found in the linked list
            while currpos is not None:

                if currpos.item == value:  # If the first node's data item is equal to the value given increase the count variable
                    count += 1
                currpos = currpos.link  # Move to the next node by updating the link or pointer
            return count  # Completes post-condition and returns the number of times a value is found in our linked list node objects

    def remove(self, value):
        """ Given a value, remove the first occurrence of value on the list
            complete this method
            pre: self.size is greater than zero, Node is not empty
            post: Finds the value given and removes the item by removing the pointer reference to the node and updates the link to subsequent node
        """
        if self.size > 0:  # Checks pre-condition
            if value == 0:  # If the start node is empty move to the next node
                self.head = self.head.link  # Update the node to the next node in the linked list
            else:
                # Finds the value given and assigns to variable
                node = self._find(value - 1)
                # Now remove the link or pointer to that value and decrement the size of the linked list of nodes
                node.link = node.link.link

            self.size -= 1
        return True  # Completes post-condition

#Sources:
#pythoncentral.io/find-remove-node-linked-lists/
#geeksforgeeks.org/write-a-function-to-get-nth-node-in-a-linked-list/
#Used several books from Packt publishing on basic OOP and data Structures
#This really didn't help that much as what helped me the most was your lecture and the textbook
#I have a pretty good handle on this now, but I did reference those sites that had the different ways you could loop through
#and produce each method. This was definately not something that I excelled at and will need to revisit this
#It was a great assignment the confusing part for me was understanding the relationship between the nodes and linked list
#then keeping track of the head and items making sure to update the next node properly. I think this assignment strenghthened my
#understanding of the while loop. It is pretty cool how you can use it to loop through and compare each value similiar to a for loop and get the min or max values
#I should of immediately worked on this after the lecture but kept procastinating on the assignment. I did try my dead level best to figure out each method on
#my own but did have to reference other code to solve it.
