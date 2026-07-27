# Last updated: 7/27/2026, 3:07:19 PM
1class Solution:
2    def myPow(self, x, n):
3        if n == 0:
4            return 1
5
6        if n < 0:
7            x = 1 / x
8            n = -n
9
10        result = 1
11
12        while n > 0:
13            if n % 2 == 1:
14                result = result * x
15
16            x = x * x
17            n = n // 2
18
19        return result