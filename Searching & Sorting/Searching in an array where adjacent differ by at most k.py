#https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/
ar=[20,40,50,70,70,60]
k=20
x=60
i=0
while i<len(ar):
    if ar[i]==x:
        print(i)
        break
    diff=x-ar[i]
    if diff//k < 1:
        i+=1
    else:
        i+=diff//k
else:
    print(-1)