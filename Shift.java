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

        int iterations = arr.length/2-1;
        int i=1;
        while (i<=iterations) {
            // Shift odd-indexed elements
            for (int j = 1; j < arr.length; j += 2) {
                int newIndex = j - 2;
                if (newIndex < 0) {
                    newIndex = arr.length + newIndex; // Circular shift for negative index
                }
                res[newIndex] = arr[j];
            }

            // Shift even-indexed elements right by 2 positions (circular shift)
            for (int j = 0; j < arr.length; j += 2) {
                int newIndex = j + 2;
                if (newIndex >= arr.length) {
                    newIndex = newIndex - arr.length; // Circular shift for exceeding index
                }
                res[newIndex] = arr[j];
            }

            for (int k = 0; k < res.length; k++) {
                arr[k] = res[k];
            }
            i += 1;
        }
        
        for (int k = 0; k < res.length; k++) {
            System.out.print(arr[k] + " ");
        }
    }
}
// Time Complexity --- O(N) where N is length of array.
// Space Complexity ---O(N) where N is length of array.