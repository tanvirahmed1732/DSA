from math import inf
class Solution:
    def maxArea(self, ar: list[int]) -> int: # 2 pointer aproach
        n=len(ar)
        l=0
        r=n-1
        mx=-inf
        while l<r:
            mx=max(mx,min(ar[l],ar[r])*(r-l)) # calculating how much water can be stored by two lines
            if ar[l]<ar[r]: # updating the left and right pointer based on the small line.
                l+=1
            else:
                r-=1
        return mx