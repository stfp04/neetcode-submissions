class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if not fresh:
            return 0

        minutes = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    if min(r+dr,c+dc) < 0 or r+dr==ROWS or c+dc==COLS or \
                        grid[r+dr][c+dc] != 1:
                            continue
                    grid[r+dr][c+dc] = 2
                    queue.append((r+dr, c+dc))
                    fresh -= 1

            minutes += 1
            if not fresh:
                return minutes


        if not fresh:
            return minutes
        return -1
