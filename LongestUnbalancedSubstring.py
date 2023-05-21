'''
Given a string with '{' and '}' characters. find the longest unbalanced substring.
Solution: if string is balanced then return len(string-1) if not return len(string)
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        for c in A:
            if c == '{':
                stack.append(c)
            else:
                if c == '}' and not stack:
                    return len(A)
                if c == '}' and stack.pop() == '{':
                    pass
                
                
        if stack: return len(A) 
        else: return len(A)-1
        
