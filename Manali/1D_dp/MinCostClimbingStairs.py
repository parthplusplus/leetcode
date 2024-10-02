class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        cost.append(0)
        def recur(i):
            if i==0 or i==1:
                dp[i] = cost[i]
                return dp[i]
            if dp[i]!=-1: return dp[i]
            dp[i] = min(recur(i-1)+cost[i],recur(i-2)+cost[i])
            return dp[i]
        return recur(n)
    
TC : O(n)
SC : O(n)