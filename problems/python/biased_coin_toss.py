"""
#66
April 14th, 2019
Square

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's 
not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

from random import random

def toss_unbiased() -> int:
	coin1, coin2 = 0, 0
	while coin1 == coin2:
		coin1, coin2 = toss_biased(), toss_biased()
	return coin1

def toss_biased() -> int:
	BIAS = 0.25
	return int(random() < BIAS)

if __name__ == '__main__':
	tosses = {0: 0, 1: 0}
	for _ in range(1000000):
		tosses[toss_biased()] += 1
	print(f'One million biased coin tosses: {tosses}')
	tosses = {0: 0, 1: 0}
	for _ in range(1000000):
		tosses[toss_unbiased()] += 1
	print(f'One million unbiased coin tosses: {tosses}')