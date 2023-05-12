'''
Insert words into a trie. Search words in a trie.

Example Input
Input 1:
A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]

Input 2:
A = [ "tape", "bcci" ]
B = [ "table", "cci" ]


Example Output
Output 1: [1, 0]
Output 2: [0, 0]
'''

class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def solve(self, A, B):
        root = Trie()

        def insert(word):
            curr = root
            for char in word:
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    curr.children[char] = Trie()
                    curr = curr.children[char]
            curr.is_end=True


        def search(word):
            
            curr = root
            for char in word:
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    return 0
            return 1 if curr.is_end else 0
                

        
        for word in A:
            insert(word)
        
        res = []
        for word in B:    
            k = search(word)
            res.append(k)
        
        return res
