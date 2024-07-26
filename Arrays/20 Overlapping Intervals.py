class Solution:
    def overlappedInterval(self, ar):
        ar.sort()
        stack = []
        stack.append(ar[0])
        for i in ar[1:]:
            if stack[-1][1] >= i[0]:
                stack[-1][1] = max(stack[-1][1], i[1])
            else:
                stack.append(i)
        return stack


# Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().strip().split()))
        Intervals = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            Intervals.append([x, y])
        obj = Solution()
        ans = obj.overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()
# Driver Code Ends
