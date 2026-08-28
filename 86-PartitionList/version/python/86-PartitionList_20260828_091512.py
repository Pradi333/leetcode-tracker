# Last updated: 8/28/2026, 9:15:12 AM
1class Solution:
2    def numDecodings(self, s):
3        if s[0] == '0':
4            return 0
5
6        dp = [0] * (len(s) + 1)
7
8        dp[0] = 1
9        dp[1] = 1
10
11        for i in range(2, len(s) + 1):
12
13            # Take one digit
14            if s[i - 1] != '0':
15                dp[i] += dp[i - 1]
16
17            # Take two digits
18            if 10 <= int(s[i - 2:i]) <= 26:
19                dp[i] += dp[i - 2]
20
21        return dp[len(s)]