# Last updated: 7/15/2026, 3:17:43 PM
1class Solution(object):
2    def isMatch(self, s, p):
3        """
4        :type s: str
5        :type p: str
6        :rtype: bool
7        """
8        m, n = len(s), len(p)
9
10        dp = [[False] * (n + 1) for _ in range(m + 1)]
11        dp[0][0] = True
12
13        # Handle patterns like a*, a*b*, a*b*c*
14        for j in range(2, n + 1):
15            if p[j - 1] == '*':
16                dp[0][j] = dp[0][j - 2]
17
18        for i in range(1, m + 1):
19            for j in range(1, n + 1):
20                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
21                    dp[i][j] = dp[i - 1][j - 1]
22
23                elif p[j - 1] == '*':
24                    # Zero occurrences
25                    dp[i][j] = dp[i][j - 2]
26
27                    # One or more occurrences
28                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
29                        dp[i][j] = dp[i][j] or dp[i - 1][j]
30
31        return dp[m][n]
32        