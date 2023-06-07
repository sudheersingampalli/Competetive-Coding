'''
Problem Description
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.

Output Format
Return an integer, representing the minimum number of steps required.

Example Input
Input 1:
 A = "abad"
 B = "abac"
Input 2:
 A = "Anshuman"
 B = "Antihuman


Example Output
Output 1:1
Output 2:2

Example Explanation
Exlanation 1:

 A = "abad" and B = "abac"
 After applying operation: Replace d with c. We get A = B.
 
Explanation 2:

 A = "Anshuman" and B = "Antihuman"
 After applying operations: Replace s with t and insert i before h. We get A = B.
'''

# NOTE: we are modifying the string by adding an extra space at the beginning for basecase.

# recursive, memoization, bottom up approach
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        A = " "+A
        B = " "+B
        n = len(A) 
        m = len(B) 
        dp = {}
        def helper(A, B, i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            else:
                if i == 0 and j ==0 :
                    dp[(i,j)] = 0
                elif i == 0:
                    dp[(i,j)] = j
                elif j == 0:
                    dp[(i,j)] = i
                elif A[i] == B[j]:
                     dp[(i,j)] = helper(A, B, i-1, j-1)
                else:
                     dp[(i,j)] = min (1+ helper(A,B, i,j-1), 
                                        1+helper(A,B,i-1, j-1),
                                        1+helper(A, B, i-1, j))
            
            return dp[(i,j)]
        
        helper(A, B, n-1, m-1)
        return dp[(n-1,m-1)]


 # iterative top down approach
  class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        A = " "+A
        B = " "+B
        n = len(A) 
        m = len(B) 
        cost = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j ==0 :
                    cost[i][j] = 0
                elif i == 0:
                    cost[i][j] = j
                elif j == 0:
                    cost[i][j] = i
                elif A[i] == B[j]:
                    cost[i][j] = cost[i-1][j-1]
                else:
                    cost[i][j] = min (1+ cost[i][j-1], 
                                        1+cost[i-1][j-1],
                                        1+cost[i-1][j])
        print(cost)
        return cost[n-1][m-1]

s = Solution()
A = "aaa"
B = "aa"
print(s.minDistance(A,B))
