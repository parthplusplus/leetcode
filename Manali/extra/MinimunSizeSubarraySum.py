class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, currSize, sum = 0,0,0
        minSize = float('inf')
        for right in range(len(nums)):
            sum+=nums[right]
            currSize+=1
            while sum>=target:
                minSize = min(minSize,currSize)
                sum-=nums[left]
                left+=1
                currSize-=1
            
        return minSize if minSize != float('inf') else 0
    
TC: O(n)
SC: O(1)