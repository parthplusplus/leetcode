class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        left = 0
        while left<=len(s2)-n:
            right = left+n
            t2 = s2[left:right]
            if sorted(s1)==sorted(t2): return True
            left+=1
        return False
        


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1>n2: return False
        s1_count = Counter(s1)
        window_ct = Counter()
        for i in range(n2):
            window_ct[s2[i]]+=1
            if i>=n1:
                if window_ct[s2[i-n1]]==1: del window_ct[s2[i-n1]]
                else: window_ct[s2[i-n1]]-=1
            if window_ct==s1_count: return True
        return False
    
TC: O(n2)
SC: O(1)