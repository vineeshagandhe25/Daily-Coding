/**
 * PalindromePattern
 */
public class PalindromePattern {

    public static void main(String[] args) {
        int n = 5;
        palindromePattern(n);
        
    }

    public static void palindromePattern(int n){
        System.out.println(" Palindrome Pattern");
         for(int i=1;i<=n;i++){

            // spaces
            for(int j=1;j<=n-i;j++){
                System.out.print(" ");    
            }

            // first half
            for(int j=i;j>=1;j--){
                System.out.print(j);    
            }

            // second half
            for(int j=2;j<=i;j++){
                System.out.print(j);    
            }

            System.out.println();
         }
    }
}

// Time Complexity --- O(N) where N is input n.
// Space Complexity --- O(1) .