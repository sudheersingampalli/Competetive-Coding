	
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def solve(self, root, key):
        if not root:
            return root
        
        # if key is less than root.data call solve on root.left and append root.left to it
        if key<root.val:
            root.left = self.solve(root.left, key)
        # if key is greater than root.data call solve on root.right and append root.right to it
        elif key>root.val:
            root.right = self.solve(root.right, key)
        
        # when key == root.val
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            root.val = self.finMax(root.left)
            root.left = self.solve(root.left, root.val)

        return root
    
    def finMax(self, A):
        maxi = A.val
        while A.right:
            A = A.right
            maxi = A.val
        return maxi
    

root = TreeNode(3)
root.left=TreeNode(2)
# root.left.right=TreeNode(9)
# root.right=TreeNode(3)
# root.right.right=TreeNode(4)
s = Solution()
print(s.solve(root,2))
