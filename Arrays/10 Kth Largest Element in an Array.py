import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=[]
        heapify(heap) #creating empty minheap
        for i in range(k):
            heappush(heap,nums[i]) #initializing first k elements into the heap
        for i in range(k,len(nums)):
            if nums[i]>heap[0]:
                heappop(heap) #removing the lowest element from the heap
                heappush(heap,nums[i]) #adding the new largest one
        return heap[0] #this is the kth largest element since this is the k sized minheap.