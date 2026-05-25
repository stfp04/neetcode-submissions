class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, 0
        n = len(height)
        a = 0

        prefix = []
        curr_max = 0
        for i in range(n):
            curr_max = max(height[i], curr_max)
            prefix.append(curr_max)

        suffix = []
        curr_max = 0
        for i in range(n - 1, -1, -1):
            curr_max = max(height[i], curr_max)
            suffix.append(curr_max)
        suffix.reverse()
            

        for i in range(n):
            a += min(prefix[i], suffix[i]) - height[i]

        return a
