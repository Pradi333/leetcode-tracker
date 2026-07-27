# Last updated: 7/27/2026, 10:34:15 AM
1class Solution:
2    def jump(self, nums):
3        jumps = 0
4        current_end = 0
5        farthest = 0
6
7        for i in range(len(nums) - 1):
8            farthest = max(farthest, i + nums[i])
9
10            # Reached the end of the current jump
11            if i == current_end:
12                jumps += 1
13                current_end = farthest
14
15        return jumps