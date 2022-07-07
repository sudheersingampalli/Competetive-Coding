#Problem : https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1#

def find(arr,n,x):
    l = 0
    r = n-1
    first = last = -1
    
    
    # first index
    while l<=r:
        mid = l+(r-l)//2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid -1
        else:
            first = mid
            r = mid -1
    
    # last index
    l = 0
    r = n-1
    while l<=r:
        mid = l+(r-l)//2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid -1
        else:
            last = mid
            l = mid +1
    
    return [first, last]
