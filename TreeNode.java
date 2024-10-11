/* You are given the root of a binary tree root. Invert the binary tree and return its root. */

//Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) { // checking for empty node .
            return root;
        }
        // swapping left and right children of node
        TreeNode temp = root.left;   
        root.left = root.right;
        root.right = temp;
        // recursivly applying on left and right of node .
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}

// Time Complexity ---  O(N) where N is no of nodes in given tree .
// Space Complexity ---  O(N) where N is no of nodes in given tree .
