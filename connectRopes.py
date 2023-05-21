'''
Problem Description
You are given an array A of integers that represent the lengths of ropes.
You need to connect these ropes into one rope. The cost of joining two ropes equals the sum of their lengths.
Find and return the minimum cost to connect these ropes into one rope.

Input Format
The only argument given is the integer array A.

Output Format
Return an integer denoting the minimum cost to connect these ropes into one rope.


Example Input
Input 1: A = [1, 2, 3, 4, 5]
Input 2: A = [5, 17, 100, 11]

Example Output
Output 1:33
Output 2: 182

Example Explanation
Explanation 1:

 Given array A = [1, 2, 3, 4, 5].
 Connect the ropes in the following manner:
 1 + 2 = 3
 3 + 3 = 6
 4 + 5 = 9
 6 + 9 = 15

 So, total cost  to connect the ropes into one is 3 + 6 + 9 + 15 = 33.
Explanation 2:

 Given array A = [5, 17, 100, 11].
 Connect the ropes in the following manner:
 5 + 11 = 16
 16 + 17 = 33
 33 + 100 = 133

 So, total cost  to connect the ropes into one is 16 + 33 + 133 = 182.
'''
import heapq
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        heapq.heapify(A)
        print("minheap :", A)
        newlen = 0
        resArr = []
        while len(A)>1:
            min1 = heapq.heappop(A)
            if A:
                min2 = heapq.heappop(A)
            else: min2= 0
            print(min1, min2)
            newlen = min1+min2
            resArr.append(newlen)
            heapq.heappush(A, newlen)
            print("new minheap :", A)
            print("res arr :", resArr)
        return sum(resArr)
    

s = Solution()
A = [1, 2, 3, 4, 5]
print(s.solve(A))
