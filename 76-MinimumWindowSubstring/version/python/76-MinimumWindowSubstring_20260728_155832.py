# Last updated: 7/28/2026, 3:58:32 PM
1class Solution:
2    def combine(self, n, k):
3        result = []
4
5        def backtrack(start, current):
6            if len(current) == k:
7                result.append(current[:])
8                return
9
10            for i in range(start, n + 1):
11                current.append(i)
12
13                backtrack(i + 1, current)
14
15                current.pop()
16
17        backtrack(1, [])
18
19        return result