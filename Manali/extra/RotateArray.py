class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = nums[:]  # Copy nums to res
        for i in range(n):
            nums[(i + k) % n] = res[i]
        return nums
    
#Method2 O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k==n or k==0 or n==1: return nums
        k = k%n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        return nums
    def reverse(self,nums,l,r):
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
