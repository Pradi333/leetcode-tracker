# Last updated: 7/28/2026, 3:00:55 PM
1class Solution:
2    def minDistance(self, word1, word2):
3        m = len(word1)
4        n = len(word2)
5
6        dp = [[0] * (n + 1) for _ in range(m + 1)]
7
8        # If word2 is empty, delete all characters from word1
9        for i in range(m + 1):
10            dp[i][0] = i
11
12        # If word1 is empty, insert all characters of word2
13        for j in range(n + 1):
14            dp[0][j] = j
15
16        for i in range(1, m + 1):
17            for j in range(1, n + 1):
18
19                if word1[i - 1] == word2[j - 1]:
20                    dp[i][j] = dp[i - 1][j - 1]
21
22                else:
23                    dp[i][j] = 1 + min(
24                        dp[i - 1][j],      # Delete
25                        dp[i][j - 1],      # Insert
26                        dp[i - 1][j - 1]   # Replace
27                    )
28
29        return dp[m][n]