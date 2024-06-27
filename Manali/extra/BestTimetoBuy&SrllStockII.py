class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1: return 0
        temp = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]-temp > 0: profit += (prices[i]-temp)
            temp = prices[i]
        return profit
        