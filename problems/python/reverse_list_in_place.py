"""
#73
April 21st, 2019
Google

Given the head of a singly linked list, reverse it in-place.
"""

from typing import TypeVar, Generic

T = TypeVar('T')

class MyList(Generic[T]):

	def __init__(self):
		self.head = None
		self.length = 0

	def append(self, e: T) -> None:
		def append(e: T, myList: MyList) -> None:
			if myList.head:
				append(e, myList.tail)
			else:
				myList.head = e
				myList.tail = MyList()
			myList.length += 1
		append(e, self)

	def reverse(self) -> None:
		def swap(current: MyList, i: int) -> None:
			if current.tail and i > 1:
				aux = current.head
				current.head = current.tail.head
				current.tail.head = aux
				swap(current.tail, i - 1)
		for i in range(self.length, 0, -1):
			swap(self, i)

	def __len__(self):
		return self.length

	def __iter__(self):
		self.next = self
		return self

	def __next__(self):
		if self.next:
			e = self.next.head
			self.next = self.next.tail
			return e
		else:
			raise StopIteration

if __name__ == '__main__':
	myList = MyList()
	for x in [int(i) for i in input().strip().split()]:
		myList.append(x)
	myList.reverse()	
	for x in myList:		
			print(x)