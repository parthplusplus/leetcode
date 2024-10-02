class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = sum(nums)
        prev_sum = 0
        for i in range(len(nums)):
            if (res-nums[i])/2 == prev_sum: return i
            prev_sum+=nums[i]
        return -1
    
TC: O(n)
SC: O(1)