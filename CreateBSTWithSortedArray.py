# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A:
            if A.val == B:
                return 1
            if B > A.val:
                return self.solve(A.right, B)
            else:
                return self.solve(A.left, B)
        
        return 0
