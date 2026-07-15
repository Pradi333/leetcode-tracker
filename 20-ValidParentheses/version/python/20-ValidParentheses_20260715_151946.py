# Last updated: 7/15/2026, 3:19:46 PM
1class Solution(object):
2    def isValid(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        stack = []
8        pairs = {
9            ')': '(',
10            ']': '[',
11            '}': '{'
12        }
13
14        for ch in s:
15            if ch in "([{":
16                stack.append(ch)
17            else:
18                if not stack or stack[-1] != pairs[ch]:
19                    return False
20                stack.pop()
21
22        return len(stack) == 0
23        