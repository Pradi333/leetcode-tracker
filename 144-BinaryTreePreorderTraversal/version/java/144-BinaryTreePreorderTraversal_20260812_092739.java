// Last updated: 8/12/2026, 9:27:39 AM
1class Solution {
2    public List<Integer> preorderTraversal(TreeNode root) {
3        List<Integer> result = new ArrayList<>();
4
5        preorder(root, result);
6
7        return result;
8    }
9
10    private void preorder(TreeNode root, List<Integer> result) {
11        if (root == null) {
12            return;
13        }
14
15        result.add(root.val);           // Root
16        preorder(root.left, result);    // Left
17        preorder(root.right, result);   // Right
18    }
19}