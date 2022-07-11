'''
link : https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array0959/1

If a sorted array is rotated, then if we choose any element from the array, either side of the element will be sorted and other side will be unsorted.
So, go to the sorted side and check if K could be there, if yes, reduce search space to left.. else right
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
