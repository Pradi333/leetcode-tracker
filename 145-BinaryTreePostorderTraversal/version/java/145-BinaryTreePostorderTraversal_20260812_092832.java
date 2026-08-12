// Last updated: 8/12/2026, 9:28:32 AM
1class LRUCache {
2
3    class Node {
4        int key, value;
5        Node prev, next;
6
7        Node(int key, int value) {
8            this.key = key;
9            this.value = value;
10        }
11    }
12
13    private int capacity;
14    private HashMap<Integer, Node> map;
15    private Node head, tail;
16
17    public LRUCache(int capacity) {
18        this.capacity = capacity;
19        map = new HashMap<>();
20
21        // Dummy nodes
22        head = new Node(0, 0);
23        tail = new Node(0, 0);
24
25        head.next = tail;
26        tail.prev = head;
27    }
28
29    // Remove a node
30    private void remove(Node node) {
31        node.prev.next = node.next;
32        node.next.prev = node.prev;
33    }
34
35    // Add node just after head
36    private void add(Node node) {
37        node.next = head.next;
38        node.prev = head;
39
40        head.next.prev = node;
41        head.next = node;
42    }
43
44    public int get(int key) {
45
46        if (!map.containsKey(key)) {
47            return -1;
48        }
49
50        Node node = map.get(key);
51
52        // Move recently used node to front
53        remove(node);
54        add(node);
55
56        return node.value;
57    }
58
59    public void put(int key, int value) {
60
61        // Key already exists
62        if (map.containsKey(key)) {
63            Node node = map.get(key);
64
65            remove(node);
66
67            node.value = value;
68            add(node);
69
70            return;
71        }
72
73        // Create new node
74        Node node = new Node(key, value);
75        map.put(key, node);
76        add(node);
77
78        // Capacity exceeded
79        if (map.size() > capacity) {
80
81            Node leastRecentlyUsed = tail.prev;
82
83            remove(leastRecentlyUsed);
84            map.remove(leastRecentlyUsed.key);
85        }
86    }
87}