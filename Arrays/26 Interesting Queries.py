#User function Template for python3
from operator import itemgetter
class Solution:
	def solveQueries(self, arr, q, k):
		#Code here
		#q.sort(key=itemgetter(1))
		
		currL,currR = 0,0
		res=[0]*len(q)
		freq=[0]*1001
		temp=0
     
        # Traverse through all queries
        for i in range(len(q)):
            L,R = q[i] # L and R values of current range
            L,R=L-1,R-1
 
            while currL<L:
                if freq[arr[currL]] == k:
                    temp-=1
                freq[arr[currL]]-=1
                currL+=1
             
            while currL>L:
                if freq[arr[currL-1]] == k-1:
                    temp+=1
                freq[arr[currL-1]]+=1
                currSum+=arr[currL-1]
                currL-=1
                
                
            while currR<=R:
                if freq[arr[currR]] == k-1:
                    temp+=1
                freq[arr[currR]]+=1
                currSum+=arr[currR]
                currR+=1
             
            while currR>R+1:
                if freq[arr[currR-1]] == k:
                    temp-=1
                freq[arr[currR-1]]-=1
                currSum-=arr[currR-1]
                currR-=1
                
            res[i]=temp
        return res
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, q, k = input().split()
		n = int(n); q = int(q); k = int(k);
		nums = list(map(int, input().split()))
		Queries = []
		for _ in range(q):
			Queries.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.solveQueries(nums, Queries, k)
		for _ in ans:
			print(_)

# } Driver Code Ends