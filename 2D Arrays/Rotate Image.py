class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #the apraoch is, first, reverse the matrix(up to bottom revers)
        #then transpose it (all column becomes row)
        up=0
        bottom=len(matrix)-1
        while up<bottom:
            matrix[up],matrix[bottom]=matrix[bottom],matrix[up] #swapping the up and bottom rows
            up+=1
            bottom-=1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]#transposing