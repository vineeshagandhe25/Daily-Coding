import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
        left = null;
        right = null;
    }
}

class TreeOperations {

    public static void inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;

        while (!stack.isEmpty() || cur != null) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }

            cur = stack.pop();
            System.out.print(cur.val + " ");
            cur = cur.right;
        }
        System.out.println();
    }

    public static void preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        stack.push(cur);

        while (!stack.isEmpty()) {
            cur = stack.pop();
            System.out.print(cur.val + " ");
            if (cur.right != null)
                stack.push(cur.right);
            if (cur.left != null)
                stack.push(cur.left);
        }
        System.out.println();
    }

    public static void postorderTraversal(TreeNode root) {
        if (root == null)
            return;
        Stack<TreeNode> s1 = new Stack<>();
        Stack<TreeNode> s2 = new Stack<>();
        s1.push(root);

        while (!s1.isEmpty()) {
            TreeNode cur = s1.pop();
            s2.push(cur);
            if (cur.left != null)
                s1.push(cur.left);
            if (cur.right != null)
                s1.push(cur.right);
        }

        while (!s2.isEmpty()) {
            System.out.print(s2.pop().val + " ");
        }
        System.out.println();
    }

    public static int findHeight(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + Math.max(findHeight(root.left), findHeight(root.right));
    }

    private static int[] inorderCount(TreeNode node) {
        if (node == null)
            return new int[] { 0, 0 };

        int[] left = inorderCount(node.left);

        int[] right = inorderCount(node.right);

        int totalNodes = left[1] + right[1] + 1;
        int leafNodes = left[0] + right[0];
        
        if (node.left == null && node.right == null) {
            leafNodes++;
        }

        return new int[] { leafNodes, totalNodes };
    }

    public static void countNodes(TreeNode root) {
        int nodes = 0;
        int leafNodes = 0;
        int[] res = inorderCount(root);
        leafNodes = res[0];
        nodes = res[1];
        System.out.println("Toatl Nodes are " + nodes + " leaf nodes are " + leafNodes);

    }
}

public class BinaryTree {
    public static void main(String[] args) {

        // Manual Construction of Tree
        int rootVal = 5;
        TreeNode root = new TreeNode(rootVal);
        root.left = new TreeNode(3);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(4);
        root.right = new TreeNode(7);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(8);

        // Tree Traversals
        TreeOperations.inorderTraversal(root);
        TreeOperations.preorderTraversal(root);
        TreeOperations.postorderTraversal(root);

        System.out.println("Height of the tree is " + TreeOperations.findHeight(root));
        TreeOperations.countNodes(root);

    }
}
