class Solution:
    def maxProfit(self, ar: list[int]) -> int:
        n=len(ar)
        mx=0
        b=ar[0]
        for i in range(1,n):
            if b>ar[i]:
                b=ar[i]
            if ar[i]-b>mx:
                mx=ar[i]-b

        return mx