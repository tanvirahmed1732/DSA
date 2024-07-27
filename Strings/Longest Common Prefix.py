class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lst=sorted(strs) # sorting to reduce the time complexity
        # since we are searching  the similar prefix, if we sort here
        # and check the first and last string in the sorted array
        # then we will get the common prefix in minimum of timne
        # cause the first and last element would be the most 
        # different from each other.
        f=lst[0]
        l=lst[-1]
        n=min(len(f),len(l))
        ret=str()
        for i in range(n):
            if f[i]!=l[i]: # checking only in the first and last element of the list
                break
            else:
                ret+=f[i]
        return ret