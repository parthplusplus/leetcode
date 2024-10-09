class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = [[]for _ in range(max(freq.values())+1)]
        print(res)
        for key, value in freq.items():
            res[value].append(key)
        ans=[]
        for i in range(len(res)-1,-1,-1):
            for j in range(len(res[i])):
                ans.append(res[i][j])
                k-=1
                if k==0: return ans

TC: O(n)
SC: O(n)
