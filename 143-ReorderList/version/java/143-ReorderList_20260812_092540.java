// Last updated: 8/12/2026, 9:25:40 AM
1class Solution {
2    public List<Integer> postorderTraversal(TreeNode root) {
3        List<Integer> result = new ArrayList<>();
4
5        postorder(root, result);
6
7        return result;
8    }
9
10    private void postorder(TreeNode root, List<Integer> result) {
11        if (root == null) {
12            return;
13        }
14
15        postorder(root.left, result);   // Left
16        postorder(root.right, result);  // Right
17        result.add(root.val);           // Root
18    }
19}