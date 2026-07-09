// Last updated: 7/9/2026, 10:06:58 AM
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Set<Character> set = new HashSet<>();
        
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {

            char c = s.charAt(right);

            while (set.contains(c)) {
                set.remove(s.charAt(left));
                left++;
            }

            set.add(c);

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}