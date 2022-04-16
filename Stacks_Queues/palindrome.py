# palindrome.py
from MyQueueADT import Queue
from StackADT import Stack
import string

#------------------------------------------------------------

def isPalindrome(phrase):
    forward = Queue()
    reverse = Stack()
    extractLetters(phrase, forward, reverse)
    return sameSequence(forward, reverse)

#------------------------------------------------------------

def extractLetters(phrase, q, s):
    for ch in phrase:
        if ch.isalpha():
            ch = ch.lower()
            q.enqueue(ch)
            s.push(ch)

#------------------------------------------------------------

def sameSequence(q, s):
    while q.size() > 0:
        ch1 = q.dequeue()
        ch2 = s.pop()
        if ch1 != ch2:
            return False
    return True

def main():
    str1 = 'racecar'
    print(f'Is "{str1}" a pallindrome?  {isPalindrome(str1)}') #should be True

    str1 = 'Python is Fun'
    print(f'Is "{str1}" a pallindrome?  {isPalindrome(str1)}') # should be False

if __name__ == '__main__': main()
