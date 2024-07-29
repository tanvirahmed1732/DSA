#https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans={} #dictionary
        for i in strs:
            s=''.join(sorted(i)) #sorted string of the string from the list
            if s in ans:
                ans[s].append(i) #if match found then append to the sorted position
            else:
                ans[s]=[i] #creating new list in the position of the sorted string
                            #so, all the string that match will be inseted in this position together
        return ans.values()