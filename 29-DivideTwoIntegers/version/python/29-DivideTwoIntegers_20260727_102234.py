# Last updated: 7/27/2026, 10:22:34 AM
1class Solution:
2    def nextPermutation(self, nums):
3        n = len(nums)
4
5        # Step 1: Find first decreasing element from right
6        i = n - 2
7
8        while i >= 0 and nums[i] >= nums[i + 1]:
9            i -= 1
10
11        # Step 2: Find element greater than nums[i]
12        if i >= 0:
13            j = n - 1
14
15            while nums[j] <= nums[i]:
16                j -= 1
17
18            # Swap
19            nums[i], nums[j] = nums[j], nums[i]
20
21        # Step 3: Reverse remaining elements
22        nums[i + 1:] = reversed(nums[i + 1:])