/* Given the root of a binary tree, return its depth.
The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node. */

// Max method
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) { // checking for empty no node
        return 0;
        }

        // calculating left and right subtrees depth and return max 
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
        
}

// Time Complexity ---  O(N) where N is no of nodes in given tree .
// Space Complexity ---  O(N) where N is no of nodes in given tree .

