'''
Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109

Input Format
The first argument is an array of integers.

Output Format
Return a string representing the largest number.

Example Input
Input 1:A = [3, 30, 34, 5, 9]
Input 2:A = [2, 3, 9, 0]

Example Output
Output 1:"9534330"
Output 2:"9320"
'''
import functools
class Solution:
    # @param A : tuple of integers
    # @return a strings

    def compare(self, x, y):
        # print(x, y)
        if x+y >= y+x:
            return -1
        else: return 1

    def largestNumber(self, A):
        n = len(A)

        newArr = [str(i) for i in A]
        # print("newArr :", newArr)
        l = 0
        for i in range(n):
            if newArr[i] == "0":
                l += 1
        
        if l == n: return "0"

        sorted_l = sorted(newArr, key=functools.cmp_to_key(self.compare))
        # print(sorted_l)

        return "".join(sorted_l)    
            
