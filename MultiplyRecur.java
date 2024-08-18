// Multiplication  using Recursion.
public class MultiplyRecur {
    public static void main(String[] args) {
        int a = 5;
        int b = 3;
        System.out.println(multiply(a, b)); // Output: 15
        // Corner Cases
        System.out.println(multiply(3, 1)); // Output: 3
        System.out.println(multiply(a, 0)); // Output: 0
        System.out.println(multiply(-5, 3)); // Output: -15
        System.out.println(multiply(5, -3)); // Output: -15
        System.out.println(multiply(-5, -3)); // Output: 15
        System.out.println(multiply(0, -3)); // Output: 0
    }

    public static int multiply(int a, int b) {
        // Base case: if b is 0, the result is 0
        if (b == 0) {
            return 0;
        }

        // If b is negative, convert to positive and adjust the sign of the result
        if (b < 0) {
            return -multiply(a, -b);
        }

        // Recursive case: add `a` to the result of `multiply(a, b-1)`
        return a + multiply(a, b - 1);
    }
}

// Time Complexity --- O(b) where b is the second operand.
// Space Complexity --- O(b) due to the recursive call stack