class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = Counter(text)
        b = Counter('balloon')
        ct = float('inf')
        for key, value in b.items():
            ct= min(word[key]//value, ct)
        return ct
    
TC: O(n)
SC: O(1)
#text contains only lower case letters so counter can be max 26