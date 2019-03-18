"""
#36
March 15th, 2019
Dropbox

Given the root to a binary search tree, find the second largest node in the tree.
"""

from typing import Type, TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
	def __init__(self, e: T):
		self.e = e
		self.parent = None
		self.left = None
		self.right = None

class BinarySearchTree(Generic[T]):

	def __init__(self):
		self.root = None
		self.nodes = 0

	def add(self, *elems: T):
		def add(e: T, node: Node):
			if e <= node.e:
				if node.left:
					add(e, node.left)
				else:
					node.left = Node(e)
					node.left.parent = node
			else:
				if node.right:
					add(e, node.right)
				else:
					node.right = Node(e)
					node.right.parent = node
		self.nodes += len(elems)
		i = 0
		if not self.root:
			self.root = Node(elems[0])
			i = 1
		for e in elems[i:]:
			add(e, self.root)

	def height(self):
		def height(node: Node):
			if node:
				return 1 + max(height(node.left), height(node.right))
			else:
				return -1
		return height(self.root)

	def min(self):
		def min(node: Node):
			if node:
				return min(node.left) if node.left else node
			else:
				return None
		return min(self.root)

	def max(self):
		def max(node: Node):
			if node:
				return max(node.right) if node.right else node
			else:
				return None
		return max(self.root)

	def second_largest(self):
		m = self.max()
		if m:
			return m.parent if m.parent else m
		else:
			return None

if __name__ == '__main__':
	tree = BinarySearchTree()
	tree.add(0,-1,-2,-3,1,2,3,4,5,6,7,8,9,10)
	print(tree.second_largest().e)



