# Last updated: 8/16/2026, 8:49:27 AM
1class Solution(object):
2    def maximumGap(self, skill, station):
3       n=len(skill)
4       m=len(station)
5       left=[0]* n
6       right=[0]* n
7       j= 0
8       for i in range(n):
9           while station[j]!=skill[i]:
10               j+=1
11           left[i]=j
12           j+=1
13       j=m-1
14       for i in range(n-1,-1,-1):
15            while station[j]!=skill[i]:
16                j-=1
17            right[i]=j
18            j-=1
19       ans=0
20       for i in range(n-1):
21           ans=max(ans,right[i+1]-left[i])
22       return ans
23        