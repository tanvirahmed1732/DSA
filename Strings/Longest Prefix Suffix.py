#User function Template for python3

class Solution:
	def lps(self, s):
		# code here
		n=len(s)
		i=1
		j=0
		ans=[0]*n
		while i<n:
			if s[i]==s[j]: #if match move bothe the pointer to check next char is equal or not
				j+=1
				ans[i]=j #store the lenght of the matching for the farther use
				i+=1
			else:
				if j==0: #if no match and the j pointer is in the first check. simply match with the next i index
					i+=1
				else:
					j=ans[j-1]#if j is not the first check. then update the j value for the farther checking.
		return ans[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends