# Last updated: 8/28/2026, 9:11:08 AM
1class Solution:
2    def grayCode(self, n):
3        result = [0]
4
5        for i in range(n):
6            add = 1 << i
7
8            for j in range(len(result) - 1, -1, -1):
9                result.append(result[j] + add)
10
11        return result