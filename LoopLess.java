// Print all numbers between 1 and 100 without using any loop .

// To print numbers between 1 and 100 we can use recursive method instead of loops .
public class LoopLess {
    public static void main(String[] args) {
        printNums(1);
    }

    public static void printNums(int num){
         
        // base condition 
        if(num == 100){
            System.out.println(num);
            return;
        }
        
        System.out.print(num+" ");
        // Recursive call
         printNums(num+1);
        
    }
}
