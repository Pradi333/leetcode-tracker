// Last updated: 7/23/2026, 10:21:11 AM
1class Solution {
2    public int searchInsert(int[] nums, int target) {
3
4        int left = 0;
5        int right = nums.length - 1;
6
7        while (left <= right) {
8
9            int mid = left + (right - left) / 2;
10
11            if (nums[mid] == target) {
12                return mid;
13            }
14            else if (nums[mid] < target) {
15                left = mid + 1;
16            }
17            else {
18                right = mid - 1;
19            }
20        }
21
22        return left;
23    }
24}