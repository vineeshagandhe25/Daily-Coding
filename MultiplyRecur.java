//Multiplication  using Recursion . 
public class MultiplyRecur {
    public static void main(String[] args) {
        int a = 5;
        int b = 3;
        System.out.println(multiply(a, b));
        // Corner Cases
        System.out.println(multiply(3, 1));
        System.out.println(multiply(a, 0));
    }

    public static int multiply(int a, int b) {
        if (b == 1) {
            return a;
        }

        if (a == 0 || b == 0) {
            return 0;
        }

        a = a + a;
        return (multiply(a, b - 1));

    }
}

// Code is incorrect for some test cases. 
