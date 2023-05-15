'''
Problem Description
Two elements of a Binary Search Tree (BST), represented by root A are swapped by mistake. Tell us the 2 values, when swapped, will restore the Binary Search Tree (BST).

A solution using O(n) space is pretty straightforward. Could you devise a constant space solution?

Note: The 2 values must be returned in ascending order


Input Format
First and only argument is the head of the tree,A

Output Format
Return the 2 elements which need to be swapped.

Example Input
Input 1: 1 2 3

Input 2:

 
         2
        / \
       3   1



Example Output
Output 1: [2, 1]
Output 2: [3, 1]
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	
	def recoverTree(self, A):
		self.prev = TreeNode(float("-inf"))
		self.first = None
		self.middle = None
		self.last = None
		self.helper(A)
		if not self.last: 
			return [self.first.val, self.middle.val] if self.first.val < self.middle.val else [self.middle.val, self.first.val]
		else: 
			return [self.first.val, self.last.val] if self.first.val < self.last.val else [self.last.val, self.first.val]

	def helper(self, A):
		if A is None: return None

		self.helper(A.left)

		#visit
		if self.prev and A.val < self.prev.val:
			if self.first is None:
				self.first = self.prev
				self.middle = A
			else:
				self.last = A
		
		self.prev = A

		self.helper(A.right)
		
		
s = Solution()		
A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
print(s.recoverTree(A))

		
		
