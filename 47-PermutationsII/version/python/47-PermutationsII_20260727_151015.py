# Last updated: 7/27/2026, 3:10:15 PM
1class Solution:
2    def totalNQueens(self, n):
3        count = [0]
4
5        cols = set()
6        diag1 = set()
7        diag2 = set()
8
9        def backtrack(row):
10            if row == n:
11                count[0] += 1
12                return
13
14            for col in range(n):
15                if col in cols:
16                    continue
17
18                if row - col in diag1:
19                    continue
20
21                if row + col in diag2:
22                    continue
23
24                # Place queen
25                cols.add(col)
26                diag1.add(row - col)
27                diag2.add(row + col)
28
29                backtrack(row + 1)
30
31                # Remove queen
32                cols.remove(col)
33                diag1.remove(row - col)
34                diag2.remove(row + col)
35
36        backtrack(0)
37
38        return count[0]