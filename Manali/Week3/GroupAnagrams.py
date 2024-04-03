class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            sorted_word = ''.join(sorted(str))
            res[sorted_word].append(str)
        return list(res.values())
    