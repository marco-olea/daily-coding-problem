"""
#50
March 29th, 2019
Microsoft


Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each 
internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def evaluate(node: Node) -> int:
	if not node.left and not node.right:
		return node.value
	lhs, rhs, op = evaluate(node.left), evaluate(node.right), node.value
	return (lhs + rhs if op == '+' 
		else lhs - rhs if op == '-'
		else lhs * rhs if op == '*'
		else lhs // rhs)

if __name__ == '__main__':
	tree = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
	print(evaluate(tree))