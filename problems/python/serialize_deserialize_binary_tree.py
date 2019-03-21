"""
#3
February 10th, 2019
Google

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def serialize(node: Node):
	if node:
		return (
			f'{{"val": "{node.val}", '
			f'"left": {serialize(node.left)}, '
			f'"right": {serialize(node.right)}}}')
	else:
		return '""'

import re
def deserialize(string: Node):
	items = re.split(r',\s', string)
	print(len(items))
	for i in range(len(items) - 1, -1, -1):
		parts = re.split(r'\{|\"|\}|:\s', items[i])
		print(list(filter(None, parts)))


T = Node('root', Node('left', Node('left.left')), Node('right'))
deserialize(serialize(T))

