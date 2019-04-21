"""
#71
April 19th, 2019
Two Sigma

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

from random import randint

def rand7() -> int:
	return randint(1, 7)

def rand5() -> int:
	result = None
	while not result:
		rnd = rand7()
		if rnd <= 5:
			result = rnd
	return result

if __name__ == '__main__':
	counts = {i + 1: 0 for i in range(5)}
	for _ in range(1000000):
		n = rand5()
		counts[n] += 1
	print(f'One million calls to rand5():\n{counts}')