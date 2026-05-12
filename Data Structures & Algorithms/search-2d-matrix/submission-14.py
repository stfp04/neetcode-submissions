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
        bottom, top = 0, (len(matrix) - 1)

        while bottom < top:
            middle = (bottom + top) // 2
            number = matrix[middle][0]

            if number < target:
                bottom = middle + 1
            elif number > target:
                top = middle - 1
            else:
                return True
        
        if bottom == top:
            if matrix[bottom][0] == target:
                return True
            elif matrix[bottom][0] < target:
                return self.binarySearch(matrix[bottom], target)
            elif matrix[bottom][0] > target and bottom > 0:
                return self.binarySearch(matrix[bottom - 1], target)
            return False

        return False