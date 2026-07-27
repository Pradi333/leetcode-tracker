# Last updated: 7/27/2026, 10:30:35 AM
1class Solution:
2    def trap(self, height):
3        if not height:
4            return 0
5
6        left = 0
7        right = len(height) - 1
8
9        left_max = 0
10        right_max = 0
11
12        water = 0
13
14        while left < right:
15            if height[left] <= height[right]:
16
17                if height[left] >= left_max:
18                    left_max = height[left]
19                else:
20                    water += left_max - height[left]
21
22                left += 1
23
24            else:
25
26                if height[right] >= right_max:
27                    right_max = height[right]
28                else:
29                    water += right_max - height[right]
30
31                right -= 1
32
33        return water