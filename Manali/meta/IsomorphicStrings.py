class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        smap = defaultdict(str)
        tmap = defaultdict(str)
        for i in range(len(s)):
            if ((s[i] in smap and smap[s[i]]!=t[i]) or (t[i] in tmap and tmap[t[i]]!=s[i])): return False
            smap[s[i]] = t[i]
            tmap[t[i]] = s[i]
        return True
        
TC: O(n)
SC: O(1)
# Where k is the size of the character set
# In the worst case, we might have to store mappings for every unique character
# For ASCII strings, this would be O(256), which simplifies to O(1)