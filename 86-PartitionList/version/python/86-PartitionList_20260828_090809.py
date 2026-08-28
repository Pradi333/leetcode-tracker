# Last updated: 8/28/2026, 9:08:09 AM
1class Solution:
2    def partition(self, head, x):
3
4        small_dummy = ListNode(0)
5        large_dummy = ListNode(0)
6
7        small = small_dummy
8        large = large_dummy
9
10        while head:
11            if head.val < x:
12                small.next = head
13                small = small.next
14            else:
15                large.next = head
16                large = large.next
17
18            head = head.next
19
20        large.next = None
21        small.next = large_dummy.next
22
23        return small_dummy.next