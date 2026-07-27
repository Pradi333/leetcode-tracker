# Last updated: 7/27/2026, 10:33:38 AM
1class Solution:
2    def isMatch(self, s, p):
3        i = 0
4        j = 0
5
6        star = -1
7        match = 0
8
9        while i < len(s):
10
11            # Characters match or '?' matches one character
12            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
13                i += 1
14                j += 1
15
16            # '*' found
17            elif j < len(p) and p[j] == '*':
18                star = j
19                match = i
20                j += 1
21
22            # Previous '*' can match one more character
23            elif star != -1:
24                j = star + 1
25                match += 1
26                i = match
27
28            else:
29                return False
30
31        # Remaining pattern must contain only '*'
32        while j < len(p) and p[j] == '*':
33            j += 1
34
35        return j == len(p)