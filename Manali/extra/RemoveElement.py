class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[ct] = nums[i]
                ct+=1
        return ct