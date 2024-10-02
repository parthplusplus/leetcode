class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1

TC: O(n)
SC: O(1)

#Stack approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in range(len(s)): stack.append(s[i])
        j = 0
        while stack: 
            s[j] = stack.pop()
            j+=1

TC: O(n)
SC: O(n)

#recursion approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l,r):
            if l<r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0,len(s)-1)

TC: O(n)
SC: O(n)
