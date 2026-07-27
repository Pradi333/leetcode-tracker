# Last updated: 7/27/2026, 3:14:03 PM
1class Solution:
2    def getPermutation(self, n, k):
3        numbers = []
4
5        for i in range(1, n + 1):
6            numbers.append(str(i))
7
8        factorial = [1] * (n + 1)
9
10        for i in range(1, n + 1):
11            factorial[i] = factorial[i - 1] * i
12
13        k -= 1
14
15        result = ""
16
17        for i in range(n, 0, -1):
18            block = factorial[i - 1]
19
20            index = k // block
21
22            result += numbers[index]
23
24            numbers.pop(index)
25
26            k = k % block
27
28        return result