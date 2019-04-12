"""
#62
April 11th, 2019
Facebook

There is an M by N matrix of zeroes. Given M and N, write a function to count the number of ways of 
starting at the top-left corner and getting to the bottom-right corner. You can only move right or 
down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the 
bottom-right:

  - Right, then down
  - Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

def count_traversals(m: int, n: int) -> int:
	if m == 1 or n == 1:
		return 1
	return count_traversals(m - 1, n) + count_traversals(m, n - 1)

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	m, n = numbers[0], numbers[1]
	print(count_traversals(m, n))