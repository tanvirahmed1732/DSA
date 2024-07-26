#https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(': ')','{': '}','[': ']'} #to match the pairs
        stack=[]
        for i in s:
            if i in check.keys(): 
                stack.append(i) #appending the opening brackets
            elif i in check.values(): #if it is the closing bracket.
                if len(stack)==0:
                    return False
                a=stack.pop() #pop the opening bracket to match to the closing bracket
                if check[a] != i: #if poped bracket's matching bracket is not equal to the i(current bracket, that means closing bracket)
                    return False
        if len(stack) == 0: # checking: after the loop, if there is still any element left in the stack
            return True
        else:
            return False