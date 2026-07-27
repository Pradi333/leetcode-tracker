# Last updated: 7/27/2026, 3:06:12 PM
1class Solution:
2    def groupAnagrams(self, strs):
3        groups = {}
4
5        for word in strs:
6            key = ''.join(sorted(word))
7
8            if key not in groups:
9                groups[key] = []
10
11            groups[key].append(word)
12
13        return list(groups.values())