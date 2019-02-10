"""
#2
February 9th, 2019
Uber

Given an array of integers, return a new array such that each element at index i of the new array is 
the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def with_division(numbers: list):
	product = 1
	for a in numbers:
		product *= a
	return [product / a for a in numbers]

def without_division(numbers: list):
	"""
	Credit: github.com/subsr97/daily-coding-problem/blob/master/challenges/product-array-puzzle.py
	"""
	n = len(numbers)
	left = [1] * n
	right = [1] * n

	for i in range(1, n):
		left[i] = numbers[i - 1] * left[i - 1]

	for i in range(n - 2, -1, -1):
		right[i] = numbers[i + 1] * right[i + 1]

	return [left[i] * right[i] for i in range(n)]

if __name__ == "__main__":
	numbers = [int(a) for a in input().strip().split()]
	print(with_division(numbers))
	print(without_division(numbers))