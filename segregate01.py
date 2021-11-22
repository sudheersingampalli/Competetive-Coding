
# segregate 0s and 1s

def seg(a):
    i= 0 
    j = len(a)-1
        
    while i <= j:
        while a[i] == 0:
            i += 1
        while a[j] == 1:
            j -= 1
        if i<j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        
    print(a)



seg([0,1,0,1,0,1,1,1,1,0])
