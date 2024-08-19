// Find the minimum of two numbers without using any conditional statements.
public class Minimum {
    public static void main(String[] args) {
        int a = 5;
        int b = 3;
        System.out.println(findMin(a, b));
        // coner cases
        System.out.println(findMin(-1, -5));
        System.out.println(findMin(0, 0));
        System.out.println(findMin(0, -1));
        System.out.println(findMin(-2, 0));
    }

    public static int findMin(int a, int b) {
        return (a + b - Math.abs(a - b)) / 2;
    }
}

// Time Complexity --- O(1).
// Space Complexity --- O(1).