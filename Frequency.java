/* A user enters integers until end of input and wants to find the largest number in the 
list of integers entered and the number of times it was entered. For example, if the 
input is 5, 2, 15, 3, 7, 15, 8, 9, 5, 2, 15, 3, and 7, the largest is 15 and is repeated 3 
times. Write an algorithm to compute frequency of the largest of the integers 
entered without storing them. Convert the algorithm to a function that displays the 
integers read and returns the largest number and its frequency */

import java.util.*;

public class Frequency {

    public static void main(String[] args) {

        int frequency = 0;
        int largest = Integer.MIN_VALUE; // To handle any range of input, even negative number
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("enter the number ");
            int x = sc.nextInt();

            if (x > largest) {
                largest = x; // Update largest number
                frequency = 1; // Reset frequency for the new largest number
            }

            else if (x == largest)
                frequency += 1; // Increment frequency for the current largest

            System.out.println("enter any number to continue and 0 to stop");
            int choice = sc.nextInt();
            if (choice == 0)
                break;
        }
        System.out.println("Largest number is " + largest + " and its frequency is " + frequency);

        sc.close();
    }
}
// Time Complexity --- O(n) where n is the number of integers entered.
// Space Complexity --- O(1).
