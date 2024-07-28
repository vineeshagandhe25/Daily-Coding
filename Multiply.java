// Multiply two numbers without using multiplication operator (*).

public class Multiply {
    public static void main(String[] args) {
        int num1=10;
        int num2=20;
        int res=multiply(num1, num2);
        System.out.println("Multiplication of "+num1+" and "+num2+" is "+res);

        // Testing Edge Cases
        System.out.println(multiply(0, 0));
        System.out.println(multiply(5, -3));
        System.out.println(multiply(-5,3));
        System.out.println(multiply(-5, -3));
        System.out.println(multiply(5, 0));
        System.out.println(multiply(0, 3));
    }
 
    public static int  multiply(int num1,int num2){  // making num2 recursive calls.
   
        if(num2==0){
            return 0;
        }

        else if(num2 >0){  // logic --- adding num1 for num2 times 
            return num1+multiply(num1, num2-1);
        }
        else{
            return -multiply(num1, -num2);
        }
    }
}

// Time Complexity --- O(N) where N is num2
// Space Complexity --- O(N) where N is num2 (due to the recursive call stack)