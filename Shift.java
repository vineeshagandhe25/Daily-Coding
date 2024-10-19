/* Given an array of 10 two-digit numbers, develop a program that does the following:
The elements in the even position should be shifted right (circular shift) by two 
positions and the elements in the odd position should be shifted left (circular shift) 
by two positions.
INPUT : 
12 23 71 34 92 43 12 67 72 88
OUTPUT:
71 88 92 23 12 34 72 43 12 67  */

public class Shift {

    public static void main(String[] args) {

        int[] arr = { 12, 23, 71, 34, 92, 43, 12, 67, 72, 88 };
        int[] res = new int[10];

        // for even index elements
        for (int i = 0; i < arr.length; i += 2) { // Time Complexity --- O(N)
            int newIndex = i + 2;
            if (newIndex >= arr.length) {
                newIndex = newIndex - arr.length;    // Circular shift
            }
            res[newIndex] = arr[i];
        }

        // for odd index elements
        for (int i = 1; i < arr.length; i += 2) { // Time Complexity --- O(N)
            int newIndex = i - 2;
            if (newIndex < 0) {
                newIndex = arr.length + newIndex;  // Circular shift
            }
            res[newIndex] = arr[i];
        }

        for (int i = 0; i < res.length; i++) {
            System.out.print(res[i] + " ");
        }
    }
}
// Time Complexity --- O(N) where N is length of array.
// Space Complexity ---O(N) where N is length of array.