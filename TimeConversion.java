/* Write a program that converts from 24-hour notation to 12-hour notation. For example, it should convert 14:25 to 2:25 PM. The input is given as two integers. 
There should be at least three methods, one for input, one to do the conversion, and one for output. Record the AM/PM information as a value of type char, 'A' for AM 
and 'P' for PM. Include a loop that lets the user repeat this computation for new input values again and again until the user wants to quit. */

import java.util.*;

public class TimeConversion {

    int hour = 0;
    int minutes = 0;
    char period = 'A'; // A for AM, P for PM

    // input function to take input
    public void input() {

        Scanner input = new Scanner(System.in);

        try {
            System.out.print("Enter hour (0-23): ");
            hour = input.nextInt();
            System.out.print("Enter minutes (0-59): ");
            minutes = input.nextInt();

            // validating input
            if (hour < 0 || hour > 23 || minutes < 0 || minutes > 59) {
                System.out.println("Invalid input. Please try again.");
                return;
            }

            convert();
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter numbers only.");
            input.next(); // clear the invalid input
        }
    }

    // conerting function
    public void convert() {

        // Determine if it's AM or PM
        if (hour >= 12) {
            period = 'P'; // PM
        } else {
            period = 'A'; // AM
        }

        // Adjust hour to 12-hour format
        if (hour == 0) {
            hour = 12; // Midnight case
        } else if (hour > 12) {
            hour -= 12;
        }

        output();
    }

    // output function to print output
    public void output() {
        System.out.println(hour + ":" + minutes + period + "M");
    }

    public static void main(String[] args) {
        TimeConversion obj = new TimeConversion();
        Scanner input = new Scanner(System.in);
        try {
            while (true) {
                System.out.println("Do you want to enter the input ? If yes enter 1 else enter any key to exit !");
                int choice = input.nextInt();
                if (choice == 1) {
                    obj.input();
                }

                else {
                    System.out.println(".....Exiting.....");
                    break;
                }

            }
        } catch (InputMismatchException e) {
            System.out.println(".....Exiting.....");
        }
    }
}

// Time Complexity --- O(1)
// Space Complexity --- O(1)