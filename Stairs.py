'''
Problem Description
You are climbing a staircase and it takes A steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Return the number of distinct ways modulo 1000000007

Input Format
The first and the only argument contains an integer A, the number of steps.

Output Format
Return an integer, representing the number of ways to reach the top.

Example Input
Input 1: A = 2
Input 2: A = 3

Example Output
Output 1: 2
Output 2: 3
'''
import sys
class Solution:
	sys.setrecursionlimit(10**6)
	def climbStairs(self, A):
		d = dict()
		def helper(A):
			if A == 1: return 1
			if A == 2: return 2
			if A in d:
                # print("found A")
				return d[A]
			else:
				k=(helper(A-1)+helper(A-2))%1000000007
				d[A] = k
				return k
		
        return helper(A)
