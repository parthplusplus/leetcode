class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        tmap = Counter(t)
        smap = defaultdict(int)
        have = 0
        need = len(tmap)
        res = [-1,-1]
        resLen = float('inf')

        for right in range(len(s)):
            smap[s[right]]+=1
            if s[right] in tmap and smap[s[right]] == tmap[s[right]]:
                have+=1
            
            while have==need:
                #update reslen
                if right-left+1 < resLen:
                    res = [left,right]
                    resLen = right-left+1

                smap[s[left]]-=1
                if s[left] in tmap and smap[s[left]] < tmap[s[left]]:
                    have-=1
                
                left+=1
            
        return s[res[0]:res[1]+1] if resLen!=float('inf') else ""

TC: O(s+t)
SC: O(s+t)
