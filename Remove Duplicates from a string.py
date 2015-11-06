__author__ = 'SS'

# OrderedDictionary is used to retain the input order. 
from collections import OrderedDict
dict=OrderedDict()
#function which removes the duplicates
def remove_dup(str): 
    string=''
    for c in str:
       if c not in dict.keys():
            dict[c]=1

    for k in dict.keys():
        string +=  k
    return string

if __name__ == '__main__':
    s=remove_dup('abcabcdued')
    print(s)
