"""
#54
April 2nd, 2019
Dropbox

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is 
to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain 
all of the digits from 1 to 9.

Implement an efficient sudoku solver.
"""

import numpy as numpy
import random as random
from sympy.utilities.iterables import multiset_permutations

class Sudoku():

	def __init__(self, grid: numpy.array):
		self.grid = grid

	def __str__(self) -> str:
		rows = []
		for row in self.grid:
			as_list = [str(val) if val > 0 else '_' for val in row]
			as_list.insert(3, '|')
			as_list.insert(7, '|')
			rows.append(' '.join(as_list))
		rows.insert(3, '---------------------')
		rows.insert(7, '---------------------')
		return '\n'.join(rows)

	@classmethod
	def from_file(cls, file_name: str):
		with open(file_name, 'r') as file:
			return cls(numpy.array(
				[int(i) for line in file for i in line.strip().split()],
				dtype=numpy.int8).reshape((9, 9)))

	def f(self):
		pool = numpy.array(list(range(1, 10)))
		row_permutations = [
			numpy.array([
				numpy.array(perm) 
				for perm in multiset_permutations(numpy.setdiff1d(pool, row))])
			for row in self.grid]

	def evaluate(self) -> float:
		unique_count = 0
		# Check rows.
		for i in range(9):
			unique_count += numpy.count_nonzero(numpy.unique(self.grid[i, : ]))
		# Check columns.
		for i in range(9):
			unique_count += numpy.count_nonzero(numpy.unique(self.grid[ : , i]))
		# Check 3x3 subgrids.
		for i in range(0, 9, 3):
			for j in range(0, 9, 3):
				unique_count += numpy.count_nonzero(numpy.unique(self.grid[i : i + 3, j : j + 3]))
		# 9 rows + 9 columns + 9 subgrids, expect 9 unique values in each, ergo
		# a correct solution will return 1.
		return unique_count / ((9 + 9 + 9) * 9)

if __name__ == '__main__':
	s = Sudoku.from_file('/Users/marcoivan/Downloads/sudoku.txt')
	print(s)
	s.f()