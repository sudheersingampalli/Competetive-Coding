# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
        hm = dict()
        if A is None:
            return
        q = list()
        q.append((A,0)) # append the node and corresponding pillar
        res = []
        while( q ):
            ele = q.pop(0)
            # print("ele ", ele)
            node = ele[0]
            pillar = ele[1]
            if pillar in hm.keys():
                hm[pillar].append(node.val) # maintain a hash to store all the elements under a pillar
            else:
                
                hm[pillar] = [node.val]
            # if a node is left to a parent, pillar = pillar-1
            if node.left:
                q.append((node.left,pillar-1))
            # if a node is right to a parent, pillar = pillar+1
            if node.right:
                q.append((node.right, pillar+1))
            
        i = min(hm.keys())
        j = max(hm.keys())

        for k in range(i,j+1):
            res.append(hm[k])
        # print(res)
        return res
