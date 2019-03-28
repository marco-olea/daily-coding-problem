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
			f'{{"val": "{str(node.val)}", '
			f'"left": {serialize(node.left)}, '
			f'"right": {serialize(node.right)}}}')
	else:
		return '{}'

def deserialize(serialized: str):
	def deserialize_aux(string: list) -> Node:
		if string[0] == '}':
			while string and string[0] == '}':
				del string[0]
		else:
			del string[:8]
			val = ''.join(string[:string.index('"')])
			del string[:len(val) + 12]
			left = deserialize_aux(string)
			del string[:12]
			right = deserialize_aux(string)
			return Node(val, left, right)
	return deserialize_aux(list(serialized[1:]))

if __name__ == '__main__':
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	print("node = Node('root', Node('left', Node('left.left')), Node('right'))")
	assertion = deserialize(serialize(node)).left.left.val == 'left.left'
	print("assertion = deserialize(serialize(node)).left.left.val == 'left.left'")
	print(f"assertion == {assertion}")

