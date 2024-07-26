class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=-sys.maxsize-1
        sm=0
        for i in range(len(nums)):
            sm+=nums[i]
            if sm>mx:
                mx=sm
            if sm<0:
                sm=0
        return mx