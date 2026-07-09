// Last updated: 7/9/2026, 10:06:13 AM
import java.util.Arrays;
class Solution {
    public long maxSum(int[] nums, int k, int mul) {
    Arrays.sort(nums);

    long ans =0;
        int curr=mul;

    for(int i=nums.length-1;i>=nums.length-k;i--){
        long normal=nums[i];
        long multiply =1l*nums[i]*curr;

        ans+=Math.max(normal,multiply);
        curr--;
    }
    return ans;   
    }
}