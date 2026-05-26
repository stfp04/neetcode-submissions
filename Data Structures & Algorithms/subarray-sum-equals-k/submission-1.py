class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = {0: 1}
        
        prefix = []
        curr = 0
        for i in range(n):
            curr += nums[i]
            prefix.append(curr)

        res = 0
        for i in range(n):
            if prefix[i] - k in sums:
                res += sums[prefix[i] - k]
            if prefix[i] in sums:
                sums[prefix[i]] += 1
            else:
                sums[prefix[i]] = 1

        return res