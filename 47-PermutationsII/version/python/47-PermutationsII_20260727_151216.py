# Last updated: 7/27/2026, 3:12:16 PM
1class Solution:
2    def merge(self, intervals):
3        intervals.sort()
4
5        result = []
6
7        for interval in intervals:
8            if not result or result[-1][1] < interval[0]:
9                result.append(interval)
10            else:
11                result[-1][1] = max(result[-1][1], interval[1])
12
13        return result