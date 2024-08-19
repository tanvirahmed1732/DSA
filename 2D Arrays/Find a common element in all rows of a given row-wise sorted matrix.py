#https://www.geeksforgeeks.org/find-common-element-rows-row-wise-sorted-matrix/
mat = [[1, 2, 3, 4, 5 ], 
        [2, 4, 5, 8, 10], 
        [3, 5, 7, 9, 11], 
        [1, 3, 5, 7, 9 ]] 
row=len(mat)
col=len(mat[0])
i,j=0,0
dic={}

while i<row:
    if mat[i][0] not in dic:
        dic[mat[i][0]]=1
    else:
        dic[mat[i][0]]+=1
    j=1
    while j<col:
        if mat[i][j] != mat[i][j-1]:
            if mat[i][j] not in dic:
                dic[mat[i][j]]=1
            else:
                dic[mat[i][j]]+=1
        j+=1
    i+=1
flag=False
for i in dic:
    if dic[i]==row:
        print(i)
        flag=True
if not flag:
    print(-1)