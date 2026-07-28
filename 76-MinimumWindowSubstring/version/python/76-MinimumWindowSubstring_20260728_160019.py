# Last updated: 7/28/2026, 4:00:19 PM
1class Solution:
2    def subsets(self, nums):
3        result = []
4
5        def backtrack(start, current):
6            result.append(current[:])
7
8            for i in range(start, len(nums)):
9                current.append(nums[i])
10
11                backtrack(i + 1, current)
12
13                current.pop()
14
15        backtrack(0, [])
16
17        return result