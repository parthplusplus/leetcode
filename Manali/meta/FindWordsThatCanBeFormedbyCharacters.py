class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        ans = 0
        for word in words:
            wfreq = Counter(word)
            good = True
            for c in word:
                if wfreq[c] > freq[c]:
                    good = False
                    break
            if good: ans+=len(word)
        return ans
    
TC: O(n * m)
SC: O(m + k)


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            freq = Counter(chars)
            ct = 0
            for c in word:
                if c in freq and freq[c]>0:
                    freq[c]-=1
                    ct+=1
            if ct==len(word): ans+=ct
        return ans
    
TC: O(n * m)
SC: O(m)