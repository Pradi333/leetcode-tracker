# Last updated: 7/15/2026, 3:05:54 PM
1class Solution(object):
2    def isPalindrome(self, x):
3        """
4        :type x: int
5        :rtype: bool
6        """
7        if x < 0:
8            return False
9
10        original = x
11        reverse = 0
12
13        while x != 0:
14            digit = x % 10
15            reverse = reverse * 10 + digit
16            x //= 10
17
18        return original == reverse