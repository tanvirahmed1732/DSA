#https://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/

ar=[5, 20, 3, 2, 50, 80]
n=78
ar.sort()
i,j=0,1
while(j<len(ar) and i<len(ar)-1):
    if ar[j]-ar[i] == n:
        print(ar[i],ar[j])
        break
    elif ar[j]-ar[i]<n:
        j+=1
    else:
        i+=1
else:
    print(-1)