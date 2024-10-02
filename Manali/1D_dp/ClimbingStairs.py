class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def recur(i):
            if i==0 or i==1:
                dp[i] = 1
                return dp[i]
            if dp[i]!=-1: return dp[i]
            dp[i] = recur(i-1) + recur(i-2)
            return dp[i]
        return recur(n)
    
TC: O(n)
SC: O(n)