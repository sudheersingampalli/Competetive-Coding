'''
Q1. Symmetric Binary Tree
Solved
feature icon
Using hints is now penalty free
Use Hint
Problem Description
Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is the root node of the binary tree.

Output Format
Return 0 / 1 ( 0 for false, 1 for true ).

Example Input
Input 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3

Input 2:

    1
   / \
  2   2
   \   \
   3    3


Example Output
Output 1:1
Output 2:0
 
 '''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import sys
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : root node of tree
	# @return an integer

    
	def isSymmetric(self, A):
        
        def helper(lt, rt):
            if not lt and not rt:
                return 1
            elif not lt or not rt or lt.val != rt.val:
                return 0
            return helper(lt.left, rt.right) and helper(lt.right, rt.left)

        if not A:
            return 1
        
        return helper(A.left, A.right)
