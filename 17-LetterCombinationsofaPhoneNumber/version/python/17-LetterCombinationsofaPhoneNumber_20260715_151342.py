# Last updated: 7/15/2026, 3:13:42 PM
1class Solution(object):
2    def letterCombinations(self, digits):
3        """
4        :type digits: str
5        :rtype: List[str]
6        """
7        if not digits:
8            return []
9
10        phone = {
11            '2': "abc",
12            '3': "def",
13            '4': "ghi",
14            '5': "jkl",
15            '6': "mno",
16            '7': "pqrs",
17            '8': "tuv",
18            '9': "wxyz"
19        }
20
21        result = []
22
23        def backtrack(index, path):
24            if index == len(digits):
25                result.append(path)
26                return
27
28            for ch in phone[digits[index]]:
29                backtrack(index + 1, path + ch)
30
31        backtrack(0, "")
32        return result
33        