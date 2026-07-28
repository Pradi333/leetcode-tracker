# Last updated: 7/28/2026, 2:48:15 PM
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid):
3        m = len(obstacleGrid)
4        n = len(obstacleGrid[0])
5
6        dp = [0] * n
7        dp[0] = 1
8
9        for i in range(m):
10            for j in range(n):
11                if obstacleGrid[i][j] == 1:
12                    dp[j] = 0
13                elif j > 0:
14                    dp[j] = dp[j] + dp[j - 1]
15
16        return dp[n - 1]