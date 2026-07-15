# Last updated: 7/15/2026, 3:07:30 PM
1class Solution(object):
2    def romanToInt(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        roman = {
8            'I': 1,
9            'V': 5,
10            'X': 10,
11            'L': 50,
12            'C': 100,
13            'D': 500,
14            'M': 1000
15        }
16
17        total = 0
18
19        for i in range(len(s)):
20            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
21                total -= roman[s[i]]
22            else:
23                total += roman[s[i]]
24
25        return total