# Last updated: 7/28/2026, 2:46:07 PM
1class Solution:
2    def rotateRight(self, head, k):
3        if not head or not head.next or k == 0:
4            return head
5
6        # Find length
7        length = 1
8        tail = head
9
10        while tail.next:
11            tail = tail.next
12            length += 1
13
14        # Avoid unnecessary rotations
15        k = k % length
16        if k == 0:
17            return head
18
19        # Make circular list
20        tail.next = head
21
22        # Find new tail
23        steps = length - k
24        new_tail = head
25
26        for _ in range(steps - 1):
27            new_tail = new_tail.next
28
29        # Break the circle
30        new_head = new_tail.next
31        new_tail.next = None
32
33        return new_head