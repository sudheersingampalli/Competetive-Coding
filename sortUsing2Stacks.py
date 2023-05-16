'''
Given a stack of integers A, sort it using another stack.
Return the array of integers after sorting the stack using another stack.


Input Format
The only argument is a stack given as an integer array A.

Output Format
Return the array of integers after sorting the stack using another stack.

Example Input
Input 1:
 A = [5, 4, 3, 2, 1]
Input 2:
 A = [5, 17, 100, 11]


Example Output
Output 1: [1, 2, 3, 4, 5]
Output 2: [5, 11, 17, 100]
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # if stack1 is empty, push the ele
        # if stack1 is not empty, if ele is > top(Stack1) AND while ele > stack2.top pop stack2 and push to stack1 push ele 
        # push ele to stack1
        #  else 
        #    while ele < top(Stack1)..  pop top(stack1), push in stack2
        # push ele to stack1
        # at the end push all eles from stack2 to sack1
        stack1 = []
        stack2 = []
        for ele in A:
            if len(stack1) == 0:
                stack1.append(ele)
            else:
                if ele > stack1[-1]:
                    while(stack2 and ele > stack2[-1]):
                        t= stack2.pop()
                        stack1.append(t)
                    stack1.append(ele)
                else:
                    while(stack1 and ele < stack1[-1]):
                        t = stack1.pop()
                        stack2.append(t)
                    stack1.append(ele)
        
        while(stack2):
            t = stack2.pop()
            stack1.append(t)
        
        return stack1
      
s = Solution()
A = [1,2,3,4, 10, 9, 8 ,7, 11, 10]
print(s.solve(A))
