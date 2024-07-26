lst=list(map(int,input().split()))
x=int(input())
n=len(lst)
i=0
while i<n:
    if lst[i]>lst[i+1]:
        break
    i+=1
mx=i
mn=(i+1)%n
for i in range(n):
    if lst[mx]+lst[mn] == x:
        print("True")
        break
    elif lst[mx]+lst[mn]>x:
        mx=(n+mx-1)%n
    elif lst[mx]+lst[mn]<x:
        mn=(n+mn+1)%n
else:
    print("False")