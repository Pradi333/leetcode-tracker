# Last updated: 7/27/2026, 10:25:34 AM
1class Solution:
2    def isValidSudoku(self, board):
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6
7        for r in range(9):
8            for c in range(9):
9                value = board[r][c]
10
11                if value == '.':
12                    continue
13
14                # Check row
15                if value in rows[r]:
16                    return False
17                rows[r].add(value)
18
19                # Check column
20                if value in cols[c]:
21                    return False
22                cols[c].add(value)
23
24                # Find 3x3 box
25                box = (r // 3) * 3 + (c // 3)
26
27                if value in boxes[box]:
28                    return False
29                boxes[box].add(value)
30
31        return True