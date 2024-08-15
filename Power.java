/*Implement a function to calculate base  raised to exponent without using built-in functions or operators.*/
public class Power {
    public static void main(String[] args) {
        int base = 5;
        int exponent = 1;
        power(base,exponent);
    }

    public static void power(int base,int exponent) {
        int result=1;
        int limit = Math.abs(exponent);
        
        for(int i=0;i<limit;i++) {
            result *= base;
        }
        if(exponent < 0) {
            System.out.println(1/result);
        }
        else {
            System.out.println(result);
        }
    }
}
