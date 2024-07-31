// Finding Maximum number without using conditional statement. 
public class Maximum {
    public static void main(String[] args) {
        // Example usage
        int num1 = 5;
        int num2 = 10;
        int max = findMax(num1, num2);
        System.out.println("The maximum of " + num1 + " and " + num2 + " is " + max);
        // Testing Edge Cases
        System.out.println(findMax(3, 2));
        System.out.println(findMax(2, 2));
        System.out.println(findMax(-1, -2));
    }

    public static int findMax(int a, int b) {
        return (a + b + Math.abs(a - b)) / 2;
    }
}

/*
 * Mathematical Explanation
 * To understand why this formula works mathematically, let's analyze it through
 * algebraic manipulation.
 * Case 1: a ≥ b
 * Initial Values: a is greater than or equal to b .
 * Absolute Difference: Math.abs(a−b)=a−b.
 * Expression: a+b+(a−b)=2a.
 * Division: 2a/2=a.
 * 
 * Case 2: a < b
 * Initial Values: b is greater than a.
 * Absolute Difference: Math.abs(a−b)=b−a.
 * Expression: a+b+(b−a)=2b.
 * Division: 2b/2=b.
 * 
 */