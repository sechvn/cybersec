'''
Program: Rational.py
Author: Eric Gimbel
Date: 2/9/22

An ADT implementaion of a rational (real) number.
Demonstrates operator overloading
'''

import math


class Rational:   # I removed object/parenthesis as this is not needed in python 3 unless you have a parent class or for backward compatibility.
    def __init__(self, num = 0, den = 1):
        '''pre: creates a new Rational object, num and den are integers
           post: creates the Rational object num / den, and returns num and den in reduced form
        '''
        # Gcd from math module to find greatest common divisor.
        # That number is then taken and divided into the numerator and denominator, 
        # resulting in a reduced fraction.
        greatestCommon = math.gcd(num,den)
        self.num = int(num / greatestCommon)
        self.den = int(den / greatestCommon)    # type casted int as the gcd returns float values and made unit tests harder to do.    
        
    def __mul__(self, other):
        '''* operator
        pre: self and other are Rational objects
        post: returns Rational product: self * other
        '''

        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)
                
    def __str__(self):
        '''return string for printing
        pre: self is Rational object
        post: returns a string representation self
        '''        
        return str(self.num) + '/' + str(self.den)    

    def __add__(self, other):
        '''+ operator
           pre: self and other are Rational objects
           post: returns added fractions in reduced form
        '''
        # Apply cross multiplication of fractions. I had to teach myself this as it was a different way than I learned! But works better. 
        # Order of operations is important here to note when trying to add on your own! 
        # This also avoids trying to set up an alternate method of adding fractions with same denominator!                                        
        n = self.num * other.den + self.den * other.num 
        d = self.den * other.den
               
        return Rational(n,d)       
                
    def __sub__(self, other):
        '''- operator
           pre: self and other are Rational objects
           post: returns subtracted fractions in reduced form
        '''
        # Again apply cross multiplication this time subtracting.
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        
        return Rational(num,den)

    def __truediv__(self, other):
        '''/ operator
           pre: self and other are Rational objects
           post: returns true division of integers in reduced form
        '''
        # The reciprocal needs to be flipped before multiplying, cross multiply!
        num = self.num * other.den
        den = self.den * other.num
        
        return Rational(num,den) 

    def __lt__(self, other):
        '''< operator
           pre: self and other are Rational objects
           post: returns True if first (left) fraction is less than second (right) fraction,
           returns False if opposite is true
        '''
        num = self.num * other.den
        den = other.num * self.den
        
        if num < den:
            return True
        else:
            return False        

    def __gt__(self, other):
        '''> operator
           pre: self and other are Rational objects
           post: returns True if first (left) fraction is greater than second (right) fraction,
                 return False if opposite is true
        '''
        num = self.num * other.den
        den = other.num * self.den
        
        if num > den:
            return True
        else:
            return False

    def __le__(self, other):
        '''<= operator
           pre: self and other are Rational objects
           post: returns True if first (left) fraction is less than or equal to second (right) fraction,
                 returns False if opposite is true
        '''
        num = self.num * other.den
        den = other.num * self.den
        
        if num <= den:
            return True
        else:
            return False

    def __ge__(self, other):
        '''>= operator
           pre: self and other are Rational objects
           post: returns True if first (left) fraction is greater than or equal to second (right) fraction,
                 returns False if opposite is true
        '''
        num = self.num * other.den
        den = other.num * self.den
        
        if num >= den:
            return True
        else:
            return False

    def __eq__(self, other):
        '''== operator
           pre: self and other are Rational objects
           post: returns True if first (left) fraction is equal to second (right) fraction,
                 returns False if fractions are not equal
        '''
        num = self.num * other.den
        den = other.num * self.den
        
        if num == den:
            return True
        else:
            return False
    
    def __ne__(self, other):
        '''!= operator
           pre: self and other are Rational objects
           post: returns True if first (left) fraction is not equal to second (right) fraction,
                 returns False if fractions are equal
        '''
        num = self.num * other.den
        den = other.num * self.den
        
        if num != den:
            return True
        else:
            return False
        
# Sources: As your aware I did look at code that was on github. But oddly enough did not use 
# the solutions. None of the code I viewed had the unit tests. And the code I did look at was simply
# to try and understand the differences of instance variables and local within classes. I did read about classes
# in two books I have, which are "Python Crash Course" and "Think Python." I read quite a bit from our
# book and watched parts of your lecture which helped immensely. The biggest issue I had was figuring out
# the addition method. My problem was simple math and not realizing the different ways to add/subtract fractions.
# One thing I didn't use was my own gcd, instead I used the math module. The code I did view on github had a version
# of Euclid's algorithm but I felt it wouldn't be my own, and I need to understand it before using it in my code.
# https://github.com/zeelorenc/python-fraction-class/blob/master/fraction.py
# https://byjus.com/maths/greatest-common-divisor/
# https://prepinsta.com/python-program/addition-of-two-fractions/
# https://www.mometrix.com/academy/cross-multiplying-fractions/
# https://pythontutor.com
# Then a ton of googling. I want to try and come up with my own gcd. Which I will continue to work on. I was able to complete the first
# assignment with the program returning none and checking for negative numbers. These are incredible learning assignments, I do get
# pretty frustated because I am not a math person but it is also logic as well and being able to translate things into code.
# This assignment definately helped! In addition to running the unit tests with the values present, I also used my class to test each method
# of code. Hopefully, everything works and I was able to properly complete the pre and post conditions.
# testone = Rational(3,6)
# testtwo = Rational(4,12)
# testResult = testone + testtwo
# print(testResult)
# OOP is indeed awesome! (Update) Didn't completely understand the power behind classes and methods,
# but once I tested with the code above, it really hit home how useful ADT's and OOP is!
# Here is the GCD or Euclid's algorithm:
#def __gcd__(a,b):
#        if b == 0: (Could also use: while b != 0: return a else: return(b, a%b)
#            return a
#        else:
#            return(b, a%b)

# It solves it by taking the larger number if "b" isn't 0, and switching them then modulus which
# gives the remainder and via recursion continues until "b" is 0 then returns "a" which is the GCD.
# Although, I understand this now, I was not comfortable using it and couldn't figure out where to put
# it in my code.
