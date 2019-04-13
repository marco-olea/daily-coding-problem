"""
#61
April 9th, 2019
Google

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are 
integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

# Square and multiply algorithm
def power(base: int, exp: int): 
	result, next_bit = 1, 0
	while exp >> next_bit > 0:
		next_bit += 1
	while next_bit > 0: # result{k} = result{k+1}^2 * base^(b{k}) where exp = b{k}b{k-1}...b{0} (bits)
		result = result ** 2 * base ** (exp >> next_bit - 1 & 1) # (exp >> (next_bit - 1)) & 1
		next_bit -= 1
	return result

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	base, exp = numbers[0], numbers[1]
	print(power(base, exp))