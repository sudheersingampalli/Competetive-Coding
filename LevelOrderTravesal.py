# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

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
        sub = []
        while( q ):
            ele = q.pop(0)
            res.append(ele.val)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            if ele == crown:
                sub.append(res)
                res = []
                if q:
                    crown = q[-1]

        return sub
