class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ct = 0
        res = []
        for c in s:
            if c=='(':
                res.append(c)
                ct+=1
            elif c==')' and ct>0:
                res.append(c)
                ct-=1
            elif c!=')':
                res.append(c)
        if ct==0: return ''.join(res)
        i = len(res)-1
        while ct>0:
            if res[i]=='(':
                res.pop(i)
                ct-=1
            i-=1
        return ''.join(res)
    
TC: O(n)
SC: O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list(s)
        stack = []
        for i in range(len(res)):
            if res[i]=='(':
                stack.append(i)
            elif res[i]==')':
                if stack: stack.pop()
                else: res[i]=''
        while stack:
            res[stack.pop()]=''
        return ''.join(res)