# Last updated: 7/27/2026, 10:24:44 AM
1class Solution:
2    def searchRange(self, nums, target):
3        first = self.findFirst(nums, target)
4        last = self.findLast(nums, target)
5
6        return [first, last]
7
8    def findFirst(self, nums, target):
9        left = 0
10        right = len(nums) - 1
11        result = -1
12
13        while left <= right:
14            mid = (left + right) // 2
15
16            if nums[mid] == target:
17                result = mid
18                right = mid - 1
19            elif nums[mid] < target:
20                left = mid + 1
21            else:
22                right = mid - 1
23
24        return result
25
26    def findLast(self, nums, target):
27        left = 0
28        right = len(nums) - 1
29        result = -1
30
31        while left <= right:
32            mid = (left + right) // 2
33
34            if nums[mid] == target:
35                result = mid
36                left = mid + 1
37            elif nums[mid] < target:
38                left = mid + 1
39            else:
40                right = mid - 1
41
42        return result