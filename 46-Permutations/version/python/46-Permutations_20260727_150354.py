# Last updated: 7/27/2026, 3:03:54 PM
1class Solution:
2    def permute(self, nums):
3        result = []
4
5        def backtrack(path, remaining):
6            if not remaining:
7                result.append(path[:])
8                return
9
10            for i in range(len(remaining)):
11                path.append(remaining[i])
12
13                backtrack(
14                    path,
15                    remaining[:i] + remaining[i+1:]
16                )
17
18                path.pop()
19
20        backtrack([], nums)
21
22        return result