'''
Input  :  str = 'wwwwaaadexxxxxx'
Output : 'w4a3d1e1x6'

Input  :  str = 'aaadeaaccc'
Output : 'a3d1e1a2c2'

Idea is to keep inserting into the dictionary until we get same character.
When the character is diffrent, we print the dictionary and clear it and insert the new character.

'''
def runLengthEncode(seq):
	dict = {}
	ls = []
	dict[seq[0]] = 1
	for c in seq[1:]:
		if c in dict.keys():
			dict[c] += 1			
		else:
			for k, v in dict.items():
				ls.append(k)
				ls.append(v)
			dict.clear()
			dict[c] = 1
	for k, v in dict.items():
		ls.append(k)
		ls.append(v)
	ls = [str(i) for i in ls]
	print (''.join(ls))


runLengthEncode('wwwwaaadexxxxxxaa')




