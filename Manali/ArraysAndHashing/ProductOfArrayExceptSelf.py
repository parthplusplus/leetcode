class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = 1
        for num in nums:
            ans.append(left)
            left*=num
        right = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
        return ans
    
# TC: O(n)
# SC: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(len(nums)):
            ans.append(ans[i]*nums[i])

        res = [1] * (len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i+1]*nums[i]   

        out = [0]*len(nums)
        for i in range(0,len(out)):
            out[i] = ans[i]*res[i+1]
        return out


# TC: O(n)
# SC: O(n)
        
