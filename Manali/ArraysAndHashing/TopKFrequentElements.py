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

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums): return nums
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key = freq.get)

TC: O(n log k)
SC: O(n + k)
