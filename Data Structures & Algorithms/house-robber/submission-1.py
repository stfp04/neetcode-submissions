class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money = [0] * len(nums)

        for i in range(n):
            if i == 0:
                money[i] = nums[i]
            elif i == 1:
                money[i] = max(money[i-1], nums[i])
            else:
                money[i] = max(money[i-2] + nums[i], money[i-1])

        return money[-1]