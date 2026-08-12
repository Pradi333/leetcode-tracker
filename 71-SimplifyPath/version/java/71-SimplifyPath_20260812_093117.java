// Last updated: 8/12/2026, 9:31:17 AM
1class Solution {
2    public String simplifyPath(String path) {
3
4        Stack<String> stack = new Stack<>();
5
6        String[] parts = path.split("/");
7
8        for (String part : parts) {
9
10            // Ignore empty parts and "."
11            if (part.equals("") || part.equals(".")) {
12                continue;
13            }
14
15            // Go to parent directory
16            if (part.equals("..")) {
17                if (!stack.isEmpty()) {
18                    stack.pop();
19                }
20            }
21            else {
22                stack.push(part);
23            }
24        }
25
26        StringBuilder result = new StringBuilder();
27
28        for (String dir : stack) {
29            result.append("/").append(dir);
30        }
31
32        return result.length() == 0 ? "/" : result.toString();
33    }
34}