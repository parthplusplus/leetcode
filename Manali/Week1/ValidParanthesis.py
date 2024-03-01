class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1: return False
        stack = []
        for c in s:
            if c=='(' or c=='[' or c=='{': stack.append(c)
            elif stack and c==')' and stack[-1]=='(': stack.pop()
            elif stack and c==']' and stack[-1]=='[': stack.pop()
            elif stack and c=='}' and stack[-1]=='{': stack.pop()
            else: return False
        return not stack
        