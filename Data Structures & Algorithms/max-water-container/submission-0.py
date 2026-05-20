class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxArea = 0

        while L < R:
            width = R - L
            height = min(heights[L], heights[R])
            area = width * height
            maxArea = max(area, maxArea)

            if heights[L] > heights[R]:
                R -= 1
            else: 
                L += 1

        return maxArea