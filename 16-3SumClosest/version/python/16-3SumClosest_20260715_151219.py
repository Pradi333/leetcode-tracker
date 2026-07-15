# Last updated: 7/15/2026, 3:12:19 PM
1class Solution(object):
2    def threeSumClosest(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        nums.sort()
9        closest = nums[0] + nums[1] + nums[2]
10
11        for i in range(len(nums) - 2):
12            left = i + 1
13            right = len(nums) - 1
14
15            while left < right:
16                total = nums[i] + nums[left] + nums[right]
17
18                if abs(target - total) < abs(target - closest):
19                    closest = total
20
21                if total < target:
22                    left += 1
23                elif total > target:
24                    right -= 1
25                else:
26                    return total
27
28        return closest