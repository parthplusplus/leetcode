class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        return str1 == str2
    
TC: O(nlogn)
SC: O(1)
        
#II Approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        ct = defaultdict(int)
        for i in s:
            ct[i]+=1
        for i in t:
            ct[i]-=1
        for val in ct.values():
            if val!=0: return False
        return True
    
TC: O(n)
SC: O(1)
