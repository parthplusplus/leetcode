class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left<right:
            sum = nums[left]+nums[right]
            if sum==target: return [left+1,right+1]
            elif sum<target: left+=1
            else: right-=1
        return []

TC:O(n)
SC:O(1)