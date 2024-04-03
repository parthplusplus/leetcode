class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        found = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            d = set()
            for j in range(i+1,len(nums)):
                if target-nums[j] in d:
                    l = [nums[i], nums[j], target-nums[j]]
                    if tuple(l) not in found:
                        ans.append(l)
                        found.add(tuple(l))
                else:
                    d.add(nums[j])
        return ans