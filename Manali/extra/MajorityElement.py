#BoyerMooreMajorityVoteAlgorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # map = {}
        # res = 0
        # ct = 0
        # for i in range(len(nums)):
        #     map[nums[i]] = 1+map.get(nums[i],0)
        #     if map[nums[i]]>ct: res = nums[i]
        #     ct = max(map[nums[i]],ct)
        # return res
        ct = 1
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==res: ct+=1
            else:
                ct-=1
                if ct==0:
                    res=nums[i]
                    ct+=1
        return res
