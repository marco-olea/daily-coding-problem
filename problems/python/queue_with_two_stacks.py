"""
#53
April 1st, 2019
Apple

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data 
structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, 
which removes it.
"""

from typing import Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
		self.size = 0

	# O(1)
	def enqueue(self, value: T) -> None:
		self.stack1.push(value)
		self.size += 1

	# O(n)
	def dequeue(self) -> T:
		if self.size == 0:
			raise Exception('Empty queue.')
		for _ in range(self.size):
			self.stack2.push(self.stack1.pop())
		value = self.stack2.pop()
		self.size -= 1
		for _ in range(self.size):
			self.stack1.push(self.stack2.pop())
		return value

class Stack(Generic[T]):
	def __init__(self):
		self.last_in = None

	def push(self, value: T) -> None:
		self.last_in = Node(value, self.last_in)

	def pop(self) -> T:
		if self.last_in:
			value = self.last_in.value
			self.last_in = self.last_in.next
			return value
		else:
			raise Exception('Empty stack.')

class Node:
	def __init__(self, value, nextt = None):
		self.value = value
		self.next = nextt

if __name__ == '__main__':
	numbers = [int(i) for i in input().strip().split()]
	stack = Stack()
	queue = Queue()
	for x in numbers:
		stack.push(x)
		queue.enqueue(x)
	print('Stack:\t' + ' '.join([str(stack.pop()) for _ in range(len(numbers))]))
	print('Queue:\t' + ' '.join([str(queue.dequeue()) for _ in range(len(numbers))]))