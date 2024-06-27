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
    
TC: O(n)
SC: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = collections.defaultdict(int)
        left, maxLength = 0,0
        for right in range(len(s)):
            map[s[right]]+=1
            while map[s[right]]>1:
                map[s[left]]-=1
                if not map[s[left]]: map.pop(s[left])
                left+=1
            maxLength= max(maxLength, right-left+1)
        return maxLength