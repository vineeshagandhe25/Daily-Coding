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
}

// Time Complexity --- O(n) where n is the number of bits in the larger of the two numbers.
// Space Complexity ---O(1) 
