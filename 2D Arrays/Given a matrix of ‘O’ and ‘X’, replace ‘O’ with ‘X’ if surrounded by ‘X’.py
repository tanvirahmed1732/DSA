#https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/

mat = [ [ 'X', 'O', 'X', 'X', 'X', 'X' ], 
        [ 'X', 'O', 'X', 'X', 'O', 'X' ], 
        [ 'X', 'X', 'X', 'O', 'O', 'X' ], 
        [ 'O', 'X', 'X', 'X', 'X', 'X' ], 
        [ 'X', 'X', 'X', 'O', 'X', 'O' ], 
        [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]

row=len(mat)
col=len(mat[0])

def func(i,j): #dfs function
    if i<0 or i>row-1 or j<0 or j>col-1 or mat[i][j]!="T":
        return
    mat[i][j]="O" #mark as visited then search for right left up and bottom
    func(i,j-1)
    func(i,j+1)
    func(i-1,j)
    func(i+1,j)


for i in range(row): #change all O's to T's to replace all T's with O's that is connected to the edge.
    for j in range(col):
        if mat[i][j]=="O":
            mat[i][j]="T"

for i in range(col):#start dfs for the first row
    if mat[0][i]=="T":
        func(0,i)
for i in range(col): #for the last row
    if mat[row-1][i]=="T":
        func(row-1,i)
for i in range(row): #for the first column
    if mat[i][0]=="T":
        func(i,0)
for i in range(row): #for the last column
    if mat[i][col-1]=="T":
        func(i,col-1)
#now I have T's in only those position where all T's is isolated from the edge.
for i in range(row): #replace those isoleted T's to X's then we are done here.
    for j in range(col):
        if mat[i][j]=="T":
            mat[i][j]="X"

for i in range(row): #print the ans
    print(*mat[i])