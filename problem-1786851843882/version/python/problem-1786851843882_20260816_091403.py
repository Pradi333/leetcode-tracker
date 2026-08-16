# Last updated: 8/16/2026, 9:14:03 AM
1class Solution(object):
2    def nearestDrone(self, drones, target):
3        best_index=-1
4        best_distance=float("inf")
5        for i in range(len(drones)):
6            x,y,r=drones[i]
7            distance=abs(x-target[0])+abs(y-target[1])
8            if distance<=r:
9                 if distance<best_distance:
10                       best_distance=distance
11                       best_index=i
12        return best_index     
13        