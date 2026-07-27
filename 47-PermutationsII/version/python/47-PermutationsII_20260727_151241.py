# Last updated: 7/27/2026, 3:12:41 PM
1class Solution:
2    def insert(self, intervals, newInterval):
3        result = []
4        i = 0
5        n = len(intervals)
6
7        # Add intervals before newInterval
8        while i < n and intervals[i][1] < newInterval[0]:
9            result.append(intervals[i])
10            i += 1
11
12        # Merge overlapping intervals
13        while i < n and intervals[i][0] <= newInterval[1]:
14            newInterval[0] = min(newInterval[0], intervals[i][0])
15            newInterval[1] = max(newInterval[1], intervals[i][1])
16            i += 1
17
18        result.append(newInterval)
19
20        # Add remaining intervals
21        while i < n:
22            result.append(intervals[i])
23            i += 1
24
25        return result