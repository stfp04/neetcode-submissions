class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = []

        for i in range(ROWS):
            row = []
            prefix = 0
            for j in range(COLS):
                value = matrix[i][j] + prefix
                if i > 0:
                    value += self.matrix[i - 1][j]
                prefix += matrix[i][j]
                row.append(value)
                
            self.matrix.append(row)
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        base = self.matrix[row2][col2]
        print("row-col", self.matrix[row1][col1], "base", base)
        if row1 > 0 and col1 > 0:
            base -= self.matrix[row1 - 1][col2]
            base -= self.matrix[row2][col1 - 1]
            base += self.matrix[row1 - 1][col1 - 1]
        elif row1 > 0:
            base -= self.matrix[row1 - 1][col2]
        elif col1 > 0:
            base -= self.matrix[row2][col1 - 1]
        print(self.matrix[row1 - 1][col2], self.matrix[row2][col1 - 1], self.matrix[row1 - 1][col1 - 1])
        return base


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)