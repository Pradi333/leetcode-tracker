// Last updated: 8/12/2026, 9:25:00 AM
1public class Solution {
2    public ListNode detectCycle(ListNode head) {
3
4        ListNode slow = head;
5        ListNode fast = head;
6
7        // Step 1: Detect whether a cycle exists
8        while (fast != null && fast.next != null) {
9            slow = slow.next;
10            fast = fast.next.next;
11
12            if (slow == fast) {
13                break;
14            }
15        }
16
17        // No cycle
18        if (fast == null || fast.next == null) {
19            return null;
20        }
21
22        // Step 2: Find the starting node of the cycle
23        slow = head;
24
25        while (slow != fast) {
26            slow = slow.next;
27            fast = fast.next;
28        }
29
30        return slow;
31    }
32}