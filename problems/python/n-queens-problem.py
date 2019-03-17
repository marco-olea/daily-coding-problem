"""
#38
March 17th, 2019
Microsoft

You have an N by N board. Write a function that, given N, returns the number of possible 
arrangements of the board where N queens can be placed on the board without threatening each other, 
i.e. no two queens share the same row, column, or diagonal.
"""

from typing import List

Solution = List[int]

def brute_force(n: int) -> Solution:
	# Negative numbers and n = 2 and n = 3 have no solutions, but n = 1 does.
	if n < 4:
		return [0] if n == 1 else []
	options = list(range(n))
	potential_solutions = [[i] for i in options]
	while len(potential_solutions[0]) != n:
		potential_solutions = [s + [o] for s in potential_solutions for o in options]
	return [s for s in potential_solutions if evaluate(s) == 1]

def genetic_algorithm(n : int) -> List[Solution]:
	INITIAL_SIZE = 50
	

def evaluate(s: Solution) -> float:
	n = len(s)
	horizontal_threats = n - len(set(s))
	diagonal_threats = 0
	for i in range(n):
		pos = s[i]
		for j in range(1, n - i):
			if s[i + j] == pos - j or s[i + j] == pos + j:
				diagonal_threats += 1
	return 1 / (1 + horizontal_threats + diagonal_threats)

def print_solution(s: Solution) -> None:
	if s:
		n = len(s)
		matrix = [['#'] * n for _ in range(n)] 
		for i in range(n):
			matrix[s[i]][i] = 'Q'
		for row in matrix:
			print(' '.join(row))
	else:
		print('No solutions.')

if __name__ == '__main__':
	n = int(input().strip().split()[0])
	bf_solutions = brute_force(n)
	print(len(bf_solutions))