# Last updated: 7/28/2026, 3:03:08 PM
1class Solution:
2    def searchMatrix(self, matrix, target):
3        rows = len(matrix)
4        cols = len(matrix[0])
5
6        left = 0
7        right = rows * cols - 1
8
9        while left <= right:
10            mid = (left + right) // 2
11
12            row = mid // cols
13            col = mid % cols
14
15            if matrix[row][col] == target:
16                return True
17
18            elif matrix[row][col] < target:
19                left = mid + 1
20
21            else:
22                right = mid - 1
23
24        return False