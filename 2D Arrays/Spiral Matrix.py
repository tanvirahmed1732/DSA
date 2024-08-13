class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans=[]
        row=len(matrix)
        col=len(matrix[0])
        l,r,t,b=0,col-1,0,row-1 #set 4 boundaries in 4 corner.(4 pointer)
        while(len(ans)<row*col): #if we find all elements
            for i in range(l,r+1):#travers left to right
                ans.append(matrix[t][i])#append only top pointer row
            t+=1 #update the top pointer after appending the top row
            
            for i in range(t,b+1): #travers top to bottom
                ans.append(matrix[i][r])#appending the right pointer column
            r-=1 #update right pointer

            if len(ans)==row*col: #if all ans found already no need to check farther
                return ans
                
            for i in range(r,l-1,-1):#travers r to left
                ans.append(matrix[b][i])#append bottom pointer row
            b-=1#update bottom pointer

            for i in range(b,t-1,-1):#travers bottom to top
                ans.append(matrix[i][l])#append left pointer column
            l+=1#update left ponter.
        return ans