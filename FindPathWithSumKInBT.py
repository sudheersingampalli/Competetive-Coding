# Definition for a  binary tree node
'''
Given a BT, find if a path exists such that the sum from root to leaf equals to k
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
import sys
class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):
        def helper(A, B):
            if A is None: return False
            if A.left is None and A.right is None:
                return A.val == B #if its a leaf check if the val == sum else decrement the val of node from B
                    
            return self.hasPathSum(A.left, B-A.val) or self.hasPathSum(A.right, B-A.val)
        
        res = helper(A,B)
        return 1 if res else 0
