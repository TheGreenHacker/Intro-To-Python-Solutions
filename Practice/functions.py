#!/usr/bin/python

import sys
import math

# Warmup

"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both 
numbers are even, but returns the greater if one or both numbers are odd
"""
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words
begin with same letter
"""
def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]

"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one 
of the integers is 20. If not, return False
"""
def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20


# Level 1

"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""
def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
"""
def master_yoda(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
"""
def almost_there(n):
    return (n >= 90 and n <= 110) or (n >= 190 and n <= 210)


# Level 2

"""
FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""
def has_33(nums):
    size = len(nums)
    for i in range(size - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

"""
PAPER DOLL: Given a string, return a string where for every character in the original there
are three characters
"""
def paper_doll(text):
    str = ""
    for letter in text:
        str += letter * 3
    return str

"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
"""
def blackjack(a,b,c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif (a == 11 or b == 11 or c == 11) and sum <= 31:
        return sum - 10
    else:
        return 'BUST'

"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
Return 0 for no numbers.
"""
def summer_69(arr):
    sum = 0
    size = len(arr)
    i = 0
    while i < size:
        if arr[i] == 6:
            while (arr[i] != 9):
                i += 1
        else:
            sum += arr[i]
        i += 1
    return sum


# Challenge

"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def includes(arr1, n1, arr2, n2):
    if n2 == len(arr2):
        return True
    if n1 == len(arr1):
        return False
    if arr1[n1] == arr2[n2]:
        return includes(arr1, n1 + 1, arr2, n2 + 1)
    else:
        return includes(arr1, n1 + 1, arr2, n2)

def spy_game(nums):
    spy = [0, 0, 7]
    return includes(nums, 0, spy, 0)

"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including
a given number
"""
def count_primes(num):
    sieve = [True] * (num + 1)
    rootNum = int(math.sqrt(num))
    for i in range(2, rootNum + 1):
        if sieve[i]:
            for j in range (2 * i, num + 1, i):
                sieve[j] = False
    primes = 0
    for i in range(2, num + 1):
        if sieve[i]:
            primes += 1
    return primes


# Driver code to test all functions
def main():
    assert lesser_of_two_evens(2,4) == 2
    assert lesser_of_two_evens(2,5) == 5

    assert animal_crackers('Levelheaded Llama')
    assert not animal_crackers('Crazy Kangaroo')

    assert makes_twenty(20,10)
    assert makes_twenty(12,8)
    assert not makes_twenty(2,3)

    assert old_macdonald('macdonald') == 'MacDonald'

    assert master_yoda('I am home') == 'home am I'
    assert master_yoda('We are ready') == 'ready are We'

    assert almost_there(90)
    assert almost_there(104)
    assert not almost_there(150)
    assert almost_there(209)

    assert has_33([1, 3, 3])
    assert not has_33([1, 3, 1, 3])
    assert not has_33([3, 1, 3])

    assert paper_doll('Hello') == 'HHHeeellllllooo'
    assert paper_doll('Mississippi') == 'MMMiiissssssiiissssssiiippppppiii'

    assert blackjack(5,6,7) == 18
    assert blackjack(9,9,9) == 'BUST'
    assert blackjack(9,9,11) == 19

    assert summer_69([1, 3, 5]) == 9
    assert summer_69([4, 5, 6, 7, 8, 9]) == 9
    assert summer_69([2, 1, 6, 9, 11]) == 14

    assert spy_game([1,2,4,0,0,7,5])
    assert spy_game([1,0,2,4,0,5,7])
    assert not spy_game([1,7,2,0,4,5,0])

    assert count_primes(100) == 25
    assert count_primes(0) == 0
    assert count_primes(1) == 0

    print "All tests passed"

if __name__ == "__main__":
    main()