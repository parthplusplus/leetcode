#Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1: return 0
        max_profit = 0
        temp = prices[0]
        for i in range(1,len(prices)):
            if prices[i]-temp<0: temp = prices[i]
            else: max_profit = max(max_profit, prices[i]-temp)
        return max_profit