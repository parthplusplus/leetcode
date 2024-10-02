class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        ans = [-1]
        n = len(nums)
        if n==1: return ans
        max = -1
        for i in range(n-1,0,-1):
            if nums[i]>max: max = nums[i]
            ans.append(max)
        ans.reverse()
        return ans
    
TC: O(n)
SC: O(n)

class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        rightMax = -1
        n = len(nums)
        for i in range(n-1,-1,-1): nums[i], rightMax = rightMax, max(rightMax,nums[i])
        return nums
    
TC: O(n)
SC: O(1)

class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(nums)-1,-1,-1):
            new_max = max_right
            max_right = max(nums[i], max_right)
            nums[i] = new_max
        return nums
