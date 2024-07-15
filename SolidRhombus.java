//Solid Rhombus Pattern
public class SolidRhombus {
    public static void main(String[] args) {
        int n = 5;
        solidRhombus(n);
    }

    public static void solidRhombus(int n){
        System.out.println("olidRhombus");
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n-i;j++){
                System.out.print(" ");    
            }
            for(int j=1;j<=n;j++){
                System.out.print("*");    
            }
            System.out.println();
        }
    }
}

// Time Complexity --- O(N^2) where N is input .
// Space Complexity --- O(1)