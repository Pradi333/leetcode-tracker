# Last updated: 8/23/2026, 8:51:12 AM
1class Solution(object):
2    def findDisappearedNumbers(self, nums, lower, upper):
3        nums=sorted(set(nums))
4        result=[]
5        prev=lower
6        for x in nums:
7            if x<lower:
8                continue
9            if x>upper:
10                break
11            if prev<x:
12                result.append([prev,x-1])
13            prev =x+1
14        if prev<=upper:
15            result.append([prev,upper])
16        return result
17        
18    
19                    
20        