# Last updated: 7/28/2026, 3:57:37 PM
1class Solution:
2    def minWindow(self, s, t):
3        if not s or not t:
4            return ""
5
6        need = {}
7
8        for ch in t:
9            need[ch] = need.get(ch, 0) + 1
10
11        window = {}
12        left = 0
13        count = 0
14        min_len = float("inf")
15        min_start = 0
16
17        for right in range(len(s)):
18            ch = s[right]
19            window[ch] = window.get(ch, 0) + 1
20
21            if ch in need and window[ch] <= need[ch]:
22                count += 1
23
24            while count == len(t):
25                if right - left + 1 < min_len:
26                    min_len = right - left + 1
27                    min_start = left
28
29                left_ch = s[left]
30                window[left_ch] -= 1
31
32                if left_ch in need and window[left_ch] < need[left_ch]:
33                    count -= 1
34
35                left += 1
36
37        if min_len == float("inf"):
38            return ""
39
40        return s[min_start:min_start + min_len]