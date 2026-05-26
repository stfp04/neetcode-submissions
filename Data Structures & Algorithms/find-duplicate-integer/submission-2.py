class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1

        bits = 1
        for _ in range(n):
            bits = bits << 1
            bits = bits | 1
        
        for num in nums:
            bit = 1 << (num - 1)
            nbit = bits & bit
            if not nbit:
                return num
            bits = bits ^ bit

        return 0