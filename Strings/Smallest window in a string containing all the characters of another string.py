#User function Template for python3
import string

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        left,stind,count,mn=0,-1,0,100001
        ns,np=len(s),len(p)
        stri = {char: 0 for char in string.ascii_lowercase} #creating freq dict, initialize zero to all lower case
        pat = {char: 0 for char in string.ascii_lowercase}
        if np>ns: #substring not possible here
            return -1
            
        for i in range(np): #creating the freq dict of pattern array
            pat[p[i]]+=1
            
        for i in range(ns):
            
            stri[s[i]]+=1 #update the freq of the string
            
            if stri[s[i]]<=pat[s[i]]: #if the pattern char is fount to the array
                count+=1
                
            if count == np: #if all the char found in the string
                while stri[s[left]]>pat[s[left]] or pat[s[left]]==0: #updating the left pointer to remove unnessesary char from the string 
                    if stri[s[left]]>pat[s[left]]:
                        stri[s[left]]-=1 #if the char is not in the pat
                    left+=1
                temp=i-left+1
                if temp<mn: #calculating the minimum length and the starting index of the substring
                    mn=temp
                    stind=left #starting index of the substring
        if stind == -1: #if these is no such pattern in the string
            return -1
        return s[stind:stind+mn] #retrun the found substring.
                    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends