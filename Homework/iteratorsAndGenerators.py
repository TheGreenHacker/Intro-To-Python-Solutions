#!/usr/bin/python
import random

"""
Create a generator that generates the squares of numbers up to some number N.
"""
def gensquares(N):
	for x in range(0, N):
		yield x**2

"""
Create a generator that yields "n" random numbers between a low and high number
(that are inputs). 
"""
def rand_num(low,high,n):
	for i in range(0, n):
		yield random.randint(low, high)


def main():

	for x in gensquares(10):
		print(x)
	
	for num in rand_num(1,10,12):
		print(num)
		
	s = 'hello'
	s_iter = iter(s)
	print(next(s_iter))
	print(next(s_iter))
	print(next(s_iter))
	print(next(s_iter))
	print(next(s_iter))

if __name__ == "__main__":
	main()