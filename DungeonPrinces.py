'''
Problem Description
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Given a 2D array of integers A of size M x N. Find and return the knight's minimum initial health so that he is able to rescue the princess.



Problem Constraints
1 <= M, N <= 500
-100 <= A[i] <= 100

Input Format
First and only argument is a 2D integer array A denoting the grid of size M x N.

Output Format
Return an integer denoting the knight's minimum initial health so that he is able to rescue the princess.



Example Input
Input 1:

 A = [ 
       [-2, -3, 3],
       [-5, -10, 1],
       [10, 30, -5]
     ]
Input 2:

 A = [ 
       [1, -1, 0],
       [-1, 1, -1],
       [1, 0, -1]
     ]


Example Output
Output 1:7
Output 2:1
'''

class Solution:
	# @pararows A : list of list of integers
	# @return an integer
	def calculaterowsinirowsurowsHP(self, A):
		rows = len(A)
		cols = len(A[0])
		dp = [[-1 for j in range(cols)] for i in range(rows)]
		
		def helper(A, i, j):
			if i >= rows or j >= cols:
				return float('inf')
			if i == rows-1 and j==cols-1:
				return max(1,1-A[i][j])
	
			if dp[i][j] != -1:
				return dp[i][j]
			
			a = helper(A, i+1, j)
			b = helper(A, i, j+1)
			dp[i][j] = max(min(a,b)-A[i][j],1)
			return dp[i][j]

		return helper(A, 0,0)

s = Solution()
A = [ 
       [1, -1, 0],
       [-1, 1, -1],
       [1, 0, -1]
     ]
print(s.calculaterowsinirowsurowsHP(A))
