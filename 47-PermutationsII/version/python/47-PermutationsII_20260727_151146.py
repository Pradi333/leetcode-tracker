# Last updated: 7/27/2026, 3:11:46 PM
1class Solution:
2    def canJump(self, nums):
3        farthest = 0
4
5        for i in range(len(nums)):
6            if i > farthest:
7                return False
8
9            farthest = max(farthest, i + nums[i])
10
11        return True