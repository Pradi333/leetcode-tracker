# Last updated: 9/6/2026, 9:21:28 AM
1class Solution(object):
2    def countGoodRotations(self, nums):
3        n=len(nums)
4        half=n//2
5        total=sum(nums)
6        window=sum(nums[:half])
7        ans =0
8        for i in range(n):
9            if window >total-window:
10                ans+=1
11            window-=nums[i]
12            window+=nums[(i+half)%n]
13        return ans
14        