class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row-1
        while top<=bottom:
            mid = (top+bottom)//2
            if matrix[mid][-1] < target: top = mid + 1
            elif matrix[mid][0] > target: bottom = mid - 1
            else: break
        left, right = 0, col-1
        while left<=right:
            midd = (left+right)//2
            if matrix[mid][midd]==target: return True
            elif matrix[mid][midd]<target: left = midd+1
            else: right = midd-1
        return False
        
TC: O(log(m*n))
SC: O(1)