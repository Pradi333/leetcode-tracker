# Last updated: 7/27/2026, 3:09:00 PM
1class Solution:
2    def solveNQueens(self, n):
3        result = []
4        board = [["."] * n for _ in range(n)]
5
6        cols = set()
7        diag1 = set()
8        diag2 = set()
9
10        def backtrack(row):
11            if row == n:
12                result.append(["".join(r) for r in board])
13                return
14
15            for col in range(n):
16                if col in cols:
17                    continue
18
19                if row - col in diag1:
20                    continue
21
22                if row + col in diag2:
23                    continue
24
25                # Place queen
26                board[row][col] = "Q"
27                cols.add(col)
28                diag1.add(row - col)
29                diag2.add(row + col)
30
31                backtrack(row + 1)
32
33                # Remove queen
34                board[row][col] = "."
35                cols.remove(col)
36                diag1.remove(row - col)
37                diag2.remove(row + col)
38
39        backtrack(0)
40
41        return result