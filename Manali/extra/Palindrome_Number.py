class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        temp = x
        rev, sum = 0, 0
        while temp > 0:
            rev = temp%10
            sum = sum*10 + rev
            temp = temp//10
        return True if sum == x else False
        