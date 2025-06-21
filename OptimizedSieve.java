import java.util.Scanner;

public class OptimizedSieve {
    public static void optimizedSieve(int n) {
        // Step 1: Create a boolean array and eliminate even numbers 
        boolean[] isPrime = new boolean[n+1];
        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }
        for(int i=4;i<=n;i+=2) {
            isPrime[i] = false;
        }

        // Step 2: Start marking non-primes
        for(int i=3;i*i<=n;i+=2) {
            if(isPrime[i]) {
                for(int j = i*i;j<=n;j+=2*i) {
                    isPrime[i] = false ;
                }
            }
        }

        // Step 3: Print all prime numbers
        System.out.println("Prime numbers up to " + n + ":");
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                System.out.print(i + " ");
            }
        }    

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of n: ");
        int n = sc.nextInt();
        optimizedSieve(n);
        sc.close();
    }
}
