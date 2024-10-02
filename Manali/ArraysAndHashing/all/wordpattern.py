class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ps = defaultdict(str)
        sp = defaultdict(str)
        res = s.split(' ')
        if len(pattern)!=len(res): return False
        for i in range(len(pattern)):
            if (pattern[i] in ps and ps[pattern[i]] != res[i]) or (res[i] in sp and sp[res[i]] != pattern[i]): return False
            ps[pattern[i]] = res[i]
            sp[res[i]] = pattern[i]
        return True
    
TC: O(n)
SC: O(n)