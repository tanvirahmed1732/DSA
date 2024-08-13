#https://leetcode.com/problems/word-search/
#dfs
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i,j,k):
            if k==len(word):#if all char of word found without any problem.
                return True
            if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!=word[k]:
                return False #if index out of bound or the char not match
            temp=board[i][j]
            board[i][j]=''#if match then mark it as found. I am using '', then it will never match again
            if dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1):
                return True #traverse left right up and bottom to find next char. if found return true
            board[i][j]=temp #if not found then remove the mark as found and return false to farthur check
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): #start searching from here. if all char found then it will return true
                    return True
        return False