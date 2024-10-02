class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]]+=1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            else: res = max(res,r-l+1)
        return res
    
TC: O(n)
SC: O(1)