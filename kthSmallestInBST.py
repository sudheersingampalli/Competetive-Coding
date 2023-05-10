'''
Solution: Have an inorder traversal and return n-1st node from the inorder traversal
'''
import sys
sys.setrecursionlimit(10**6)

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

  def kthsmallest(self, A, B):
        res = []
        def inorder(A):
            if A:
                inorder(A.left)
                res.append(A.val)                
                inorder(A.right)
        
        inorder(A)
        return res[B-1]
    

root = TreeNode(2)
root.right=TreeNode(3)
root.left=TreeNode(1)


s = Solution()
print(s.kthsmallest(root,2))
