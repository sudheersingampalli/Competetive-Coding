# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def zigzagLevelOrder(self, A):
        queue = []
		stack = []
		res, subres = [],[]
		righttoleft = True
		if A:
			queue.append(A)
			queue.append('#')

		while(queue):
			# push all eles into stack
			while queue[0] != '#':
				ele = queue.pop(0)
				subres.append(ele.val)
				stack.append(ele)
			
			if righttoleft:
				while(stack):
					ele = stack.pop()
					if ele.right: queue.append(ele.right)
					if ele.left : queue.append(ele.left)
			elif not righttoleft:
				while(stack):
					ele = stack.pop()
					if ele.left : queue.append(ele.left)
					if ele.right: queue.append(ele.right)
			
			if queue[0] == '#':
				righttoleft = not righttoleft
				queue.pop(0)
				if queue: queue.append('#')
				res.append(subres)
				subres=[]
		
		return res
        
