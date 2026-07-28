# Last updated: 7/28/2026, 2:52:25 PM
1class Solution:
2    def plusOne(self, digits):
3        for i in range(len(digits) - 1, -1, -1):
4            if digits[i] < 9:
5                digits[i] += 1
6                return digits
7
8            digits[i] = 0
9
10        return [1] + digits