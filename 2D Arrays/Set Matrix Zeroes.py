#
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #I use first column and first row as a indicator.
        #if we find any zero, then set the [row][0] and [0][col] position to zero
        #then search again and if there any 0 present in the first col and row
        #set entire row and col to zero. we face a problem here. if there is any zero
        #already present in the first col or row we need sed entire column or row to zero.
        #but if I do that first, I can't use the col and row as indicator. so, I do it letter
        col=False
        row=False
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    if i==0:#if first col has any zero
                        row=True
                    if j==0:#if first row has any zero
                        col=True
                    matrix[i][0]=matrix[0][j]=0 #set the corresponding first row and col zero
       
        for i in range(1,r):#to set all element zero if first row or col has any zero
            for j in range(1,c): #skipping first col and row
                if matrix[i][0]==0:
                    matrix[i][j]=0
                if matrix[0][j]==0:
                    matrix[i][j]=0
        if col: #set all to the first col(skipped col) if initially any zero was there
            for i in range(r):
                matrix[i][0]=0
        if row:#same as col
            for i in range(c):
                matrix[0][i]=0
        return matrix
        