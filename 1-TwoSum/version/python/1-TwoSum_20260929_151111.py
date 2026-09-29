# Last updated: 9/29/2026, 3:11:11 PM
1class Solution:
2    def twoSum(self, nums, target):
3        seen = {}
4
5        for i in range(len(nums)):
6            needed = target - nums[i]
7
8            if needed in seen:
9                return [seen[needed], i]
10
11            seen[nums[i]] = i   