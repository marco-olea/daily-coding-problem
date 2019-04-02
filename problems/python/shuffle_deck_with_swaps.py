"""
#51
March 30th, 2019
Facebook

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an 
input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randint

def shuffled_deck():
	deck = [rank + suit 
		for suit in ['s', 'c', 'd', 'h']
		for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']]
	for i in range(52):
		j = 52 - randint(1, 52 - i)
		aux = deck[i]
		deck[i] = deck[j]
		deck[j] = aux
	return deck

if __name__ == '__main__':
	print(shuffled_deck())