'''
use the technique of vertical view and just display the first elements of each pillar
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        hm = dict()
        if A is None:
            return
        q = list()
        q.append((A,0))
        res = []
        while( q ):
            ele = q.pop(0)
            # print("ele ", ele)
            node = ele[0]
            pillar = ele[1]
            if pillar in hm.keys():
                hm[pillar].append(node.val)
            else:
                
                hm[pillar] = [node.val]
            if node.left:
                q.append((node.left,pillar-1))
            if node.right:
                q.append((node.right, pillar+1))
            
        i = min(hm.keys())
        j = max(hm.keys())

        for k in range(i,j+1):
            res.append(hm[k][0]) # fetching only the first ele
        # print(res)
        return res
