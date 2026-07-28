# Last updated: 7/28/2026, 2:49:01 PM
1class Solution:
2    def minPathSum(self, grid):
3        m = len(grid)
4        n = len(grid[0])
5
6        for i in range(m):
7            for j in range(n):
8                if i == 0 and j == 0:
9                    continue
10
11                if i == 0:
12                    grid[i][j] += grid[i][j - 1]
13
14                elif j == 0:
15                    grid[i][j] += grid[i - 1][j]
16
17                else:
18                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
19
20        return grid[m - 1][n - 1]