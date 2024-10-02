class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        ans = []
        for i in range(len(nums)):
            if nums[i]!=i+1: ans.append(i+1)
        return ans
    

TC: O(n)
SC: O(1)
#Although there are nested loops, each number will be placed in its correct position at most once.