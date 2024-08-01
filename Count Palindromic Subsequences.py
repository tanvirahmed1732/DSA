class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,s):
        # Code here
        n=len(s)
        l=0
        r=n-1
        dp = [[-1] * n for _ in range(n)]
        def count(i,j):
            if i>j:
                return 0
            if i == j:
                return 1
            if dp[i][j]!=-1:#that means we already calculate this, no need to farther calculation.
                return dp[i][j]
            elif s[i]==s[j]:#then we check excluding i first and then excluding j.(+1 for the matching)
                dp[i][j]=(count(i+1,j)+count(i,j-1)+1)%(10**9 + 7)
                return dp[i][j]
            else: #-count for the twice count.
                dp[i][j]=(count(i+1,j)+count(i,j-1)-count(i+1,j-1))%(10**9 + 7)
                return dp[i][j]
        return count(l,r)

#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends