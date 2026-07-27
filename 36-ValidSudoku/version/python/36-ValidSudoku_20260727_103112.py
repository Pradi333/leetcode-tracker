# Last updated: 7/27/2026, 10:31:12 AM
1class Solution:
2    def multiply(self, num1, num2):
3        if num1 == "0" or num2 == "0":
4            return "0"
5
6        result = [0] * (len(num1) + len(num2))
7
8        # Multiply each digit
9        for i in range(len(num1) - 1, -1, -1):
10            for j in range(len(num2) - 1, -1, -1):
11
12                n1 = ord(num1[i]) - ord('0')
13                n2 = ord(num2[j]) - ord('0')
14
15                product = n1 * n2
16
17                pos1 = i + j
18                pos2 = i + j + 1
19
20                total = product + result[pos2]
21
22                result[pos2] = total % 10
23                result[pos1] += total // 10
24
25        # Convert list to string
26        answer = ""
27
28        for digit in result:
29            if answer == "" and digit == 0:
30                continue
31
32            answer += str(digit)
33
34        return answer