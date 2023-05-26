'''
Solution: Bring the other persons to the middle person.
'''
class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):
		# start = arr[i]
		# end = cp - mid + i

		seating = [c for c in A]
		c = seating.count('x')
		print(seating, c)
		arr = [-1]*c
		j=0
		for i in range(len(seating)):
			if seating[i] == 'x':
				arr[j] = i
				j += 1
		print(arr)
		jump = 0
		mid = len(arr)//2
		print(mid)
		for k in range(len(arr)):
			start = arr[k]
			end = arr[mid]-mid+k
			jump += abs(end-start)
		return jump%(10**7+3)
	

s = Solution()
A = "....x..xx...x.."
print(s.seats(A))
