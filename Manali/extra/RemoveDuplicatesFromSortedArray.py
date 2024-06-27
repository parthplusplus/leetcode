class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ct = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[ct]= nums[i]
                ct+=1
        return ct