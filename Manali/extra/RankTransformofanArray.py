class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = arr.copy()
        temp.sort()
        index = {}
        j = 1
        for i in range(len(temp)):
            if temp[i] not in index:
                index[temp[i]] = j
                j+=1
        ans = []
        for i in range(len(arr)):
            ans.append(index[arr[i]])
        return ans
    
TC: O(nlogn)
SC: O(nlogn)