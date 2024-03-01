class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: return 0 if nums[0]==target else -1
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = int((start+end)/2)
            if nums[mid]==target: return mid
            elif nums[mid]<target: start+=1
            else: end-=1
        return -1
        