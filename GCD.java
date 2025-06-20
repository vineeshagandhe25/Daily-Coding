/* Problem: Given an integer array, find the maximum GCD of all elements of the array when exactly one element is removed.
Approach:
- Use prefix and suffix GCD arrays.
- For each element, calculate GCD of the rest of the array by combining
GCD of prefix and suffix parts excluding the current element. */ 

public class GCD {

    // Function to find GCD of two numbers using the Euclidean algorithm
    public static int findGCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // Function to find maximum GCD after removing one element from the array
    public static int maxGcd(int[] arr) {
        int n = arr.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];

        // Build prefix GCD array
        prefix[0] = arr[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = findGCD(prefix[i - 1], arr[i]);
        }

        // Build suffix GCD array
        suffix[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = findGCD(suffix[i + 1], arr[i]);
        }

        int maxGCD = 0;

        // Try removing each element and calculate resulting GCD
        for (int i = 0; i < n; i++) {
            int currentGCD;

            if (i == 0) {
                currentGCD = suffix[1];  // Exclude first element
            } else if (i == n - 1) {
                currentGCD = prefix[n - 2];  // Exclude last element
            } else {
                currentGCD = findGCD(prefix[i - 1], suffix[i + 1]);  // Exclude middle element
            }

            maxGCD = Math.max(maxGCD, currentGCD);
        }

        return maxGCD;
    }

    public static void main(String[] args) {
        int[] arr = {12, 15, 18};  
        int result = maxGcd(arr);
        System.out.println("Maximum GCD after removing one element: " + result);
    }
}

// Time Complexity --- O(n logM) Prefix and suffix arrays take O(n logM) where M is the maximum element in the array.
// Space Complexity --- O(n)