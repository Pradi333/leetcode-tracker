# Last updated: 7/27/2026, 10:29:49 AM
1class Solution:
2    def firstMissingPositive(self, nums):
3        n = len(nums)
4
5        # Put each number in its correct position
6        for i in range(n):
7            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
8                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
9
10        # Find the first position with the wrong number
11        for i in range(n):
12            if nums[i] != i + 1:
13                return i + 1
14
15        return n + 1