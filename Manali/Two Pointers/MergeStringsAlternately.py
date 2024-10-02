class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i=0
        while i<len(word1) and i<len(word2):
            ans.append(word1[i])
            ans.append(word2[i])
            i+=1
        if i<len(word1):
            ans.append(word1[i:])
        if i<len(word2):
            ans.append(word2[i:])
        return "".join(ans)

TC:O(n)
SC:O(n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr = ""
        i=0
        while i<len(word1) and i<len(word2):
            newStr+=word1[i]
            newStr+=word2[i]
            i+=1
        if i<len(word1):
            newStr+=word1[i:]
        if i<len(word2):
            newStr+=word2[i:]
        return newStr
