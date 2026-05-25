class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0]
        for i in range(n):
            prefix.append(nums[i] + prefix[-1])

        suffix = 0
        pivot = -1
        for i in range(n - 1, -1, -1):
            print(i)
            if suffix == prefix[i]:
                pivot = i
            suffix += nums[i] 

        return pivot