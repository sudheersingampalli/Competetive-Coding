'''
Find the level which has max sum and return the sum.
'''


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        # do level order using crown variable.
        # take max
        resSum = float('-inf')
        q = []
        crown = A
        q.append(A)
        intSum = 0
        while(q):
            
            ele = q.pop(0)
            intSum += ele.val
            
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            
            if ele == crown:
                resSum = max(resSum, intSum)
                if q: crown = q[-1]
                intSum = 0
        
        return resSum
