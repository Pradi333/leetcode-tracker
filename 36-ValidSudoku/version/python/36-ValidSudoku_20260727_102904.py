# Last updated: 7/27/2026, 10:29:04 AM
1class Solution:
2    def combinationSum2(self, candidates, target):
3        result = []
4
5        candidates.sort()
6
7        def backtrack(start, current, total):
8            if total == target:
9                result.append(current[:])
10                return
11
12            if total > target:
13                return
14
15            for i in range(start, len(candidates)):
16
17                # Skip duplicate numbers at the same level
18                if i > start and candidates[i] == candidates[i - 1]:
19                    continue
20
21                # Since array is sorted
22                if total + candidates[i] > target:
23                    break
24
25                current.append(candidates[i])
26
27                # i + 1 means each element can be used only once
28                backtrack(i + 1, current, total + candidates[i])
29
30                current.pop()
31
32        backtrack(0, [], 0)
33
34        return result