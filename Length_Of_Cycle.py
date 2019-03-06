# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:22:53 2019

Program to check the len of the cycle in an array

@author: sudheer.singampalli
"""

# check if there is a loop 1 2 1

d = {}
def checkLoop(a, i, count):
    if i in d:
        return count - d[i]
    else:
        d[i] = count
        count += 1
        print('count ', count)
    if a[i] > len(a)-1:
        return 0
    else:
        return checkLoop(a, a[i], count)

count = 1
a = [1, 2, 3, 1]
k = checkLoop(a, 0, count)
print('k ', k)