class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"(" : ")",  "{" : "}", "[" : "]"}
        stack = [] #F
        for i in s:
            if i in bracket.keys():
                stack.append(i)

            elif not stack or bracket[stack.pop()] != i:
                return False
        return stack == []