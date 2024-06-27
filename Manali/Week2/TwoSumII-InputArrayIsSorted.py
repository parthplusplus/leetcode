class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = defaultdict(int)
        for i in range(len(numbers)):
            if target-numbers[i] in res:
                    l = []
                    l.append(res[target-numbers[i]]+1)
                    l.append(i+1)
                    return l
            if numbers[i] not in res:
                res[numbers[i]] = i
        return []        