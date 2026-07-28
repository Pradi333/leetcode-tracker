# Last updated: 7/28/2026, 2:49:55 PM
1class Solution:
2    def isNumber(self, s):
3        s = s.strip()
4
5        if not s:
6            return False
7
8        seen_digit = False
9        seen_dot = False
10        seen_exp = False
11        digit_after_exp = True
12
13        for i, ch in enumerate(s):
14
15            if ch.isdigit():
16                seen_digit = True
17
18                if seen_exp:
19                    digit_after_exp = True
20
21            elif ch in '+-':
22                # Sign is allowed only at the beginning
23                # or immediately after e/E
24                if i != 0 and s[i - 1] not in 'eE':
25                    return False
26
27            elif ch == '.':
28                # Only one decimal point and no dot after e/E
29                if seen_dot or seen_exp:
30                    return False
31
32                seen_dot = True
33
34            elif ch in 'eE':
35                # e/E needs a digit before it
36                # and can appear only once
37                if seen_exp or not seen_digit:
38                    return False
39
40                seen_exp = True
41                digit_after_exp = False
42
43            else:
44                return False
45
46        return seen_digit and digit_after_exp