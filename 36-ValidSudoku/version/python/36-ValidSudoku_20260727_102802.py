# Last updated: 7/27/2026, 10:28:02 AM
1class Solution:
2    def combinationSum(self, candidates, target):
3        result = []
4
5        def backtrack(start, current, total):
6            if total == target:
7                result.append(current[:])
8                return
9
10            if total > target:
11                return
12
13            for i in range(start, len(candidates)):
14                current.append(candidates[i])
15
16                # Same element can be used again
17                backtrack(i, current, total + candidates[i])
18
19                current.pop()
20
21        backtrack(0, [], 0)
22
23        return result