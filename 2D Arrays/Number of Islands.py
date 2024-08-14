#https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/
#dfs
graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]
ans=0
def dfs(i,j):
    if i<0 or i>len(graph)-1 or j<0 or j>len(graph[0])-1 or graph[i][j]!=1:
        return
    graph[i][j]=-1
    dfs(i-1,j)
    dfs(i-1,j-1)
    dfs(i-1,j+1)
    dfs(i,j-1)
    dfs(i,j+1)
    dfs(i+1,j-1)
    dfs(i+1,j)
    dfs(i+1,j+1)

    

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j]==1:
            dfs(i,j)
            ans+=1
print(ans)
