class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-k+1):
            ans = min(nums[i+k-1]-nums[i], ans)
        return ans

TC: O(nlogn)
SC: O(1)
