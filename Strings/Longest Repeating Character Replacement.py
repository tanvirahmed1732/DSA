#https://leetcode.com/problems/longest-repeating-character-replacement/description/
#two pointer approach
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        freq={}
        l=0
        for r in range(len(s)):
            if s[r] in freq: #collecting frequency of the char from the string until r position
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            lent=r-l+1 #distance between two pointer
            if lent-max(freq.values())<=k: #checking how many different char available in the lent.
                ans=max(ans,lent) # that means, if the other char is less than k from the max freq char then update the ans
            else:
                freq[s[l]]-=1 #else move the left pointer and update the freq dictionary.
                l+=1
        return ans