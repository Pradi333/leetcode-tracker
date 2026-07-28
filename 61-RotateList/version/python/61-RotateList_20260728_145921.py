# Last updated: 7/28/2026, 2:59:21 PM
1class Solution:
2    def climbStairs(self, n):
3        if n <= 2:
4            return n
5
6        first = 1
7        second = 2
8
9        for i in range(3, n + 1):
10            third = first + second
11            first = second
12            second = third
13
14        return second