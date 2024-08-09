// Addition using Recursion . 
public class AddRecursive {
    public static void main(String[] args) {
        int a = 5;
        int b = 3;
        System.out.println(add(a, b));
    }

    public static int add(int a, int b) {
        if (a == 0 & b == 0) {
            return 0;
        }

        if (a == 0) {
            return b;
        }

        if (b == 0) {
            return a;
        }

        else {
            return add(a + 1, b - 1);
        }
    }
}

// Time Complexity --- O(1)
// Space Complexity --- O(1)