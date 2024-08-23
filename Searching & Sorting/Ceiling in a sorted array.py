#https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

def findceil(ar,l,r,x):
    if x<=ar[l]: #if the x is less then or equal to the first element of the arr, then first element is the ceil
        return ar[l]
    if x>ar[r]: #if x is greater than the elements present in the arr, then there is no ceil present
        return -1
    while(l<=r):
        mid = (l+r)//2 #calculating the mid
        if ar[mid]==x: #if mid is the x then we found the ceil
            return ar[mid]
        elif x<ar[mid]: #if the x is in the left side of the arr, update the r pointer
            r=mid-1
        else:
            l=mid+1 #if the x is in the right side, update the l pointer
    else: #after completing the loop, the l pointer will be the ceil
        return ar[l]





ar=[1, 2, 8, 10, 10, 12, 19]
x=20
l=0
r=len(ar)
ans=findceil(ar,l,r-1,x)
print(ans)