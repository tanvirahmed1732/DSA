# User function Template for python3
class Solution:
    def longSubarrWthSumDivByK(self, arr, n, k):
        # Complete the function
        c = {} #Declaring dictionary, using dictionary instead of arry is more efficient here. It will reduce time complexity
        mx = 0
        rem = [0] * n #Declaring the list to store the rem
        sm = 0
        for i in range(n):
            sm += arr[i]
            rem[i] = ((sm % k) + k) % k #double mod to handle negative values
            if rem[i] == 0: # if the consecutinve sum is divisible by k then it is the longest sub array
                mx = i + 1
            elif rem[i] not in c: # if the rem is unique assing it into the dictionary, where key is rem and value is i(the position)
                c[rem[i]] = i
            elif rem[i] in c: #if the rem is matched, then from that matched rem value to the current value, it is another subarry that is divisible by k
                mx = max(mx, i - c[rem[i]]) # checking, new subarray is greater than the old mx value.
        return mx

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n, K = map(int, input().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.longSubarrWthSumDivByK(arr, n, K)
        print(res)
# Driver Code Ends
