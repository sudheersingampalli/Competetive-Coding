'''
Problem Description
N children are standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum number of candies you must give?



Input Format: The first and only argument is an integer array A representing the rating of children.

Output Format: Return an integer representing the minimum candies to be given.

Example Input
Input 1:  A = [1, 2]
Input 2: A = [1, 5, 2, 1]

Example Output
Output 1: 3
Output 2: 7

Solution:
create two array ltor and rtol; fill ltor[i]=ltor[i-1]+1 if rating[i] > rating[i-1]; slly fill rtol[i]=rtol[i+1]+1 if rating[i]>rating[i+1]
take max(ltor[i], rtol[i]
'''


class Solution:
	# @param A : list of integers
	# @return an integer
	def candy(self, rating):
        ltor = [1]*len(rating)
        rtol = [1]*len(rating)

        for i in range(1, len(rating)):
            if rating[i]>rating[i-1]:
                ltor[i]=ltor[i-1]+1

        for i in range(len(rating)-2, -1, -1):
            if rating[i]>rating[i+1]:
                rtol[i]=rtol[i+1]+1

        res = [1]*len(rating)
        for i in range(len(rating)):
            res[i]= max(ltor[i], rtol[i])
        
        return sum(res)
