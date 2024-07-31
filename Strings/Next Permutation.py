#https://www.geeksforgeeks.org/problems/next-permutation5226/1
#I have already solved this problem before.
#link: https://github.com/tanvirahmed1732/DSA/blob/main/Arrays/7%20Next%20Permutation.py
#User function Template for python3

class Solution:
    def nextPermutation(self, n, arr):
        # code here
        if sorted(arr)==arr[::-1]:#if there is no farther arrangement possible.
            return sorted(arr)
        ind=0
        for i in range(n-1,1,-1): #finding the number that is greater thean its previous number. in the search of reverse order.
            if arr[i]>arr[i-1]:
                ind=i-1
                break
        for i in range(n-1,ind,-1): #finding the number that is greater than the ind, we will swap this number to the ind number.
            if arr[ind]<arr[i]:
                arr[ind],arr[i]=arr[i],arr[ind]
                break
        arr=arr[:ind+1]+sorted(arr[ind+1:]) #after swapping, sorting the remaining elements after the ind.
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends