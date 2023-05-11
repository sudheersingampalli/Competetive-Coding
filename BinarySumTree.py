# Definition for a  binary tree node
'''
Check if each node in a tree is equal to the sum of it's nodes in left and right subtrees.
'''
import sys
sys.setrecursionlimit(10**6)

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer

    def solve(self, A):

        def helper(A):
            
            if A is None:
                return [True, 0]
            
            if A.left is None and A.right is None:
                return [True, A.val]
            
            l = helper(A.left)
            r = helper(A.right)
            if ((A.val == l[1]+r[1]) and (l[0] and r[0]) ):
                return [True, A.val+l[1]+r[1]]
            else:
                return [False, A.val]

        return 1 if helper(A)[0] else 0
        
