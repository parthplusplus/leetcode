class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)//2
        for num in nums:
            freq[num]+=1
            if freq[num]>n: return num

TC: O(n)
SC: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        ct = 0
        for num in nums:
            if ct==0:
                candidate = num
            ct += (-1 if num!=candidate else 1)
        return candidate
    
TC: O(n)
SC: O(1)