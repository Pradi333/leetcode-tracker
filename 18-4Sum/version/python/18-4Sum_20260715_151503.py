# Last updated: 7/15/2026, 3:15:03 PM
1class Solution(object):
2    def fourSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[List[int]]
7        """
8        nums.sort()
9        result = []
10        n = len(nums)
11
12        for i in range(n - 3):
13            if i > 0 and nums[i] == nums[i - 1]:
14                continue
15
16            for j in range(i + 1, n - 2):
17                if j > i + 1 and nums[j] == nums[j - 1]:
18                    continue
19
20                left = j + 1
21                right = n - 1
22
23                while left < right:
24                    total = nums[i] + nums[j] + nums[left] + nums[right]
25
26                    if total == target:
27                        result.append([nums[i], nums[j], nums[left], nums[right]])
28
29                        while left < right and nums[left] == nums[left + 1]:
30                            left += 1
31                        while left < right and nums[right] == nums[right - 1]:
32                            right -= 1
33
34                        left += 1
35                        right -= 1
36
37                    elif total < target:
38                        left += 1
39                    else:
40                        right -= 1
41
42        return result
43        