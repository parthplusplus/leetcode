class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == "(" or c == "{" or c == "["):
                stack.append(c)
            elif (c == ")"):
                if (len(stack) == 0 or stack[-1] != "("):
                    return False
                stack.pop()
            elif (c == "]"):
                if (len(stack) == 0 or stack[-1] != "["):
                    return False
                stack.pop()
            elif (c == "}"):
                if (len(stack) == 0 or stack[-1] != "{"):
                    return False
                stack.pop()
        if(len(stack) > 0):
            return False
        return True
            
        