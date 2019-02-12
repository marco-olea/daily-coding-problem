"""
#1
February 8th, 2019
Google

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def brute_force(numbers: list, k: int):
	sat = [(a, b) 
		for a in numbers for b in numbers 
		if numbers.index(a) != numbers.index(b) and a + b == k]
	return sat[0] if sat else None

def one_pass(numbers: list, k: int):
	known = {}
	for e in numbers:
		try:
			e_ = known[k - e]
			return (e, k - e)
		except KeyError:
			known[e] = True

if __name__ == '__main__':
	numbers = [int(a) for a in input().strip().split()]
	k = int(input().strip())
	print(brute_force(numbers, k))
	print(one_pass(numbers, k))