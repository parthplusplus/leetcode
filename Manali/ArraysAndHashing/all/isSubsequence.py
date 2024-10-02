class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if not s: return True
        for c in t:
            if i<len(s) and s[i]==c:i+=1
        return i==len(s)
    
TC: O(n)
Sc: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        if n==0 : return True
        for c in t:
            if s[i]==c:i+=1
            if i==n: return True
        return False
    
TC: O(t)
Sc: O(1)