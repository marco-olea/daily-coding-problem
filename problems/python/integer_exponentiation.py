"""
#61
April 9th, 2019
Google

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are 
integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

def power(base: int, exp: int):
	size = 0 # Number of bits in exp
	aux_exp = exp
	while aux_exp > 0:
		aux_exp >>= 1
		size += 1
	result, i = 1, 1 
	while i <= size: # result{k} = base^(b{k}) * result{k+1}^2 where exp = b{k}b{k-1}...b{0} (bits)
		result = base ** (exp >> size - i & 1) * result ** 2 # Precedence: (exp >> (size - i)) & 1
		i += 1
	return result

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	base, exp = numbers[0], numbers[1]
	print(power(base, exp))