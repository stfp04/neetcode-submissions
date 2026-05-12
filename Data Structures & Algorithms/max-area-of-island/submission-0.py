class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c,v):
            if r == ROWS or c == COLS or \
                    min(r,c) < 0 or \
                    grid[r][c] == 0 or \
                    (r,c) in v:
                return 0
            
            v.add((r,c))

            count = 1
            count += dfs(r+1,c,v)
            count += dfs(r-1,c,v)
            count += dfs(r,c+1,v)
            count += dfs(r,c-1,v)

            return count

        m = 0
        v = set()
        for i in range(ROWS):
            for j in range(COLS):
                n = dfs(i,j,v)
                if n:
                    m = max(m,n)

        return m