class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxL, maxR = 0, 0
        curSum, maxSum = 0, nums[0]
        L  = 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R

            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxR = R
                maxL = L

        return maxSum