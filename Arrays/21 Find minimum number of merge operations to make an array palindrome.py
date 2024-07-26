# 2 pointer aproach
arr = [11,14,15,99]
n=len(arr)
l=0
r=n-1
c=0
while l<r:
    if arr[l]==arr[r]: # if right most and left most value is same no need to merger simply update the pointers
        l+=1
        r-=1
    elif arr[l]<arr[r]: # if left is small, we need to merge in left to make the left is same as right
        l+=1
        arr[l]=arr[l-1]+arr[l] # summing and storing in the l position for the future checking
        c+=1 # after summing two adjecent, update the count value by 1. since we are merging 1 time
    elif arr[r]>arr[l]: # same here!!!
        r-=1
        arr[r]=arr[r+1]+arr[r]
        c+=1
print(c)