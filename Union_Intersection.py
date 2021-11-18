## Given two arrays find the Union and Intersection

# intersection

def intersection(a,b):
    if len(a)== 0 or len(b)==0:
        return "No intersection"
    intersection = []
    i,j = 0,0
    while i<len(a) and j<len(b):
        print('iteration--->',i,j)
        if a[i] == b[j]:
            intersection.append(a[i])
            i +=1
            j +=1
        elif a[i]<b[j]:
            i += 1
        elif a[i]>b[j]:
            j +=1
    
    print(intersection)
    
def union(a,b):
    # all elements 
    if len(a)== 0 or len(b)==0:
        return "No union"
    union = []
    i,j = 0,0
    while i<len(a) or j<len(b):
        print('iteration--->',i,j)
        if i==len(a):
            union += b[j:]
            # union.append((k for k in b[j:]))
            break
        elif j==len(b):
            union += a[i:]
            
            break
        if a[i] == b[j]:
            union.append(a[i])
            i +=1
            j +=1
        elif a[i]<b[j]:
            union.append(a[i])
            i += 1
        elif a[i]>b[j]:
            union.append(b[j])
            j +=1
    
    print(union)
intersection([1,2,3,4],[5,6])
union([1,2,3,4],[3,4,5,6])  
