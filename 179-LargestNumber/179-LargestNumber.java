// Last updated: 7/9/2026, 10:06:47 AM
import java.util.*;

class Solution {
    public String largestNumber(int[] nums) {
        
        String[] arr = new String[nums.length];
        
        // Convert integers to strings
        for (int i = 0; i < nums.length; i++) {
            arr[i] = String.valueOf(nums[i]);
        }
        
        // Custom sorting
        Arrays.sort(arr, (a, b) -> (b + a).compareTo(a + b));
        
        // If the largest number is 0, return 0
        if (arr[0].equals("0")) {
            return "0";
        }
        
        // Build the result
        StringBuilder sb = new StringBuilder();
        for (String s : arr) {
            sb.append(s);
        }
        
        return sb.toString();
    }
}