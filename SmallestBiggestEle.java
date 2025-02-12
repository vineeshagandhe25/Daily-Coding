/* Write a program in java that stores 20 integers entered by a user in an array, and 
then computes the following using appropriate methods:

(i) Smallest and Biggest elements 
(ii) nth biggest and nth smallest element
(iii) Position of smallest and biggest element  */

import java.util.*;

public class SmallestBiggestEle {

    // Method to find the smallest and biggest element
    public static void findSmallBigEle(int[] array) { // Time Complexity - O(n) Space Complexity - O(1)
        int small = array[0];
        int big = array[0];

        for (int i = 1; i < array.length; i++) {
            if (array[i] < small) {
                small = array[i];
            }

            if (array[i] > big) {
                big = array[i];
            }
        }

        System.out.println("The Biggest element: " + big);
        System.out.println("The Smallest element: " + small);
    }

    // method to find nth smallest and nth biggest element
    public static void findNthBigSmallEle(int[] array, int n) { // Time Complexity - O(nlogn) (since it uses quickSort),
                                                                // Space
        // Complexity - O(logn) (due to quickSort)

        // Sorting the array
        quickSort(array, 0, array.length - 1);

        // nth smallest element
        if (n - 1 < array.length) {
            System.out.println(n + "th Smallest element: " + array[n - 1]);
        } else {
            System.out.println("Invalid 'n' for smallest element.");
        }

        // nth biggest element
        if (n - 1 < array.length) {
            System.out.println(n + "th Biggest element: " + array[array.length - n]);
        } else {
            System.out.println("Invalid 'n' for biggest element.");
        }

    }

    // quick sort
    // Time Complexity: O(nlogn) (average case) O(n²) (worst case)
    // Space Complexity: O(logn) (for recursion stack)

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int i = low;
        int j = high;

        while (i < j) {

            while (i < high && arr[i] <= pivot) {
                i++;
            }

            while (arr[j] > pivot) {
                j--;
            }

            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        arr[low] = arr[j];
        arr[j] = pivot;

        return j;
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {

            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void findBigSmallPosition(int[] array) { // Time Complexity - O(n) Space Complexity - O(1)
        int small_pos = 0, big_pos = 0;

        for (int i = 1; i < array.length; i++) {

            if (array[small_pos] > array[i]) {
                small_pos = i;
            }

            if (array[big_pos] < array[i]) {
                big_pos = i;
            }
        }

        System.out.println("The Biggest element position : " + big_pos);
        System.out.println("The Smallest element position : " + small_pos);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int array[] = new int[20];
        for (int i = 0; i < 20; i++) {
            array[i] = sc.nextInt();
        }

        System.out.println("Smallest and Biggest elements :");
        findSmallBigEle(array);
        System.out.println("Smallest and Biggest elements positions are :");
        findBigSmallPosition(array);
        System.out.println("N th biggest and smallest elements :");
        System.out.println("Enter value for n to find nth biggest and smallest elements:");
        int n = sc.nextInt();
        findNthBigSmallEle(array, n);
        sc.close();
    }

}

// Time Complexity --- O(nlogn) where n is length of given array.
// Space Complexity --- O(logn) where n is length of given array.
