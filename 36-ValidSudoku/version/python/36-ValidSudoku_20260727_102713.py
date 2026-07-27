# Last updated: 7/27/2026, 10:27:13 AM
1class Solution:
2    def countAndSay(self, n):
3        result = "1"
4
5        for _ in range(n - 1):
6            new_result = ""
7            count = 1
8
9            for i in range(1, len(result)):
10                if result[i] == result[i - 1]:
11                    count += 1
12                else:
13                    new_result += str(count) + result[i - 1]
14                    count = 1
15
16            new_result += str(count) + result[-1]
17            result = new_result
18
19        return result