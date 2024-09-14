// Add two numbers without using '+' operator and subtract two numbers without using '-' operator .
public class AddSub 
{
    public static void main(String[] args) 
    {
        int num1 = 5;
        int num2 = 1;

        System.out.println("The result of addition is " + add(num1, num2));
        System.out.println("The result of subtraction is " + sub(num1, num2));
    }

    public static int add(int num1,int num2)
    {
       int carry = 0;
       while (num2 != 0) 
       { 
         carry = num1 & num2;
         num1 = num1 ^ num2;
         num2 = carry << 1 ;
       }

       return num1;
    }

    /* The code adds two integers by using bitwise operations. It computes the sum with XOR and handles the carry with AND and left-shift operations. */

    public static int sub(int num1,int num2)
    {
        int barrow = 0;
        num2 = ~num2 + 1 ;
        while (num2 != 0) 
       { 
         barrow = num1 & num2;
         num1 = num1 ^ num2;
         num2 = barrow << 1 ;
       }

       return num1;

    }

    /*The code uses bitwise operations to perform subtraction by first converting the second number (num2) to its negative form using two's complement.
     It then computes the difference using XOR for subtraction and AND for calculating the borrow, left-shifting the borrow to the next significant bit.
     Finally, the result is returned when no more borrow remains. */
}

// Time Complexity --- O(n) where n is the number of bits in the larger of the two numbers.
// Space Complexity ---O(1) 
