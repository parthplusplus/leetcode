class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = collections.defaultdict(int)
        left,totalFruits,maxFruits = 0,0,0
        for right in range(len(fruits)):
            map[fruits[right]]+=1
            totalFruits+=1
            while len(map)>2:
                map[fruits[left]]-=1
                if not map[fruits[left]]: map.pop(fruits[left])
                left+=1
                totalFruits-=1
            maxFruits = max(maxFruits, totalFruits)
        return maxFruits
        
TC: O(n)
SC: O(1)