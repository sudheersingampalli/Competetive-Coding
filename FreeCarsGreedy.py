'''
Given two arrays, A and B of size N. A[i] represents the time by which you can buy the ith car without paying any money.

B[i] represents the profit you can earn by buying the ith car. It takes 1 minute to buy a car, so you can only buy the ith car when the current time <= A[i] - 1.

Your task is to find the maximum profit one can earn by buying cars considering that you can only buy one car at a time.

NOTE:

You can start buying from time = 0.
Return your answer modulo 109 + 7.

Example Input
Input 1:
 A = [1, 3, 2, 3, 3]
 B = [5, 6, 1, 3, 9]

Input 2:
 A = [3, 8, 7, 5]
 B = [3, 1, 7, 19]


Example Output
Output 1:20
Output 2:30
'''

import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, expiry, profit):
        expiry, profit = zip(*sorted(zip(expiry, profit)))
        # expiry (1, 2, 2, 4, 4, 6, 6, 7, 8, 8) 
        # profit (8, 7, 9, 7, 8, 5, 7, 11, 4, 10)

        res = []
        time = 0
        totalProfit = 0
        for i in range(len(expiry)):
            if time < expiry[i]:
                heapq.heappush(res, profit[i])
                time += 1
                totalProfit += profit[i]
            else:
                top = heapq.heappop(res)
                if profit[i] > top:
                    totalProfit -= top
                    totalProfit += profit[i]
                    heapq.heappush(res, profit[i])
                else:
                    heapq.heappush(res, top)
        return totalProfit%(10**9 + 7)

s = Solution()
A = [6,8,5,4,2,1,6,4,2,8,5,4,4,8,8,5,3,4,4,5,8,5,5,7,2,4,5,2,6]
B = [11,10,8,10,5,7,5,9,8,7,11,5,7,4,7,9,8,5,5,5,8,11,8,4,4,2,9,6,6]
print(s.solve(A, B))
