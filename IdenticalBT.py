'''
Check if two trees are identical or not
'''
# class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):

        def helper(A, B):
            if A is None and B is None:
                return True
            if A and B:
                if A.val != B.val:
                    return False
                else:
                    return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)
        return 1 if helper(A, B) else 0
