class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1]
        suffix = [1]
        for i in range(n):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[n - i - 1])

        print(prefix, suffix)

        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[n - i - 1])

        return res