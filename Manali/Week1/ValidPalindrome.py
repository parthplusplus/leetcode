class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1: return True
        start = 0
        end = len(s)-1
        while start<end :
            if (not s[start].isalpha()) and (not s[start].isdigit()):
                start+=1
                continue
            if (not s[end].isalpha()) and (not s[end].isdigit()):
                end-=1
                continue
            if s[start].lower()==s[end].lower():
                start+=1
                end-=1
            else: return False
        return True
        