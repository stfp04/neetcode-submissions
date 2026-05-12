class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for num in nums:
            if num not in unique:
                unique[num] = 1
            else:
                return True
        return False