# Definition for a  binary tree node
import sys
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	sys.setrecursionlimit(10*6)
	def isValidBST(self, A):
		return self.isValidBSTUtil(A, float('-inf'), float('inf'))
	
	def isValidBSTUtil(self, A, mini, maxi):
		if not A: return 1
		if A.val<mini or A.val>maxi:
			return 0
		return self.isValidBSTUtil(A.left, mini, A.val-1) and self.isValidBSTUtil(A.right, A.val+1, maxi)

	
		
	
				
root = TreeNode(2147483647)
# root.left=TreeNode(1)
# root.left.right=TreeNode(9)
# root.right=TreeNode(3)
# root.right.right=TreeNode(4)
s = Solution()
print(s.isValidBST(root))
