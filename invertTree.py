# Definition for a  binary tree node
import sys
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):
        sys.setrecursionlimit(10**6)
        if A:
          
           A.right, A.left =  self.invertTree(A.left), self.invertTree(A.right) # swap left and right subtrees.
        
        return A
