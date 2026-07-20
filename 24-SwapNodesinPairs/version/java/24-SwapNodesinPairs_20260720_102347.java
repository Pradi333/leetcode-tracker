// Last updated: 7/20/2026, 10:23:47 AM
1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12    public ListNode swapPairs(ListNode head) {
13        ListNode dummy = new ListNode(0);
14        dummy.next = head;
15
16        ListNode prev = dummy;
17
18        while (prev.next != null && prev.next.next != null) {
19            ListNode first = prev.next;
20            ListNode second = first.next;
21
22            // Swap
23            first.next = second.next;
24            second.next = first;
25            prev.next = second;
26
27            // Move to the next pair
28            prev = first;
29        }
30
31        return dummy.next;
32    }
33}