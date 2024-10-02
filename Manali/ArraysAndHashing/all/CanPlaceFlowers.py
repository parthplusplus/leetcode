class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                f[i]=1
                n-=1
        return n<=0

TC: O(n)
SC: O(n)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0: return True
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==size-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
                if n==0: return True
        return False
    
TC: O(n)
SC: O(1)