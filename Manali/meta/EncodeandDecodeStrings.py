class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i=0
        while i < len(s):
            temp = ""
            while s[i]!='#':
                temp+=s[i]
                i+=1
            temp = int(temp)
            ans.append(s[i+1:i+temp+1])
            i+=temp+1
        print(ans)
        return ans


TC: O(n)
SC: O(n)

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "π".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("π")

TC: O(n)
SC: O(k)

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
