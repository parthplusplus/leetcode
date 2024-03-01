class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1: return 0
        maximum = 0
        i = 0
        j = 1
        while j<len(prices) :
            if prices[j]-prices[i]<0:
                i=j
                j+=1
            else:
                maximum = max(maximum,prices[j]-prices[i])
                j+=1
        return maximum