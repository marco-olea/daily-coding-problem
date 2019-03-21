"""
#40
March 19th, 2019
Google

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

from sys import getsizeof
from math import log
from typing import List

def brute_force(numbers: List[int]) -> int:
	counts = {}
	for x in numbers:
		try:
			counts[x] += 1
		except KeyError:
			counts[x] = 1
	for x, c in counts.items():
		if c == 1:
			return x

def efficient(numbers: List[int]) -> int:
	BITS = 64
	result = ''
	for i in range(BITS):
		next_bit = 1 << i
		sum_of_bits = sum([(x & next_bit) // next_bit for x in numbers])
		# If m is the sum of the current bit of each number, then 3 | m or 3 | (m-1).
		# If 3 | (m-1), then we know that bit is part of the number that only occurs once.
		result = str(sum_of_bits % 3) + result
	return int(result, 2)

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	print(brute_force(numbers))
	print(efficient(numbers))