class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for value in freq.values():
            ans += (value*(value-1))//2
        return ans
    
TC: O(n)
SC: O(n)