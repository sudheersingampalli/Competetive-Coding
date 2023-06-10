'''
Problem Description
Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.

In this case, return the length of the longest increasing subsequence.



Problem Constraints
1 <= length(A) <= 2500
0 <= A[i] <= 2500



Input Format
The first and the only argument is an integer array A.



Output Format
Return an integer representing the length of the longest increasing subsequence.



Example Input
Input 1:

 A = [1, 2, 1, 5]
Input 2:

 A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


Example Output
Output 1:

 3
Output 2:

 6


Example Explanation
Explanation 1:

 The longest increasing subsequence: [1, 2, 5]
Explanation 2:

 The possible longest increasing subsequences: [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
'''
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
        n = len(A)
        L = [1]*n
        P = [-1]*n
        for i in range(n):
            for j in range(0,i):
                if A[j]<A[i]: # something to the left of i is less than A[i]
                    if L[j]+1 > L[i]: # if so, check the length of that something+1 if it's greater than current length of i
                        L[i] = L[j]+1 
                        P[i] = j # previous of i would be j
        
        print("L -->", L)
        print("P -->", P)

        return  max(L)
      
      # if the subsequence is asked , then we can use the below code
        # maxlenInd = L.index(maxlen)
        # print("maxlen ", maxlen)
        # print("maxlenInd ", maxlenInd)

        # if maxlenInd == 0: return 1
        # else:
        #     count = 1
        #     # ans = [A[maxlenInd]]
        #     idx = maxlenInd
        #     while( idx != 0):
        #         # ans.append(A[P[idx]])
        #         count += 1 
        #         idx = P[idx]
        #     # print("ans :" ,ans)
        #     return count

