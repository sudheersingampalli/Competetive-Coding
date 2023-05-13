'''
Given a list of N words, find the shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is the prefix of another. In other words, the representation is always possible

Input Format
First and only argument is a string array of size N.

Output Format
Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.


Example Input
Input 1:
 A = ["zebra", "dog", "duck", "dove"]

Input 2:
A = ["apple", "ball", "cat"]

Example Output
Output 1:
 ["z", "dog", "du", "dov"]

Output 2:
 ["a", "b", "c"]
'''

def prefix(self, A):
		root = Trie()

		def insert(word):
			curr = root

			for char in word:
				if char in curr.children: # node has path with char to next node
					curr.children[char+"freq"] += 1
					curr = curr.children[char]
				else:# node has no path with the char
					curr.children[char] = Trie()
					curr.children[char+"freq"] = 1
					curr = curr.children[char]
			curr.is_end=True
			# print trie

		def search(word):
			substr = ""
			curr = root
			
			for char in word:
				if curr.children[char+"freq"] > 1:
					substr += char
					curr = curr.children[char]
				else:
					substr += char
					break
			return substr    
		
		for word in A:
			insert(word)
		
		res = []
		for word in A:    
			k = search(word)
			res.append(k)
		
		return res
  
A = ["apple", "ball", "cat"]
s = Solution()
print(s.prefix(A))
