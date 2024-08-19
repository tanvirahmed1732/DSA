#{ 
 # Driver Code Starts

# } Driver Code Ends
#Problem link: https://www.geeksforgeeks.org/problems/permutations-in-array1747/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
class Solution:
    def isPossible(self, k, arr1, arr2):
        #Your code goes here.
        arr1.sort()
        arr2.sort(reverse=True)
        for i in range(len(arr1)):
            if arr1[i]+arr2[i]<k:
                return False
        else:
            return True

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())
    for _ in range(t):
        k = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.isPossible(k, arr1, arr2)
        if ans:
            print("true")
        else:
            print("false")

if __name__ == "__main__":
    main()
# } Driver Code Ends