// Last updated: 7/23/2026, 10:22:20 AM
1class Solution {
2    public int strStr(String haystack, String needle) {
3
4        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
5
6            int j = 0;
7
8            while (j < needle.length() &&
9                   haystack.charAt(i + j) == needle.charAt(j)) {
10                j++;
11            }
12
13            if (j == needle.length()) {
14                return i;
15            }
16        }
17
18        return -1;
19    }
20}