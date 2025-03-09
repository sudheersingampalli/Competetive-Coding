"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Solution:
Calculate LeftArray: Contains product of all eles to the left of an ele
RightArray: Contains product of all eles to the right of an ele
Return LeftArray * RightArray
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1]*l
        right = [1]*l
        
        for i in range(1,l):
            left[i] = left[i-1]*nums[i-1]
        for j in range(l-2, -1, -1):
            right[j] = right[j+1]*nums[j+1]
        
        return [left[k]*right[k] for k in range(l)]
