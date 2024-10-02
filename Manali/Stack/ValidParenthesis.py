class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[': st.append(s[i])
            elif st and st[-1] == '(' and s[i] == ')': st.pop()
            elif st and st[-1] == '{' and s[i] == '}': st.pop()
            elif st and st[-1] == '[' and s[i] == ']': st.pop()
            else: return False
        return True if not st else False
    
TC: O(n)
SC: O(n)

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