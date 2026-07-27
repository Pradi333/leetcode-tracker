# Last updated: 7/27/2026, 3:10:56 PM
1class Solution:
2    def spiralOrder(self, matrix):
3        result = []
4
5        while matrix:
6            # First row
7            result += matrix.pop(0)
8
9            # Last column
10            if matrix and matrix[0]:
11                for row in matrix:
12                    result.append(row.pop())
13
14            # Last row
15            if matrix:
16                result += matrix.pop()[::-1]
17
18            # First column
19            if matrix and matrix[0]:
20                for row in matrix[::-1]:
21                    result.append(row.pop(0))
22
23        return result