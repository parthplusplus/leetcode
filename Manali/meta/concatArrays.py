class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        
TC: O(n)
SC: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
           
TC: O(n)
SC: O(1)


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums: ans.append(num)
        return ans
        
TC: O(n)
SC: O(n)
