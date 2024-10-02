class Solution:
    def largestGoodInteger(self, num: str) -> str:
        large = ""
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]: large = max(large, num[i:i+3])
        return large
        
TC: O(n)
SC: O(1)