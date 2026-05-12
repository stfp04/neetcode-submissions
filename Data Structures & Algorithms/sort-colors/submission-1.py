class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3

        for n in nums:
            freq[n] += 1

        k = 0
        for i in range(len(freq)):
            for _ in range(freq[i]):
                nums[k] = i
                k += 1
        