/* The sum of the digits of 18117 is 1+8+1+1+7 = 18. Just as we can separate the number, we can separate this sum into the last digit, 7, and the sum of all but the 
last digit, 1+8+1+1 = 11. Write a recursive function to sum the digits of a number n, add its last digit to the sum of the digits of n. 
There's one special case: if a number has only one digit, then the sum of its digits is itself */

public class SumOfDigits {

    // Recursive function to sum the digits 
    public static int sumOfDigits(int num) {

        // To Handle negative numbers
        if (num < 0 ) {
            return -1;
        } 
        
        // Base case: if the number is a single digit, return it
        if ( num < 10) {
            return num ;
        }

        // Recursive case: add the last digit to the sum of the digits of the rest of the number
        return num % 10 + sumOfDigits(num/10) ;
    }
    public static void main(String[] args) {
        int number = 18117;
        int result = sumOfDigits(number);
        System.out.println("The sum of the digits of " + number + " is: " + result);
       
        // Corner cases 
        number = -123;
        result = sumOfDigits(number);
        System.out.println("The sum of the digits of " + number + " is: " + result);

        number = 1;
        result = sumOfDigits(number);
        System.out.println("The sum of the digits of " + number + " is: " + result);

        number = 0;
        result = sumOfDigits(number);
        System.out.println("The sum of the digits of " + number + " is: " + result);
    }
}

// Time Complexity --- O(N) where N is the no of digits in given number .
// Space Complexity --- O(N) where N is the no of digits in given number .