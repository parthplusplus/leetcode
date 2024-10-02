class Solution:
    def square(self,n):
        sum = 0
        while n > 0:
            rev = n%10
            sum = sum + (rev ** 2)
            n = n//10   
        return sum
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.square(n)
            if n == 1: return True
        return False         
        