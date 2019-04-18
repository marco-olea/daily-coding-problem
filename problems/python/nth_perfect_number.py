"""
#70
April 18th, 2019
Microsoft

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

from math import log

def get_perfect_number(n: int) -> int:
	result = 10
	while n > 0:
		result = aux = result + 9
		# Evaluate
		sum_digits, next_digit = 0, int(log(result) / log(10))
		while next_digit >= 0:
			sum_digits += result // 10**next_digit
			result %= 10**next_digit
			next_digit -= 1
		if sum_digits == 10:
			n -= 1
		# result was modified; return to original value
		result = aux
	return result

if __name__ == '__main__':
	perfect_numbers = ['{}\t{}'.format(i + 1, get_perfect_number(i + 1)) for i in range(20)]
	print('First 20 perfect numbers:\nn\tf(n)\n' + '\n'.join(perfect_numbers))