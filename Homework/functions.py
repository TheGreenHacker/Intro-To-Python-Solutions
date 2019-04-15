#!/usr/bin/python

import math
import string
from sets import Set
import pytest

"""
Write a function that computes the volume of a sphere given its radius.
"""
def vol(rad):
    return 4 * math.pi * rad**3 / 3

"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""
def ran_check(num, low, high):
    if num >= low and num <= high:
        print "{} is in the range between {} and {}".format(num, low, high)

def ran_bool(num, low, high):
    return num >= low and num <= high

"""
Write a Python function that accepts a string and calculates the number of upper case letters
and lower case letters.
"""
def up_low(s):
    lower = 0
    upper = 0
    for c in s:
        if c.isalpha():
            if c.isupper():
                upper += 1
            else:
                lower += 1
    print "No. of Upper case characters : {}".format(upper)
    print "No. of Lower case characters : {}".format(lower)

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""
def unique_list(lst):
    return list(Set(lst))

"""
Write a Python function to multiply all the numbers in a list.
"""
def multiply(numbers):
    return reduce(lambda x, y: x*y, numbers)

"""
Write a Python function that checks whether a passed in string is palindrome or not.
"""
def palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

"""
Write a Python function to check whether a string is pangram or not.
"""
def ispangram(str1, alphabet=string.ascii_lowercase):
    s = Set()
    for char in str1:
        if char in alphabet:
            s.add(char)
    return len(s) == len(alphabet)


# Driver code to test all functions
def main():
    assert vol(2) == pytest.approx(33.5103216383, 0.00001)

    ran_check(5, 2, 7)
    assert ran_bool(3, 1, 10)
    assert not ran_bool(15, 1, 10)

    s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
    up_low(s)

    assert unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]

    assert multiply([1, 2, 3, -4]) == -24

    assert palindrome('helleh')
    assert palindrome('racecar')
    assert not palindrome('weed')
    assert not palindrome('interview')

    assert ispangram("The quick brown fox jumps over the lazy dog")
    assert not ispangram("Smoke weed everyday")
    
    print "All tests passed"

if __name__ == "__main__":
    main()