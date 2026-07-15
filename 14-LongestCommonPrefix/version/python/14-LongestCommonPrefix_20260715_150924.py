# Last updated: 7/15/2026, 3:09:24 PM
1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: str
6        """
7        if not strs:
8            return ""
9
10        prefix = strs[0]
11
12        for s in strs[1:]:
13            while s[:len(prefix)] != prefix:
14                prefix = prefix[:-1]
15                if prefix == "":
16                    return ""
17
18        return prefix
19        