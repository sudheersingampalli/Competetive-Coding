'''
Given a BT, check if we can divide the tree into two parts such that their sum is equal
Hints:
1. Check total sum. If sum%2 !=0 return false
2. One of the subtree should be equal to sum/2
'''

import sys
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    sys.setrecursionlimit(10**6)
    def solve(self, A):
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
