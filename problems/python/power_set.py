"""
#37
March 16th, 2019
Google

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

from typing import Set, TypeVar

T = TypeVar('T')

def power_set(s: Set[T]) -> Set[Set[T]]:
	power = {frozenset()}
	while len(power) != 2**len(s):
		power |= {frozenset(y | {x}) for y in power for x in s}
	return power

if __name__ == '__main__':
	power = list(power_set({int(i) for i in input().strip().split()}))
	power.sort(key=len)
	for subset in power:
		print(set(subset))