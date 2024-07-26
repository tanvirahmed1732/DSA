class Solution:
    def trap(self, ar: list[int]) -> int:
        w=0
        i=0
        j=len(ar)-1
        ib=ar[i]
        jb=ar[j]
        while i<j:
            if ib<=jb:
                w+=ib-ar[i]
                i+=1
                ib=max(ib,ar[i])
            else:
                w+=jb-ar[j]
                j-=1
                jb=max(jb,ar[j])
        return w
        