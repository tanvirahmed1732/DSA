#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #two pointer approach
        a={}
        m=0
        l=0
        for r in range(len(s)):
            if s[r] in a and a[s[r]]>=l: #if there is any duplicate occures
                l=a[s[r]]+1 #simply update the left pointer to exlude the duplicate value for the farther checking
            else:
                m=max(m,r-l+1) #if there is no duplicate calculating the length also updating the max variable.
            a[s[r]]=r #storing the index of the recent char in the string. 
        return m