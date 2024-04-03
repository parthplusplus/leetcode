class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        d = {}
        maxLength = 0
        for r in range(len(s)):
            if s[r] not in d or d[s[r]]<l:
                maxLength = max(maxLength, r-l+1)
            else:
                l= d[s[r]]+1
            d[s[r]] = r
        return maxLength