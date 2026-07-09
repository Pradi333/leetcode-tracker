// Last updated: 7/9/2026, 10:06:15 AM
public class Solution {
    public int hammingWeight(int n) {
        
        int count = 0;

        while (n != 0) {
            count += (n & 1); // check last bit
            n >>>= 1;         // unsigned right shift
        }

        return count;
    }
}