'''
Find the LCA in a BST. 
It is very simple. Traverse from the root. The node where there is a divergence in the path is the LCA.
'''

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        curr = A
        while(curr):
          # if B and C are greater than curr, go to right and search
            if B > curr.val and C > curr.val:
                curr = curr.right
          # if B and C are less than curr, go to left and search
            elif B < curr.val and C < curr.val:
                curr = curr.left
          # It means, either once of the node is equal to curr or both don't fall in same sub tree. So, return this node
            else:
                return curr.val
