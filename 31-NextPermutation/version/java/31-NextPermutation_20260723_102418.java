// Last updated: 7/23/2026, 10:24:18 AM
1class Solution {
2
3    public void nextPermutation(int[] nums) {
4
5        int i = nums.length - 2;
6
7        // Step 1: Find pivot
8        while (i >= 0 && nums[i] >= nums[i + 1]) {
9            i--;
10        }
11
12        // Step 2: Find successor
13        if (i >= 0) {
14            int j = nums.length - 1;
15
16            while (nums[j] <= nums[i]) {
17                j--;
18            }
19
20            swap(nums, i, j);
21        }
22
23        // Step 3: Reverse the suffix
24        reverse(nums, i + 1, nums.length - 1);
25    }
26
27    private void swap(int[] nums, int i, int j) {
28        int temp = nums[i];
29        nums[i] = nums[j];
30        nums[j] = temp;
31    }
32
33    private void reverse(int[] nums, int left, int right) {
34        while (left < right) {
35            swap(nums, left, right);
36            left++;
37            right--;
38        }
39    }
40}