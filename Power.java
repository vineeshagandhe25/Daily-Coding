/*Implement a function to calculate base  raised to exponent without using built-in functions or operators.*/
public class Power {
    public static void main(String[] args) {
        int base = 5;
        int exponent = 2;
        System.out.println(power(base, exponent));
        // Coner Cases
        System.out.println(power(base, 0));
        System.out.println(power(0, exponent));
        System.out.println(power(0, 0));
        System.out.println(power(base, 1));
        System.out.println(power(base, -2));
    }

    public static float power(int base, int exponent) {
        float result = 1;
        int limit = Math.abs(exponent);

        for (int i = 0; i < limit; i++) { // Time Complexity --- O(N) where N is value of Limit
            result *= base;
        }
        if (exponent < 0) {
            return 1 / result;
        } else {
            return result;
        }
    }
}

// Time Complexity --- O(N) where N is value of Limit.
// Space Complexity --- O(1)