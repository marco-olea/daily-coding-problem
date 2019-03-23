"""
#43
March 22nd, 2019
Amazon

Implement a stack that has the following methods:

  - push(val), which pushes an element onto the stack.

  - pop(), which pops off and returns the topmost element of the stack. If there are no elements in 
    the stack, then it should throw an error or return null.

  - max(), which returns the maximum value in the stack currently. If there are no elements in the 
    stack, then it should throw an error or return null.

Each method should run in constant time.
"""

from typing import TypeVar, Generic, List

T = TypeVar('T', int, float)

class Stack(Generic[T]):

	def __init__(self):
		self.last_in = None
		self.count = 0
		self.max_value = None

	def push(self, value: T) -> None:
		if not self.max_value or value <= self.max_value:
			node = Node(value)
		else:
			node = Node(2 * value - self.max_value)
		if not self.max_value or value > self.max_value:
			self.max_value = value
		node.previous = self.last_in
		self.last_in = node
		self.count += 1

	def pop(self) -> T:
		if self.last_in:
			value = self.last_in.value
			if value > self.max_value:
				value = self.max_value
				self.max_value = 2 * self.max_value - self.last_in.value
			self.last_in = self.last_in.previous
			self.count -= 1
			return value
		else:
			raise Exception('Stack is empty.')

	def max(self) -> T:
		return self.max_value

	def size(self) -> int:
		return self.count

	def __str__(self):
		def __str(s: List[str], node: Node) -> None:
			if node:
				s.append(str(node.value))
				__str(s, node.previous)
		s = []
		__str(s, self.last_in)
		return ' '.join(s)

class Node(Generic[T]):
	def __init__(self, value: T):
		self.value = value
		self.previous = None

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	stack = Stack()
	for x in numbers:
		stack.push(x)
	for _ in range(stack.size()):
		print(f'max(): {stack.max()}\tpop(): {stack.pop()}')