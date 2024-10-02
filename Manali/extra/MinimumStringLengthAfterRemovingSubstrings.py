class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack and ((stack[-1]=='A' and s[i]=='B') or (stack[-1]=='C' and s[i]=='D')): stack.pop()
            else: stack.append(s[i])
        return len(stack)
        

TC: O(n)
SC: O(n)