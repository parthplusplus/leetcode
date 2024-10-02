class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, ans = 0,0
        right = len(height) - 1
        while left<right:
            area = (right-left) * min(height[right], height[left])
            ans = max(ans,area)
            if height[left] < height[right]: left+=1
            else: right-=1
        return ans
        
TC: O(n)
SC: O(1)