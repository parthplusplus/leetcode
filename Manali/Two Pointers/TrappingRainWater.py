class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        left[0] = height[0]
        right[n-1] = height[n-1]
        res = 0
        for i in range(1,n):
            left[i] = (max(left[i-1],height[i]))
        for i in range(n-2,-1,-1):
            right[i] = (max(right[i+1],height[i]))
        for i in range(n):
            res += min(left[i],right[i])-height[i]
        return res
        
TC: O(n)
SC: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        l ,res = 0,0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        while l<r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

TC: O(n)
SC: O(1)