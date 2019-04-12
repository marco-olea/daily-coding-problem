"""
#63
April 11th, 2019
Microsoft

Given a 2D matrix of characters and a target word, write a function that returns whether the word 
can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, 
given the target word 'MASS', you should return true, since it's the last row.
"""

from typing import List, Tuple, Optional

def search_word(matrix: List[List[str]], word: str) -> Optional[Tuple[int, int, str]]:
	for i in range(len(matrix)):
		for j in range(len(matrix[i]) - len(word) + 1):
			if word == ''.join(matrix[i][j:j + len(word)]):
				return (i, j, 'right')
	for j in range(len(matrix[0])):
		for i in range(len(matrix) - len(word) + 1):
			if word == ''.join([matrix[k][j] for k in range(i, i + len(word))]):
				return (i, j, 'down')

if __name__ == '__main__':
	matrix = [
		['F', 'A', 'C', 'I'], 
		['O', 'B', 'Q', 'P'], 
		['A', 'N', 'O', 'B'], 
		['M', 'A', 'S', 'S']]
	print('[{},\n {},\n {},\n {}]'.format(matrix[0], matrix[1], matrix[2], matrix[3]))
	print('FOAM = ' + str(search_word(matrix, 'FOAM')))
	print('MASS = ' + str(search_word(matrix, 'MASS')))
	print('NO = ' + str(search_word(matrix, 'NO')))
	print('PBS = ' + str(search_word(matrix, 'PBS')))
	print('WORD = ' + str(search_word(matrix, 'WORD')))