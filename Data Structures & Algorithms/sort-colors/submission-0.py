class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3

        for n in nums:
            freq[n] += 1

        base = 0
        for i in range(len(freq)):
            entry = freq[i]
            for j in range(entry):
                nums[base + j] = i
            base += entry
        