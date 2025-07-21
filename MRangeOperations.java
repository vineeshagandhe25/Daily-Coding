/*Given:

An integer n — the size of an array (initially all zeros, 1-indexed).

A list of m operations. Each operation is given as [a, b, k], meaning:

Add integer k to every element from index a to b inclusive.

Task: After performing all m operations, return the maximum value in the array */
public class MRangeOperations {

    long arrayManipulation(int n, int[][] queries) {
        long[] arr = new long[n + 2];
        for (int i = 1; i < n + 2; i++)
            arr[i] = 0;

        for (int[] q : queries) {
            int a = q[0];
            int b = q[1];
            long k = q[2];
            arr[a] += k;
            if (b + 1 < arr.length) {
                arr[b + 1] -= k;
            }
        }
        long cur = 0, maxVal = 0;
        for (int i = 0; i < n + 1; i++) {
            cur += arr[i];
            maxVal = Math.max(maxVal, cur);
        }
        return maxVal;
    }

    public static void main(String[] args) {
        MRangeOperations obj = new MRangeOperations();

        int n = 5;
        int[][] queries = {
            {1, 2, 100},
            {2, 5, 100},
            {3, 4, 100}
        };

        long result = obj.arrayManipulation(n, queries);
        System.out.println("Maximum value after operations: " + result);
    }
}
