"""
#45
March 24th, 2019
Two Sigma

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

from random import randint

def rand5() -> int:
	return randint(1, 5)

def rand7() -> int:
	# Each 1, 2, 3, 4, 5, 6, 7 is selected with a probability of 3/25.
	# Will loop with a probability of 4/25.
	while True:
		choice = rand5()
		if choice <= 3:
			return rand5()
		elif choice == 4:
			return 6 if rand5() <= 3 else 7
		elif rand5() == 5:
			return 7

if __name__ == '__main__':
	counts = {i + 1: 0 for i in range(7)}
	for _ in range(1000000):
		n = rand7()
		counts[n] += 1
	print(f'One million calls to rand7():\n{counts}')
