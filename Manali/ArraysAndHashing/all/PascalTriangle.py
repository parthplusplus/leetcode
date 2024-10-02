class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[i] + [0]
            row = []
            for j in range(len(res)+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res

TC: O(n^2)
SC: O(n^2)