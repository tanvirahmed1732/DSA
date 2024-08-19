a=[2,1,3]
b=[7,8,9]
k=10
a.sort(reverse=True)
b.sort()
for i in range(len(a)):
    if a[i]+b[i]<k:
        print("NO")
        break
else:
    print("YES")