# Last updated: 7/28/2026, 4:02:41 PM
1class Solution:
2    def exist(self, board, word):
3        rows = len(board)
4        cols = len(board[0])
5
6        def dfs(r, c, index):
7            # All characters matched
8            if index == len(word):
9                return True
10
11            # Out of bounds or character doesn't match
12            if (r < 0 or r >= rows or
13                c < 0 or c >= cols or
14                board[r][c] != word[index]):
15                return False
16
17            # Mark cell as visited
18            temp = board[r][c]
19            board[r][c] = "#"
20
21            # Search in 4 directions
22            found = (
23                dfs(r + 1, c, index + 1) or
24                dfs(r - 1, c, index + 1) or
25                dfs(r, c + 1, index + 1) or
26                dfs(r, c - 1, index + 1)
27            )
28
29            # Restore the cell
30            board[r][c] = temp
31
32            return found
33
34        for r in range(rows):
35            for c in range(cols):
36                if board[r][c] == word[0]:
37                    if dfs(r, c, 0):
38                        return True
39
40        return False