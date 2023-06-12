'''
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :


Problem Constraints
1 <= size of the array <= 1000000

Input Format
First argument is an array of digits.

Output Format
Return the array of digits after adding one.

Example Input
Input 1:[1, 2, 3]

Example Output
Output 1:[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.

Solution: reverse the array, add one to the first number and carry fwd the carry.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A = A[::-1]
        
        n = len(A)
        ans = [0]*n
        s = 1+A[0]
        c = 1 if s>9 else 0
        ans[0] = s%10
        
        for i in range(1, n):
            s = c+A[i]
            c = 1 if s>9 else 0
            ans[i] = s%10
        if c == 1:
            ans.append(1)
        # print("ans ", ans)
        k = len(ans)
        while ans[k-1] == 0:
            ans.pop()
            k -= 1
        # print(ans)
        return ans[::-1]

       
