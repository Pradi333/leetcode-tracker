# Last updated: 7/27/2026, 3:13:08 PM
1class Solution:
2    def lengthOfLastWord(self, s):
3        s = s.strip()
4
5        words = s.split()
6
7        return len(words[-1])