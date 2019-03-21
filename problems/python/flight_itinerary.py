"""
#41
March 20th, 2019
Facebook

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. 
If there are multiple possible itineraries, return the lexicographically smallest one. 
All flights must be used in the itinerary.

For example, given the list of flights 
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', 
you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also 
a valid itinerary. However, the first one is lexicographically smaller.

sfo hko yyz sfo yul yyz hko ord
yul
"""

from typing import List

def f(flights, start):
	origins = {
		origin: [flight[1] for flight in flights if flight[0] == origin] 
		for origin in [place for flight in flights for place in flight]}
	

if __name__ == '__main__':
	input_1 = [s.upper() for s in input().strip().split()]
	input_2 = input().strip().split()
	flights = [(input_1[i], input_1[i+1]) for i in range(0, len(input_1), 2)]
	start = input_2[0].upper()
	f(flights, start)