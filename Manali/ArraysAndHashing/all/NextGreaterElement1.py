class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = defaultdict(int)
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i]>stack[-1]: stack.pop()
            if stack: nums[nums2[i]] = stack[-1]
            else: nums[nums2[i]] = -1
            stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(nums[num])
        return ans

TC: O(n+m)
SC: O(n)
#n-length of num2 ans m-length of num1

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            i=0
            while i<len(nums2) and nums2[i]!=num: i+=1
            while i<len(nums2) and nums2[i]<=num: i+=1
            ans.append(nums2[i] if i<len(nums2) else -1)
        return ans
            
TC: O(n*m)
SC: O(1)