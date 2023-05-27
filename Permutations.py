'''
Given an integer array A of size N denoting collection of numbers , return all possible permutations.

NOTE:

No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Return the answer in any order

Solution:
Use Backtracking.
We use two arrays:
1. used -> denotes if the ele is visited or not
2. subans -> which has the answer
'''

class Solution:
	def permute(self, A):
		ans = []
		n = len(A)
		used = [0]*n
		subans = [0]*n
		
		def helper(subans, ind, used):
			if ind == n:
				ans.append(subans)
				return
			else:
				for i in range(n):
					if used[i] == 0:
						used[i] = 1
						subans[ind] = A[i]
						helper(subans[:], ind+1, used)
						used[i] = 0
		
		helper(subans, 0, used)
		return ans

s = Solution()
A = [1, 2, 3]
print(s.permute(A))
