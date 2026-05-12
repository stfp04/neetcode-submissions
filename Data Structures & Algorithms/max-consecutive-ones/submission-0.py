class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best, res = 0, 0
        for i in range(len(nums)):
            t = nums[i]
            if not t:
                best = max(best, res)
                res = 0
                continue
            res = res + t
        return max(best, res)