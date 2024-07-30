#https://leetcode.com/problems/longest-palindromic-substring/
#simple O(n^2) aproach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx=0
        ans=''
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                ss=s[i:j]
                if ss==ss[::-1]: #if the substring match to the reverse of it.
                    if mx<j-i: # and if it is the max substring
                        mx=j-i #update max and update the ans
                        ans=s[i:j]
        return ans