"""
#47
March 26th, 2019
Facebook

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a 
function that calculates the maximum profit you could have made from buying and selling that stock 
once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 
5 dollars and sell it at 10 dollars.
"""

from typing import List, Union, TypeVar

T = TypeVar('T', int, float)

def maximum_profit(stock_history: T) -> T:
	max_profit = (0, 0)
	for i in range(len(stock_history)):
		for j in range(i + 1, len(stock_history)):
			if (stock_history[j] - stock_history[i]
					> stock_history[max_profit[1]] - stock_history[max_profit[0]]):
				max_profit = (i, j)
	return max_profit

if __name__ == '__main__':
	stock_history = [int(f) for f in input().strip().split()]
	max_profit = maximum_profit(stock_history)
	if max_profit == (0, 0):
		print('Cannot make a profit.')
	else:
		print(f'Buy at {stock_history[max_profit[0]]}, sell at {stock_history[max_profit[1]]}, '
			f'make a profit of {stock_history[max_profit[1]] - stock_history[max_profit[0]]}.')