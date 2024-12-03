class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        best_sum = 0
        curr_sum = 0
        for change in changes:
            curr_sum = max(curr_sum + change, 0)
            best_sum = max(best_sum, curr_sum)
        return best_sum