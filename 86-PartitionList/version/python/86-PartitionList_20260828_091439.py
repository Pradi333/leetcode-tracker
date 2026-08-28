# Last updated: 8/28/2026, 9:14:39 AM
1class Solution:
2    def subsetsWithDup(self, nums):
3        nums.sort()
4        result = []
5
6        def backtrack(start, current):
7            result.append(current[:])
8
9            for i in range(start, len(nums)):
10
11                if i > start and nums[i] == nums[i - 1]:
12                    continue
13
14                current.append(nums[i])
15
16                backtrack(i + 1, current)
17
18                current.pop()
19
20        backtrack(0, [])
21
22        return result 