# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:49:02 2019

Program to find the pairs having the mentioned sum.

Idea :: Put the ele as key and compliment as value.
before inserting, check if compliment is existing as a key.
if yes, append it to the list.

OR

Put the compliement as key and ele as value
before inserting, check if the ele is existing as a key

@author: sudheer.singampalli
"""

l = []
def pairs(a, sum):
    d = {}    
    print(a)
    for ele in a:
        compliment = sum - ele
        if compliment in d:
            l.append((compliment, d[compliment]))
            print(l)
        else:
            d[ele] = compliment
            print(d)
            
    return l
d = {}
a = [5, 3, 6, 9, 1, 2]
k = 7
res = pairs(a, k)
print ('paris are ', res)