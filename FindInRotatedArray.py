'''
link : https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array0959/1
'''

def Search(arr,n,k):
    left = 0
    right = n-1
    
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == k:
            return mid
        
        if arr[left]<arr[mid]: # left is sorted
            if arr[left]<=k and k < arr[mid]:
                right = mid-1# reduce search to left side
            else:
                left = mid+1# reduce search to right side
        else: #right is sorted
            if arr[mid]< k and k<=arr[right]:
                left = mid+1
            else:
                right = mid-1
    
    return -1
