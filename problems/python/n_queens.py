"""
#38
March 17th, 2019
Microsoft

You have an N by N board. Write a function that, given N, returns the number of possible 
arrangements of the board where N queens can be placed on the board without threatening each other, 
i.e. no two queens share the same row, column, or diagonal.
"""

from random import random, sample, choices
from typing import List

Solution = List[int]

def brute_force(n: int) -> List[Solution]:
	options = list(range(n))
	potential_solutions = [[i] for i in options]
	while len(potential_solutions[0]) != n:
		potential_solutions = [s + [o] for s in potential_solutions for o in options]
	return [s for s in potential_solutions if evaluate(s) == 1]

def genetic_algorithm(n : int) -> List[Solution]:
	POPULATION_SIZE = 100
	MUTATION_PROBABILITY = 0.2
	# Randomly-generate population, but no repeated numbers, i.e., no chromosomes with horizontal threats.
	population = [sample(list(range(n)), n) for _ in range(POPULATION_SIZE)]
	# Evaluate population
	fitness = [evaluate(p) for p in population]
	while max(fitness) != 1:
		# Select pairs with repetition
		pairs = [choices(population, weights=fitness, k=2) for _ in range(POPULATION_SIZE // 2 - 1)]
		# Elitism
		best = population[fitness.index(max(fitness))]
		# New generation
		new_generation = [best, best]
		# Order 1 crossover
		for pair in pairs:
			cutoff = sample(list(range(n)), 1)[0]
			offspring = pair[0][:cutoff]
			for gene in pair[1]:
				if gene not in offspring:
					offspring += [gene]
			new_generation += [offspring]
		# Swap mutation
		for offspring in new_generation:
			for i in range(n):
				if random() < MUTATION_PROBABILITY:
					other = sample(list(range(n)), 1)[0]
					aux = offspring[i]
					offspring[i] = offspring[other]
					offspring[other] = aux
		population = new_generation
		# Evaluate population
		fitness = [evaluate(p) for p in population]
	return [p for p in population if evaluate(p) == 1]

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
	n = len(s)
	matrix = [['#'] * n for _ in range(n)] 
	for i in range(n):
		matrix[s[i]][i] = 'Q'
	for row in matrix:
		print(' '.join(row))

if __name__ == '__main__':
	n = int(input().strip().split()[0])
	# Negative numbers and n = 2 and n = 3 have no solutions, but n = 1 does.
	if n < 4:
		print('Q' if n == 1 else str([]))
	else:
		ga_solutions = genetic_algorithm(n)
		print("Genetic algorithm typically only finds one solution, here it is:")
		print_solution(ga_solutions[0])
		print('Finding by brute force...')
		bf_solutions = brute_force(n)
		print(f'Brute force found all {len(bf_solutions)} solutions. Here is one:')
		print_solution(bf_solutions[0])