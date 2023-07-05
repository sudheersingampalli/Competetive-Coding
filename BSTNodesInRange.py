'''
BST nodes in a range

Problem Description
Given a binary search tree of integers. You are given a range B and C.
Return the count of the number of nodes that lie in the given range.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= B < = C <= 109

Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B.
Third argument is an integer C.

Output Format
Return the count of the number of nodes that lies in the given range.

Example Input
Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 12
     C = 20
Input 2:

            8
           / \
          6  21
         / \
        1   7

     B = 2
     C = 20


Example Output
Output 1:

 5
Output 2:

 3


Example Explanation
Explanation 1:

 Nodes which are in range [12, 20] are : [12, 14, 15, 20, 16]
Explanation 2:

 Nodes which are in range [2, 20] are : [8, 6, 7]

Hint: Do an inorder traversal and find number of nodes in the range

'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # do an inorder traversal. Find the nodes in the range.

        arr = []
        def helper(A):
            if A:
                helper(A.left)
                arr.append(A.val)
                helper(A.right)
        helper(A)
        count = 0
        for i in range(len(arr)):
            if arr[i] >= B and arr[i] <= C:
                count += 1
        return count

    
