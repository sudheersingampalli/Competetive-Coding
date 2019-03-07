# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:29:28 2019

Segregate even and odd numbers:
    IP :: 12, 34, 45, 9, 8, 90, 3
    OP :: 12, 34, 8, 90, 45, 9, 3
@author: sudheer.singampalli


12, 34, 90, 8, 9, 45, 3
            e   s       
"""


def segregate(a):
    s = 0
    e = len(a) - 1
    while s <= e :
        while a[s] % 2 == 0:
            s += 1
        while a[e] % 2 != 0:
            e -= 1
        if s <= e:
            a[s], a[e] = a[e], a[s]
    return a

l = [12, 34, 45, 9, 8, 90, 3]
print(l)
newarr = segregate(l)
print(newarr)
    