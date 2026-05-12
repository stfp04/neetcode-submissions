class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in sums:
                return [sums[num], i]
            diff = target - num
            sums[diff] = i
