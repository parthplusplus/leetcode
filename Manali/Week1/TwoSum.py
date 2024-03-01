class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        dictionary = {}
        for i in range(len(nums)):
            if target-nums[i] in dictionary:
                l.append(i)
                l.append(dictionary[target-nums[i]])
                return l
            else:
                dictionary[nums[i]] = i
        return l