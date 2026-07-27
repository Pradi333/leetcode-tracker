# Last updated: 7/27/2026, 10:19:21 AM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        # Handle overflow case
4        if dividend == -2147483648 and divisor == -1:
5            return 2147483647
6
7        negative = (dividend < 0) != (divisor < 0)
8
9        dividend = abs(dividend)
10        divisor = abs(divisor)
11
12        result = 0
13
14        while dividend >= divisor:
15            temp = divisor
16            multiple = 1
17
18            while dividend >= (temp << 1):
19                temp <<= 1
20                multiple <<= 1
21
22            dividend -= temp
23            result += multiple
24
25        if negative:
26            result = -result
27
28        # Keep result within 32-bit integer range
29        result = max(-2147483648, min(result, 2147483647))
30
31        return result