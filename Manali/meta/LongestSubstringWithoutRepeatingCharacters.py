class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res
    
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