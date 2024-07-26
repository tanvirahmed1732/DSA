arr = [3, 4, 1, 9, 56, 7, 9, 12]
m=5
arr.sort()
t= arr[m-1]-arr[0]
for i in range(len(arr)-m+1):
    if arr[i+m-1]-arr[i]<t:
        t=arr[i+m-1]-arr[i]
print(t)