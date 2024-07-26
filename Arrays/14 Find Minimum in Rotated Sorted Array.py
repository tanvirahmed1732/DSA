class Solution:
    def findMin(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2 #calculating mid
            if nums[m]<nums[r]:
                r=m #reseting the right value since there is no smallest value after mid.
            else:
                l=m+1 #reseting the left value since there is no smallers value in the left side
        return nums[l]