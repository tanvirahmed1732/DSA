#User function Template for python3

class Solution:
    def match(self, wild, pattern):
        # code here
        w=len(wild)
        p=len(pattern)
        i,j,ans,k=0,0,-1,0 #index i for pattern j for wild
        while i<p:
            if j<w and (wild[j]=="?" or pattern[i]==wild[j]):#if it is single char change or mathc just continue
                i+=1
                j+=1
            elif j<w and wild[j]=="*":#mark the index for the future tracking
                ans=j
                k=i
                j+=1
            elif ans != -1: #update the pattern and k index until next match
                j=ans+1
                k+=1
                i=k
            else: #if there is no match, return
                return False
        while j<w and wild[j]=="*": #check remaining * in the wild
            j+=1
        if j==w: #if all tracking complete without any problem, then the strings can be same
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends