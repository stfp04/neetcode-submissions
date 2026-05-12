class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c,v):
            if r == ROWS or c == COLS or \
                    min(r,c) < 0 or \
                    grid[r][c] == "0" or \
                    (r,c) in v:
                return 0
            
            v.add((r,c))

            count = 1
            count += dfs(r+1,c,v)
            count += dfs(r-1,c,v)
            count += dfs(r,c+1,v)
            count += dfs(r,c-1,v)

            return 1

        n = 0
        v = set()
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,v):
                    n += 1

        return n

        