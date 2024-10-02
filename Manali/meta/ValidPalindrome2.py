class Solution:
    def isPalindrome(self,left,right, s):
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return self.isPalindrome(left+1,right, s) or self.isPalindrome(left, right-1, s)
        return True
        
TC: O(n)
SC: O(1)