class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        backRow = [0] * len(obstacleGrid[0])
        backRow[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    backRow[j] = 0
                else:
                    if j > 0:
                        backRow[j] += backRow[j - 1]
        return backRow[-1]