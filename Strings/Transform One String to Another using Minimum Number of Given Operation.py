#https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/
a="EACBD"
b="EABCD"
n=len(a)
if n!=len(b):
    print("Not Possible")
    exit()
temp=0
for i in range(n):
    temp+=ord(a[i])
    temp-=ord(b[i])
if temp!=0:
    print("Not Possible")
    exit()
i,j=n-1,n-1
ans=0
while i>=0:
    while i>=0 and a[i]!=b[j]:
        i-=1
        ans+=1
    i-=1
    j-=1
print(ans)