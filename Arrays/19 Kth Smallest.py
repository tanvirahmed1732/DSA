#User function Template for python3
from heapq import heappop, heappush, heapify
class Solution:
    def kthSmallest(self,arr, l, r, k):
        heap=[]
        heapify(heap) #creating empty heap
        for i in range(k):
            heappush(heap,-1*arr[i]) #intialize first k value into the heap
        for i in range(k,len(arr)):
            if arr[i]<-1*heap[0]:
                heappop(heap)
                heappush(heap,-1*arr[i])
        return -1*heap[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends