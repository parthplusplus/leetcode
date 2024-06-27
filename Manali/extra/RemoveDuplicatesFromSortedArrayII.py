class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        temp = 0
        ct = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[temp]:
                ct=1
                temp+=1
                nums[temp] = nums[i]
            else:
                if(ct<2):
                    ct+=1
                    temp+=1
                    nums[temp] = nums[i]
        return temp+1