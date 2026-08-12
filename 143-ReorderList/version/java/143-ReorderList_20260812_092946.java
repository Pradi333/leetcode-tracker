// Last updated: 8/12/2026, 9:29:46 AM
1class Solution {
2    public void reorderList(ListNode head) {
3
4        if (head == null || head.next == null) {
5            return;
6        }
7
8        // 1. Find middle
9        ListNode slow = head;
10        ListNode fast = head;
11
12        while (fast != null && fast.next != null) {
13            slow = slow.next;
14            fast = fast.next.next;
15        }
16
17        // 2. Reverse second half
18        ListNode second = slow.next;
19        slow.next = null;
20
21        ListNode prev = null;
22
23        while (second != null) {
24            ListNode next = second.next;
25            second.next = prev;
26            prev = second;
27            second = next;
28        }
29
30        // 3. Merge two halves
31        ListNode first = head;
32        second = prev;
33
34        while (second != null) {
35            ListNode temp1 = first.next;
36            ListNode temp2 = second.next;
37
38            first.next = second;
39            second.next = temp1;
40
41            first = temp1;
42            second = temp2;
43        }
44    }
45}