'''
Program: test_rational.py
Author: Eric Gimbel
Date: 2//9/22

A set of unit tests for our Rational ADT
'''

import sys
import unittest

from Rational import *

class RationalTest(unittest.TestCase):
       
    def testConstructorOneInt(self):

        r = Rational(-3)
        self.assertEqual(str(r), '-3/1')
       
    def testConstructorTwoInt(self):

        r = Rational(3, 4)
        self.assertEqual(str(r), '3/4')

    def testMul(self):

        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        r3 = r1 * r2
        self.assertEqual(str(r3), '1/2')

    def testAdd(self):
        r1 = Rational(1,4)
        r2 = Rational(-4,8)
        r3 = r1 + r2
        self.assertEqual(str(r3), '-1/4')

    def testSub(self):
        r1 = Rational(1,4)
        r2 = Rational(2,8)
        r3 = r1 - r2
        self.assertEqual(str(r3), '0/1')
        
    def testTruediv(self):
        r1 = Rational(10,12)
        r2 = Rational(6,8)
        r3 = r1 / r2
        self.assertEqual(str(r3), '10/9')
    
    def testLt(self):
        r1 = Rational(2,4)
        r2 = Rational(4,6)
        r3 = r1 < r2
        self.assertEqual(str(r3), 'True' or 'False')    

    def testGt(self):
        r1 = Rational(3,4)
        r2 = Rational(2,16)
        r3 = r1 > r2
        self.assertEqual(str(r3), 'True' or 'False')

    def testLe(self):
        r1 = Rational(1,4)
        r2 = Rational(2,8)
        r3 = r1 <= r2
        self.assertEqual(str(r3), 'True' or 'False')
    # TODO -- add tests for the other methods in Rational.py
    def testGe(self):
        r1 = Rational(3,6)
        r2 = Rational(4,12)
        r3 = r1 >= r2
        self.assertEqual(str(r3), 'True' or 'False')
        
    def testEq(self):
        r1 = Rational(1,4)
        r2 = Rational(2,8)
        r3 = r1 == r2
        self.assertEqual(str(r3), 'True' or 'False')
    
    def testNe(self):
        r1 = Rational(10,12)
        r2 = Rational(6,8)
        r3 = r1 != r2
        self.assertEqual(str(r3), 'True' or 'False')
                
def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
