#https://leetcode.com/problems/palindromic-substrings/
#peice of cake, using string slicing.
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            for j in range(i+1,n+1):
                ss=s[i:j]
                if ss==ss[::-1]: #if the substring match to its reverse version
                    ans+=1
        return ans