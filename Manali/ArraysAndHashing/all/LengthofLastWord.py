class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = s.strip().split(" ")
        return len(str[-1])
    
TC: O(n)
SC: O(n)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                return length
        return length
    
TC: O(n)
SC: O(1)