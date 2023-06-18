'''
Problem Description
Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a Binary Search Tree (BST), where each internal node (non-leaf nodes) have exactly one child.

Problem Constraints
1 <= number of nodes <= 100000
Input Format
First and only argument is an integer array denoting the preorder traversal of binary tree.

Output Format
Return a string "YES" if true else "NO".

Example Input
Input 1:
 A : [4, 10, 5, 8]
Input 2:
 A : [1, 5, 6, 4]

Example Output
Output 1:
 "YES"
Output 2:
 "NO"


Example Explanation

Explanation 1:

 The possible BST is:
            4
             \
             10
             /
             5
              \
              8
Explanation 2:

 There is no possible BST which have the above preorder traversal.

'''
import sys

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : list of integers
    # @return a strings
    
    def solve(self, A):
        l = float('-inf')
        r = float('inf')

        root = A[0]
        for i in range(1, len(A)):
            if root < A[i]:
                l = root
            else:
                r = root
            if A[i]<l or A[i]>r:
                return "NO"
            root = A[i]
        return "YES"
