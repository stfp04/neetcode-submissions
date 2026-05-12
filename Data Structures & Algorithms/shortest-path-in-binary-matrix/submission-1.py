class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        length = 1
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                directions = [
                    [0, 1],   # right
                    [0, -1],  # left
                    [1, 0],   # down
                    [-1, 0],  # up
                    [1, 1],   # down-right
                    [1, -1],  # down-left
                    [-1, 1],  # up-right
                    [-1, -1]  # up-left
                ]

                for dr, dc in directions:
                    if min(r+dr,c+dc) < 0 or \
                        r+dr==ROWS or c+dc==COLS or \
                        (r+dr,c+dc) in visit or \
                        grid[r+dr][c+dc]==1:
                            continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            
            length += 1

        return -1