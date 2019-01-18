'''
Kadane's algorithm

given an array 
having both positive and negative numbers.
Print the maximum sum of that array

Eg : [-2, -3, 4, -1, -2, 1, 5, -3]
'''
l = [4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2]
maxSum = 0
sumsofar = 0
si = 0
ei = 0
s =0
for i in range(len(l)):
	sumsofar += l[i]
	if maxSum < sumsofar:
		maxSum = sumsofar
		ei = i
		si = s
	if sumsofar < 0:
		sumsofar = 0
		s = i+1


print('maxSum is ', maxSum)
print('si is {} ei is {}'.format(si, ei))
print(l[si:ei+1])