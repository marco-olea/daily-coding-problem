"""
#65
April 13th, 2019
Amazon

Given a M by N matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

from typing import TypeVar, List

T = TypeVar('T')
Matrix = List[List[T]]

def clockwise_spiral(matrix: Matrix) -> List[T]:
	order = []
	while matrix:
		order += matrix[0]
		del matrix[0]
		if matrix:
			for row in matrix:
				order.append(row[-1])
				del row[-1]
		if matrix:
			order += matrix[-1][::-1]
			del matrix[-1]
		if matrix:
			for row in matrix[::-1]:
				order.append(row[0])
				del row[0]
	return order

if __name__ == '__main__':
	EXAMPLE = [
		[1,  2,  3,  4,  5, 6],
		[7,  8,  9,  10, 11, 12],
		[13, 14, 15, 16, 17, 18],
		[19, 20, 21, 22, 23, 24],
		[25, 26, 27, 28, 29, 30]]
	for row in EXAMPLE:
		print('\t'.join([str(e) for e in row]))
	print(' '.join([str(e) for e in clockwise_spiral(EXAMPLE)]))








