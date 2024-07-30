// Finding Maximum number
public class Maximum {
    public static void main(String[] args) {
        // Example usage
        int num1 = 5;
        int num2 = 10;
        int max = findMax(num1, num2);
        System.out.println("The maximum of " + num1 + " and " + num2 + " is " + max);
        // Testing Edge Cases
        System.out.println(findMax(3,2));
        System.out.println(findMax(2,2));
        System.out.println(findMax(-1,-2));
    }

    public static int findMax(int a, int b) {
        return (a + b + Math.abs(a - b)) / 2; 
    }
}
