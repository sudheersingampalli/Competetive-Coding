'''
Problem Description
Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.
You need to return the length of such longest common subsequence.
Problem Constraints
1 <= Length of A, B <= 1005

Input Format
First argument is a string A.
Second argument is a string B.

Output Format
Return an integer denoting the length of the longest common subsequence.

Example Input
Input 1:
 A = "abbcdgf"
 B = "bbadcgf"
Input 2:
 A = "aaaaaa"
 B = "ababab"

Example Output
Output 1: 5
Output 2:3
 
'''

# Recursive Solution
import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        A = " "+A
        B = " "+B
        n = len(A) 
        m = len(B) 
        dp = {}
        def helper(A, B, i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            else:
                if i == 0 or j ==0 :
                    dp[(i,j)] = 0
                elif A[i] == B[j]:
                     dp[(i,j)] = 1+helper(A, B, i-1, j-1)
                else:
                     dp[(i,j)] = max ( helper(A,B, i,j-1), 
                                        helper(A,B,i-1, j))
            
            return dp[(i,j)]
        
        helper(A, B, n-1, m-1)
        return dp[(n-1,m-1)]

# Iterative Solution:
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def lcs(self, A, B):
        A = " "+A
        B = " "+B
        n = len(A) 
        m = len(B) 
        
        # Iterative approach
        cost = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j ==0 :
                    cost[i][j] = 0
                elif A[i] == B[j]:
                    cost[i][j] = 1+ cost[i-1][j-1]
                else:
                    cost[i][j] = max (cost[i][j-1], cost[i-1][j])
        print(cost)
        return cost[n-1][m-1]
    
        # if 

s = Solution()
A = "aaa"
B = "aa"
print(s.lcs(A,B))
