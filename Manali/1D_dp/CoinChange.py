class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        def recur(i):
            if i==0: 
                dp[i] = 0
                return dp[i]
            if dp[i]!=-1: return dp[i]
            temp = float('inf')
            for coin in coins:
                if i-coin>=0: temp = min(temp, recur(i-coin)+1)
            dp[i] = temp
            return dp[i]
        res = recur(amount)
        return res if res!=float('inf') else -1

#a=amount   
TC: O(n*a)
SC: O(a)