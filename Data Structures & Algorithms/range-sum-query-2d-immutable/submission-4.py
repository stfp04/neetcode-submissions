class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.nums = []

        for row in matrix:

            prefix = row[:]

            for i in range(1, len(prefix)):
                prefix[i] += prefix[i - 1]

            self.nums.append(prefix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        ans = 0

        for i in range(row1, row2 + 1):

            if col1 > 0:
                ans += self.nums[i][col2] - self.nums[i][col1 - 1]
            else:
                ans += self.nums[i][col2]

        return ans