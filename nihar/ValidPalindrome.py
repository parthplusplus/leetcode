class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.lower()
        while ( i < j):
            while (i < len(s) and not s[i].isalnum()):
                i += 1
            while (j > 0 and not s[j].isalnum()):
                j -= 1
            if (i < j and i < len(s) and j>0 and s[i] != s[j]):
                return False
            else:
                i += 1
                j -= 1
        return True