class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        curRow = [0] * n
        i = n - 1
        while obstacleGrid[m-1][i] == 0 and i >= 0:
            curRow[i] = 1
            i -= 1
        while i >= 0:
            curRow[i] = 0
            i -= 1
        
        for i in range(m-2,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    curRow[j] = 0
                elif j + 1 < n and obstacleGrid[i][j+1] == 0:
                    curRow[j] += curRow[j+1]

        return curRow[0]
                