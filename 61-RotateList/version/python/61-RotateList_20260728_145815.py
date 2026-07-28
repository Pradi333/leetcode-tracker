# Last updated: 7/28/2026, 2:58:15 PM
1class Solution:
2    def mySqrt(self, x):
3        left = 0
4        right = x
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            if mid * mid == x:
10                return mid
11
12            elif mid * mid < x:
13                left = mid + 1
14
15            else:
16                right = mid - 1
17
18        return right