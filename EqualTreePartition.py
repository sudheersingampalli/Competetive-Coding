# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
class Solution:
	# @param A : root node of tree
	# @return an integer
	sys.setrecursionlimit(10**6)
	def solve(self, A):
		# whole sum should be even
		# one of the subtree as a whole will be involved
		# one of the subtree will be sum/2 then return true
		def totalSum(A):
			if not A: return 0
			return totalSum(A.left)+A.val+totalSum(A.right)
	
		def check(A):
			if A is None: return [0,False]
			l = check(A.left)
			r = check(A.right)
			if l[0] == k/2 or r[0] == k/2: 
				return [l[0]+A.val+r[0],True]
			else: return [l[0]+A.val+r[0],l[1] or r[1]]
				
		k = totalSum(A)
		if k%2 != 0: return 0
	
		res = check(A)
		return 1 if res[1] else 0
	
root = TreeNode(106)
root.right=TreeNode(480)
root.right.left=TreeNode(454)
root.right.right=TreeNode(321)
root.right.right.left=TreeNode(719)

s = Solution()
print(s.solve(root))
