'''
Q1. Generate all Parentheses II
Problem Description
Given an integer A pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*A.


Input Format
First and only argument is integer A.

Output Format
Return a sorted list of all possible parenthesis.

Example Input
Input 1:A = 3
Input 2:A = 1

Example Output
Output 1:
[ "((()))", "(()())", "(())()", "()(())", "()()()" ]

Output 2:
[ "()" ]


Example Explanation
Explanation 1:

 All paranthesis are given in the output list.
Explanation 2:

 All paranthesis are given in the output list.

Solution:: Use backtracking
'''
class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        
        backtrack(0,0)
        return res

s = Solution()
s.generateParenthesis(3)
