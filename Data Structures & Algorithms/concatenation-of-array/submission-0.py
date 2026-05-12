class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            t = nums[i]
            ans[i] = t
            ans[i + n] = t
        return ans