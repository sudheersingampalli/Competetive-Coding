'''
Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the minimum count.


Example Input
Input 1: A = 6
Input 2: A = 5

Example Output
Output 1: 3
Output 2: 2


Example Explanation
Explanation 1:

 Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
 Minimum count of numbers, sum of whose squares is 6 is 3. 
Explanation 2:

 We can represent 5 using only 2 numbers i.e. 12 + 22 = 5

'''


class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):
        
        arr = [float('inf')]*(A+1)

        arr[0] = 0

        for i in range(1, A+1):
            x = 1
            while x * x <= i:
                arr[i] = min(arr[i], arr[i-x*x])+1
                x += 1  # Increment x by 1 in each iteration
        
        return arr[A]

s = Solution()
print(s.countMinSquares(12))
