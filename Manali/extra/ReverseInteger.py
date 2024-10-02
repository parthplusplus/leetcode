class Solution:
    def reverse(self, x: int) -> int:
        is_neg, rev, sum = 0,0,0
        if x<0: 
            is_neg = 1
            x = abs(x)
        while x>0 :
            rev = x%10
            sum= sum*10+rev
            x = x//10
        if sum<(-2**31) or sum>(2**31-1): return 0
        return sum if not is_neg else -sum
        
TC:O(logx)
SC: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        is_neg, rev, sum = 0, 0, 0
        if x<0: 
            is_neg = 1
            x = abs(x)
        while x>0 :
            if sum > (2**31-1)//10: return 0
            rev = x%10
            sum = sum*10 + rev
            x = x//10
        return -sum if is_neg else sum
