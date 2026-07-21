class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            print(stack)
            if s[i] in "({[":
                stack.append(s[i])
            if s[i] == ")":
                if(len(stack) == 0):
                    return False
                if stack.pop() != "(":
                    return False
            if s[i] == "}":
                if(len(stack) == 0):
                    return False 
                if stack.pop() != "{":
                    return False
            if s[i] == "]":
                if(len(stack) == 0):
                    return False
                if stack.pop() != "[":
                    return False
        if len(stack) != 0:
            return False
        return True
            
        