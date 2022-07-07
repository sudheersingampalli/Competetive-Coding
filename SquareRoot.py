'''
Link :: https://practice.geeksforgeeks.org/problems/square-root/1
'''

class Solution:
    def floorSqrt(self, x): 
        l = 1
        h = x//2
        ans = 1
        while(l<=h):
            mid = l+(h-l)//2
            square = mid*mid
            
            if square > x:
                h=mid-1
            elif square < x:
                ans = mid
                l=mid+1
            else:
                return mid
        return ans
