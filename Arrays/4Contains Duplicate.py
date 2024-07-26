class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st=set(nums) #since set doesn't contain any duplicate values
        if len(nums)==len(st): #if any duplicate value exist the won't match
            return False
        else:
            return True