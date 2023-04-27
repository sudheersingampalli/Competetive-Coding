# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
'''
Right view of a binary tree using Crown Variable
'''
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        if A is None:
            return
        q = list()
        q.append(A)
        crown = A
        res = []
        while( q ):
            ele = q.pop(0)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            if ele == crown:
                res.append(ele.val)    
                
                if q:
                    crown = q[-1]

        return res
