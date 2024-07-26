class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out=set()
        n,p,z=[],[],[]
        for i in nums: #separating the positive negative and zeros
            if i<0:
                n.append(i)
            if i>0:
                p.append(i)
            if i==0:
                z.append(i)
        P,N=set(p),set(n) #set of positive and negative,,,set doesn't contain duplicates
        
        if len(z)>0: #if there is atleast 1 zero in the nums
            for i in P:
                if -1*i in N: #finding the mirror in the both negative and positive array
                    out.add((-1*i,0,i)) # for example if -1 and 1 exist then output will be -1,0,1
        if len(z)>=3:
            out.add((0,0,0)) #if there is 3 or more zeros available
        
        for i in range(len(n)): # to find the pair of negative that is equivalen to the positive
            for j in range(i+1,len(n)): # for example, for -1,-1 if there is any 2 exist then it will add to the output
                temp=n[i]+n[j]
                if -1*temp in P:
                    out.add(tuple(sorted([n[i],n[j],-1*temp])))
        
        for i in range(len(p)): # same for the positive also
            for j in range(i+1,len(p)):
                temp=p[i]+p[j]
                if -1*temp in N:
                    out.add(tuple(sorted([p[i],p[j],-1*temp])))
        return out