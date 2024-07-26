import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        r=[0]*n
        l=[1]*n
        r=[1]*n
        for i in range(n-1):
            l[i+1]=l[i]*nums[i]
        for i in range(n-1,0,-1):
            r[i-1]=r[i]*nums[i]
        for i in range(n):
            r[i]=l[i]*r[i]
        return r