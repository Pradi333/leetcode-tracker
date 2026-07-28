# Last updated: 7/28/2026, 3:00:23 PM
1class Solution:
2    def simplifyPath(self, path):
3        stack = []
4
5        parts = path.split("/")
6
7        for part in parts:
8            if part == "" or part == ".":
9                continue
10
11            elif part == "..":
12                if stack:
13                    stack.pop()
14
15            else:
16                stack.append(part)
17
18        return "/" + "/".join(stack)