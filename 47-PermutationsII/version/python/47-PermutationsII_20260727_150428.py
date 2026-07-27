# Last updated: 7/27/2026, 3:04:28 PM
1class Solution:
2    def permuteUnique(self, nums):
3        nums.sort()
4        result = []
5
6        def backtrack(path, used):
7            if len(path) == len(nums):
8                result.append(path[:])
9                return
10
11            for i in range(len(nums)):
12                if used[i]:
13                    continue
14
15                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
16                    continue
17
18                used[i] = True
19                path.append(nums[i])
20
21                backtrack(path, used)
22
23                path.pop()
24                used[i] = False
25
26        backtrack([], [False] * len(nums))
27
28        return result