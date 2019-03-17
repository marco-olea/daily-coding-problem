"""
#4
February 11th, 2019
Stripe

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

from typing import List

def brute_force(numbers: List[int]) -> int:
	numbers.sort()
	fmpi = 0
	# Find first positive integer
	for x in numbers:
		if x > 0:
			fmpi = x
			break
	# If no positive integers or first positive integer is greater than 1:
	if fmpi != 1:
		return 1
	# Find first missing positive integer
	while (fmpi + 1) in numbers:
		fmpi += 1
	return fmpi + 1

def fmpi(numbers: List[int]) -> int:
	if not numbers:
		return 1
	fmpi = max(numbers)
	# Find minimum positive integer
	for x in numbers:
		if x > 0 and x < fmpi:
			fmpi = x
	# If no positive integers or minimum positive integer is greater than 1:
	if fmpi != 1:
		return 1
	# TODO: The following is correct but no longer linear, needs refinement
	# Find first missing positive integer
	while (fmpi + 1) in numbers:
		fmpi += 1
	return fmpi + 1

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	print(brute_force(numbers))
	print(fmpi(numbers))

