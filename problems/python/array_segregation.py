"""
#35
March 14th, 2019
Google

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so 
that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become 
['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

from typing import List

def segregate(array: List[str]) -> List[str]:
	def swap(i: int, j: int) -> None:
		aux = array[i]
		array[i] = array[j]
		array[j] = aux
	def passs():
		k, l = 0, len(array) - 1
		for i in range(len(array)):
			if array[i] == 'R':
				while k < len(array) and array[k] == 'R':
					k += 1
				if k < i:
					swap(i, k)
			elif array[i] == 'B':
				while l >= 0 and array[l] == 'B':
					l -= 1
				if l > i:
					swap(i, l)
	# Why two? No idea, it works.
	passs()
	passs()

if __name__ == '__main__':
	array = [str(c).upper() for c in input().strip().split()]
	print(array)
	segregate(array)
	print(array)