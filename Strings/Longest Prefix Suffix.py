<<<<<<< HEAD
=======

>>>>>>> 8668aa29cf057a5b85d6a1c6c49b3db05f5e94ed
#https://www.geeksforgeeks.org/problems/longest-prefix-suffix2527/1
#User function Template for python3

class Solution:
<<<<<<< HEAD
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
=======
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
>>>>>>> 8668aa29cf057a5b85d6a1c6c49b3db05f5e94ed


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
<<<<<<< HEAD
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends
=======
    T=int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends
>>>>>>> 8668aa29cf057a5b85d6a1c6c49b3db05f5e94ed
