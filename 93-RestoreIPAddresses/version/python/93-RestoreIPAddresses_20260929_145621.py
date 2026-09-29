# Last updated: 9/29/2026, 2:56:21 PM
1class Solution:
2    def restoreIpAddresses(self, s):
3        result = []
4
5        def backtrack(index, parts):
6            # If we have 4 parts
7            if len(parts) == 4:
8                # All digits must be used
9                if index == len(s):
10                    result.append(".".join(parts))
11                return
12
13            # Try taking 1, 2, or 3 digits
14            for length in range(1, 4):
15
16                if index + length > len(s):
17                    break
18
19                part = s[index:index + length]
20
21                # Leading zero is not allowed
22                if len(part) > 1 and part[0] == '0':
23                    continue
24
25                # Value must be <= 255
26                if int(part) > 255:
27                    continue
28
29                parts.append(part)
30
31                backtrack(index + length, parts)
32
33                parts.pop()
34
35        backtrack(0, [])
36        return result