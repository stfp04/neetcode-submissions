class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col, visit):
            nonlocal ROWS, COLS
            count = 0
            if row == ROWS or col == COLS or \
                    min(row, col) < 0 or \
                    grid[row][col] == 1 or \
                    (row, col) in visit:
                return 0

            if row == ROWS - 1 and col == COLS - 1:
                return 1

            count = 0

            visit.add((row,col))

            count += dfs(row + 1, col, visit)
            count += dfs(row - 1, col, visit)
            count += dfs(row, col + 1, visit)
            count += dfs(row, col - 1, visit)

            visit.remove((row,col))

            return count
        return dfs(0,0,set())
        
            