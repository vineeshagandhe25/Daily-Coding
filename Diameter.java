/* The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

Given the root of a binary tree root, return the diameter of the tree. */

class Solution {
    int diameter = 0; 
    public int diameterOfBinaryTree(TreeNode root) {
        getDiameter(root); 
        return diameter;
    }
     public int getDiameter(TreeNode root) {
       if (root == null) {  // for empty tree
            return 0; 
        }

        // getting left and right diameters and adding those diameter and getting max diameter .
        int leftHeight = getDiameter(root.left);
        int rightHeight = getDiameter(root.right);
        diameter = Math.max(diameter, leftHeight + rightHeight); 

        return 1 + Math.max(leftHeight, rightHeight);
     }
}

// Time Complexity --- O(N) where N is no of nodes .
// Space Complexity --- O(N) where N is no of nodes .

