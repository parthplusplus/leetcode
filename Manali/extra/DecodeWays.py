class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        if len(s) == 1: return 1 
        prev_prev = 0
        prev = 1
        for i in range(len(s)):
            current = 0
            if s[i] != '0': current = prev
            if i>0 and (s[i-1]=='1' or (s[i-1]=='2' and int(s[i])<=6)): current += prev_prev
            prev_prev, prev = prev, current
        return prev
    
TC: O(n)
SC: O(1)


#dp solution
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0': return 0
        if n == 1: return 1
        dp = [0]*n
        dp[0] = 1
        for i in range(1,n):
            if s[i]!='0': dp[i] += dp[i-1]
            two_digit = s[i-1:i+1]
            if 10<=int(two_digit)<=26:
                dp[i] += dp[i-2] if i>1 else 1
        return dp[n-1]  

TC : O(n)
SC : O(n)