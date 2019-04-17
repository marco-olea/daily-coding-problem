"""
#69
April 17th, 2019
Facebook

Given a list of integers, return the largest product that can be made by multiplying any three 
integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

from typing import List

def brute_force(numbers: List[int]) -> int:
	n, largest = len(numbers), 0
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j + 1, n):
				product = numbers[i] * numbers[j] * numbers[k]
				largest = product if product > largest else largest
	return largest

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	print(brute_force(numbers))
