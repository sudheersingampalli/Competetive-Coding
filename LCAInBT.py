'''
If B or C is not present in the tree, return -1
else return the LCA.
'''

# Definition for a  binary tree node
# class TreeNode:
def __init__(self, x):
  self.val = x
  self.left = None
  self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def lca(self, A, B, C):
        allnodes = []
      # inorder traversal to make a note of all the nodes to check later if B and C exists
        def inorder(A):
            if A:
                inorder(A.left)
                allnodes.append(A.val)
                inorder(A.right)

        def lcahelper(A, B, C):
            if A is None: return None
            if A.val == B or A.val == C: return A

            L = lcahelper(A.left, B, C)
            R = lcahelper(A.right, B, C)

            if L and R: return A
            if L: return L
            if R: return R
            else : return None
        
        arr = inorder(A)
        if B not in allnodes or C not in allnodes:
            return -1
        res = lcahelper(A, B, C)
        # print("res", res.val)
        return res.val if res else None

			
