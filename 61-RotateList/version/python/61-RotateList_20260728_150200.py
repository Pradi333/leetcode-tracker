# Last updated: 7/28/2026, 3:02:00 PM
1class Solution:
2    def setZeroes(self, matrix):
3        rows = len(matrix)
4        cols = len(matrix[0])
5
6        zero_rows = set()
7        zero_cols = set()
8
9        # Find all rows and columns containing 0
10        for i in range(rows):
11            for j in range(cols):
12                if matrix[i][j] == 0:
13                    zero_rows.add(i)
14                    zero_cols.add(j)
15
16        # Set rows to zero
17        for i in zero_rows:
18            for j in range(cols):
19                matrix[i][j] = 0
20
21        # Set columns to zero
22        for j in zero_cols:
23            for i in range(rows):
24                matrix[i][j] = 0