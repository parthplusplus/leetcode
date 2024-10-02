class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        elif len(nums) == 1: return 1
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                length = 1
                while num+length in nums: length += 1
                longest = max(longest, length)
        return longest
        

TC: O(n)
SC: O(n)