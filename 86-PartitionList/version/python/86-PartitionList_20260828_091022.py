# Last updated: 8/28/2026, 9:10:22 AM
1class Solution:
2    def merge(self, nums1, m, nums2, n):
3
4        i = m - 1
5        j = n - 1
6        k = m + n - 1
7
8        while j >= 0:
9
10            if i >= 0 and nums1[i] > nums2[j]:
11                nums1[k] = nums1[i]
12                i -= 1
13            else:
14                nums1[k] = nums2[j]
15                j -= 1
16
17            k -= 1