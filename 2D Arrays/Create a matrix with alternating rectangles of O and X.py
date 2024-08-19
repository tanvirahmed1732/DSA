#https://www.geeksforgeeks.org/create-a-matrix-with-alternating-rectangles-of-0-and-x/
row=5
col=5
ans = [["T"] * col for i in range(row)] 
l,r,t,b=0,col-1,0,row-1
flag="X"
while l<=r and t<=b:
    for i in range(l,r+1):
        ans[t][i]=flag
    t+=1 
        
    for i in range(t,b+1):
        ans[i][r]=flag
    r-=1 
    
    if t<b:        
        for i in range(r,l-1,-1):
            ans[b][i]=flag
        b-=1
    if l<r:
        for i in range(b,t-1,-1):
            ans[i][l]=flag
        l+=1
    if flag=="X":
        flag="O"
    else:
        flag="X"

for i in range(row):
    print(*ans[i])
print(ans)