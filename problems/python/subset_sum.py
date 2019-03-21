"""
#42
March 21st, 2019
Google

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

from typing import Optional, List
from power_set import power_set

# O(2^n)
def brute_force(numbers: List[int], k) -> Optional[List[int]]:
	subsets = power_set(numbers)
	for subset in subsets:
		if sum(subset) == k:
			return list(subset)

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	k = int(input().strip().split()[0])
	print(brute_force(set(numbers), k))