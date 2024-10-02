#Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        l, res = 0, 0
        for r in range(1,len(prices)):
            if prices[r]-prices[l] < 0: l=r
            else: res = max(res, prices[r]-prices[l])
        return res
    
TC: O(n)
SC: O(1)