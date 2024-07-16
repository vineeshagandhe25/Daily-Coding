// Diamond Pattern
public class Diamond {
    public static void main(String[] args) {
        int n = 5;
        diamondPattern(n);
    }

    public static void diamondPattern(int n){
        System.out.println("Diamond Pattern ");
        
        // 1st part
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n-i;j++){
                System.out.print(" ");
            }
            for(int j=1;j<=2*i-1;j++){
                System.out.print("*");
            }
            System.out.println();
        }
        // 2nd part
        for(int i=n;i>=1;i--){
            for(int j=1;j<=n-i;j++){
                System.out.print(" ");
            }
            for(int j=1;j<=2*i-1;j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

// Time Complexity --- O(N^2) where N is input
// Space Complexity --- O(1)