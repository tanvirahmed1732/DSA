class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums[:]) == nums[::-1]:
            nums.sort()
            return
        ind = 0
        for i in range(len(nums)-1,1,-1):
            if nums[i]>nums[i-1]:
                ind=i-1
                break
        for i in range(len(nums)-1,0,-1):
            if nums[ind]<nums[i]:
                nums[ind],nums[i]=nums[i],nums[ind]
                break
        nums[:]=nums[:ind+1]+sorted(nums[ind+1:])
