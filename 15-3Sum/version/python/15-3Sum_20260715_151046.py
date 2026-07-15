# Last updated: 7/15/2026, 3:10:46 PM
1class Solution(object):
2    def threeSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        nums.sort()
8        result = []
9
10        for i in range(len(nums) - 2):
11            if i > 0 and nums[i] == nums[i - 1]:
12                continue
13
14            left = i + 1
15            right = len(nums) - 1
16
17            while left < right:
18                total = nums[i] + nums[left] + nums[right]
19
20                if total == 0:
21                    result.append([nums[i], nums[left], nums[right]])
22
23                    while left < right and nums[left] == nums[left + 1]:
24                        left += 1
25                    while left < right and nums[right] == nums[right - 1]:
26                        right -= 1
27
28                    left += 1
29                    right -= 1
30
31                elif total < 0:
32                    left += 1
33                else:
34                    right -= 1
35
36        return result
37        