class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while r - l > 1:
            mid = l + (r-l)//2

            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] > target:
                r = mid
            else:
                l = mid
        
        if matrix[l // len(matrix[0])][l % len(matrix[0])] == target:
            return True
        if matrix[r // len(matrix[0])][r % len(matrix[0])] == target:
            return True
        return False