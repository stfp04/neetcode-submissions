class Solution:
    def binarySearch(self, nums: List[int], target) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            row = matrix[i]
            if row[0] >= target:
                if row[0] == target:
                    return True
                elif i <= 0:
                    return False
                else:
                    return self.binarySearch(matrix[i-1], target)
        
        if matrix[-1][-1] >= target:
            if matrix[-1][-1] == target:
                return True
            else:
                return self.binarySearch(matrix[-1], target)
        else:
            return False