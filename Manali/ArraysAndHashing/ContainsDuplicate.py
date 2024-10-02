class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for num in nums:
            if num in unique: return True
            unique.add(num)
        return False
    
TC: O(n)
SC: O(n)

#also do by sorting O(nlogn) and space O(1)