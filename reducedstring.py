#!/bin/python

from __future__ import print_function
import sys
def super_reduced_string(s):
    # Complete this function
    l=s[0]
    for i in range(1,len(s)):
        if l[-1]==s[i]:
            if len(l) ==1:
                l='0'
            else:
                l = l[:-1]
        elif l =='0':
            l=s[i]
        else:
            l = l+s[i]
    if l=='0':
        return "Empty String"
    else:
        return l          
                
    
    
s = raw_input().strip()
result = super_reduced_string(s)
print(*result,sep='')
