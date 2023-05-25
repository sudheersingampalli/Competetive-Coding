'''
There are N jobs to be done, but you can do only one job at a time.
Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.
Your aim is to select jobs in such a way so that you can finish the maximum number of jobs.
Return the maximum number of jobs you can finish.

Input Format
The first argument is an integer array A of size N, denoting the start time of the jobs.
The second argument is an integer array B of size N, denoting the finish time of the jobs.

Output Format
Return an integer denoting the maximum number of jobs you can finish.

Example Input
Input 1:
 A = [1, 5, 7, 1]
 B = [7, 8, 8, 8]
Input 2:
 A = [3, 2, 6]
 B = [9, 8, 9]

Example Output
Output 1: 2
Output 2: 1


Example Explanation
Explanation 1:

 We can finish the job in the period of time: (1, 7) and (7, 8).
Explanation 2:

 Since all three jobs collide with each other. We can do only 1 job.


Solution: Order the finish times in asc order. if the start time of next job is > finish time of last job increment the answer.
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, startTime, finishTime):
        finishTime, startTime = zip(*sorted(zip(finishTime,startTime)))

        ans = 1
        end = finishTime[0]
        for i in range(1, len(finishTime)):
            if startTime[i] >= end:
                ans += 1
                end = finishTime[i]
        
        return ans
