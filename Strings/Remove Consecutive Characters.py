#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        b=str()
        b+=s[0] # assigning first element from the string, since we are traversing from 1th position in the loop
        for i in range(1,len(s)): # travesing all element in the string
            if s[i]!=s[i-1]: #checking the condition
                b+=s[i] #assigning to the new variable if the condition match
        return b

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends