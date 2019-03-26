"""
#46
March 25th, 2019
Amazon

Given a string, find the longest palindromic contiguous substring. If there are more than one with 
the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic 
substring of "bananas" is "anana".
"""

from typing import List

def longest_palindromic_substring(string: str) -> str:
	substrings = get_all_substrings(string)
	substrings.sort(key=len, reverse=True)
	for substring in substrings:
		if is_palindrome(substring):
			return substring
	return ''

def get_all_substrings(string: str) -> List[str]:
	if len(string) == 0:
		return []
	# Start with substrings of length 1, then form all possible contiguous substrings of length 2,
	# then form all possible contiguous substrings of length 3, and so on.
	substrings = [[(string[i], i) for i in range(len(string))]]
	while len(substrings[-1][0][0]) < len(string):
		substrings += [[
			(pair[0] + string[1 + pair[1]], 1 + pair[1]) 
			for pair in substrings[-1] 
			if 1 + pair[1] < len(string)]]
	return [pair[0] for sublist in substrings for pair in sublist]

def is_palindrome(string: str) -> bool:
	if len(string) in [0, 1]:
		return True
	return string[0] == string[-1] and is_palindrome(string[1:-1])

if __name__ == '__main__':
	string = input().strip().split()
	string = string[0] if string else ''
	print(f'\'{longest_palindromic_substring(string)}\'')