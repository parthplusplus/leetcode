class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str in strs:
            temp = ''.join(sorted(str))
            ans[temp].append(str)
        return ans.values()
    
TC : O(n*klogk)
SC : O(n*k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str in strs:
            count = [0]*26
            for c in str: count[ord(c)-ord('a')]+=1
            ans[tuple(count)].append(str)
        return ans.values()
    
TC : O(n*k)
SC : O(n*k)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            sorted_word = ''.join(sorted(str))
            res[sorted_word].append(str)
        return list(res.values())