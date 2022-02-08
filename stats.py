# Program: stats.py
# Author: Eric Gimbel
# Date: 2/6/22
#
# Assignment 1, Intro to Data Strtures
#
# Note: you may NOT use the built-in statistical functions
#       min, max, sum, et.   Instead, create your own code to
#       calculate the answer.
#
#       You may use math.sqrt when calculating the standard deviation

import math

def get_scores():
    '''Get scores interactively from the user

    pre: Accepts integer numbers >= 0
    post: returns a list of numbers obtained from user
    
    '''
    nums = []
    
    for i in nums:
        if i < 0:
            raise ValueError
       
    while True:
        num = input("Enter a number (<return> to Quit): ")
        if num == "": break
        nums.append(eval(num))
    return nums


def min_value(nums):
    ''' find the minimum

    pre: nums is a list of numbers and len(nums) > 0
    post: returns smallest number in nums
    
    '''
    for i in nums:
        if i < 0:
            raise ValueError
        
    min = nums[-1]
    for num in nums:
        if num < min:
            min = num
    return min


def max_value(nums):
    ''' find the maximum

    pre: nums is a list of numbers and len(nums) > 0
    post: returns largest number in nums
    
    '''
    for i in nums:
        if i < 0:
            raise ValueError
    
    max = nums[-1]
    for num in nums:
        if num > max:
            max = num
    return max

def average(nums):
    ''' calculate the mean

    pre: nums is a list of numbers and len(nums) > 0
    post: returns the mean (a float) of the values in nums
    
    '''
    for i in nums:
        if i < 0:
            raise ValueError
    
    count = 0    
    length = 0    
    for i in nums:        
        for x in nums:            
            count += i            
            length += 1            
    return count / length
        

def std_deviation(nums):
    '''calculate the standard deviation

    pre: nums is a list of numbers and len(nums) > 1
    post: returns the standard deviation (a float) of the values in nums
          
    '''
    for i in nums:
        if i < 0:
            raise ValueError
        
    x = average(nums)    
    total = 0.0    
    for num in nums:        
        total += (x - num) ** 2            
    return math.sqrt(total / (len(nums) - 1))   #Used the book for this, tried to use list comprehension variation I found, but the book was much simpler and cleaner.
    

def distribution(nums):
    ''' pre: Accepts list of integer values >= 0
        post: Determines how many integer values are within exam or grade ranges (eg. 60-69,70-79,ect.)
        then prints how many integer values of each fall within the grade ranges.
    '''
    for i in nums:
        if i < 0:
            raise ValueError
    
    range1 = 0
    range2 = 0
    range3 = 0
    range4 = 0
    range5 = 0
    range6 = 0
    
    for num in nums:
        if num > 99:
            range1 += 1
        if num > 89 and num < 100:
            range2 += 1
        if num > 79 and num < 90:
            range3 += 1
        if num > 69 and num < 80:
            range4 += 1
        if num > 59 and num < 70:
            range5 += 1
        if num <= 59:
            range6 += 1
            
    return(range1, range2, range3, range4, range5, range6)
    

def main():
    nums = get_scores()
    print(min_value(nums))
    print(max_value(nums))
    print(average(nums))
    print(std_deviation(nums))
    print(distribution(nums))
    
if __name__ == '__main__':
    main()
    
    
# I used a few websites and general googling to find ideas on how to code the min, max, and len without using the functions. I also
# used pythontutor.org to test and step through some of the code as I was testing everything out. My brother also gave me an idea
# on how to write the distribution function which I was already using and is notably different than what he suggested. To begin with
# I was attempting to find a way to do the distribution function without if statements for the ranges. 
# List of sources: https://stackoverflow.com/questions/15148491/min-and-max-of-a-list-without-using-min-max-function#:~:text=def%20minMax%20%28lst%2Cuser%29%3A%20if%20user%20%3D%3D%20min%3A%20return,one%20function%20it%20will%20be%20%221%20recursive%20function%22.
# https://www.delftstack.com/howto/python/standard-deviation-of-a-list-in-python/
# https://datagy.io/python-count-occurrences-in-list/

    
