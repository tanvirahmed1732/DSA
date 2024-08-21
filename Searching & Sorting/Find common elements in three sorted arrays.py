a=[1,5,10,20,30]
b=[5,13,15,20]
c=[5,20]
i,j,k=0,0,0
while(i<len(a) and j<len(b) and k<len(c)):
    if a[i] == b[j] and b[j] == c[k]:
        print(a[i])
        i,j,k=i+1,j+1,k+1
        continue
    temp=max(a[i],b[j],c[k])
    if a[i]<temp:
        i+=1
    if b[j]<temp:
        j+=1
    if c[k]<temp:
        k+=1
