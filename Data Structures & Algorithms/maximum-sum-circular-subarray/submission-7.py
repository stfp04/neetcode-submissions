class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]

        for i in range(n):
            j = i
            k = 0
            curSum = 0
            while k < n:
                max(curSum, 0)
                curSum += nums[j]
                maxSum = max(curSum, maxSum)
                k += 1
                j = (j + 1) % n

        return maxSum
        