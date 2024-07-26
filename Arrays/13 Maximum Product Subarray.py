import sys


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        mx = -sys.maxsize - 1
        ml = 1
        for i in range(len(nums)):
            ml *= nums[i]
            if ml > mx:
                mx = ml
            if ml == 0:
                ml = nums[i]
            if nums[i] > mx:
                mx = nums[i]
        ml = 1
        for i in range(len(nums) - 1, 0, -1):
            ml *= nums[i]
            if ml > mx:
                mx = ml
            if ml == 0:
                ml = nums[i]
        return mx
