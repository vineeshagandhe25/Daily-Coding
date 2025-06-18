import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("enter num ");
        int num = sc.nextInt();
        int res = 1;

        // factorial code
        for (int i = 1; i <= num; i++) {
            res *= i;
        }

        System.out.println("The Result " + res);
    }
}

// Time Complexity --- O(n) where n = num
// space Complexity --- O(1)