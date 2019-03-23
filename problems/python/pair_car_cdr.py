"""
#5
February 12th, 2019
Jane Street

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that 
pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
"""

def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair

def car(pair):
	return pair(lambda *args: args[0])

def cdr(pair):
	return pair(lambda *args: args[1])

if __name__ == '__main__':
	args = input().strip().split()
	pair = cons(args[0], args[1])
	print(f'car: {car(pair)}\ncdr: {cdr(pair)}')