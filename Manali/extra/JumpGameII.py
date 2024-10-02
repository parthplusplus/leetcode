class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        jump = 1
        local = nums[0]
        maxReach = 0
        for i in range(1,len(nums)):
            if i>local:
                local = maxReach
                jump+=1
            maxReach = max(maxReach,i+nums[i])
        return jump