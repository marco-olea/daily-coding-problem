"""
#33
March 12th, 2019
Microsoft

Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

def running_median(A: list):
	B = []
	for x in A:
		B += [x]
		i = len(B) - 1
		while i > 0 and B[i] > B[i - 1]:
			aux = B[i]
			B[i] = B[i - 1]
			B[i - 1] = aux
			i -= 1
		m = int(len(B) / 2)
		print(str(B[m] if len(B) % 2 == 1 else (B[m] + B[m - 1]) / 2))

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	running_median(numbers)
