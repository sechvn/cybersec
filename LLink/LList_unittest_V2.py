'''
 CIS 120, Intro to Data Structures, Assignment 4

 Program: LList_unittest.py
 Author: Eric Gimbel
 Date Created: 4/6/2022

 Brief Description: Unittests to test implementation of Node class with linked list class methods
'''

import sys
import unittest

import LList as ll


def _newLL(sequence=()):
    ''' private function to create a new linked list for testing'''
    theLL = ll.LList()
    for item in sequence:
        theLL.append(item)
    return theLL


class LListTest(unittest.TestCase):

    _LL1 = _newLL((12, 11, 7, 1, 2, 23, 25, 4, 8, 5, 4, 8, 17))

    def testMin(self):
        '''  Test the .min() method '''
        self.assertEqual(self._LL1.min(), 1)

    def testMax(self):
        '''  Test the .max() method '''
        self.assertEqual(self._LL1.max(), 25)

    def testCount(self):
        ''' test the .count(value) method '''
        self.assertEqual(self._LL1.count(8), 2)

    def testIndex(self):
        ''' Test the .index(value, <start>) method '''
        self.assertEqual(self._LL1.index(7), 4)

    def testRemove(self):
        ''' test the .remove(value) method '''
        self.assertEqual(self._LL1.remove(4), True)


def main(argv):
    unittest.main()


if __name__ == '__main__':
    main(sys.argv)
