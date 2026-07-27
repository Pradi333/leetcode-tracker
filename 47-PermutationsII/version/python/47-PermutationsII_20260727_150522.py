# Last updated: 7/27/2026, 3:05:22 PM
1class Solution:
2    def rotate(self, matrix):
3        n = len(matrix)
4
5        # Transpose the matrix
6        for i in range(n):
7            for j in range(i + 1, n):
8                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
9
10        # Reverse every row
11        for row in matrix:
12            row.reverse()
13
14