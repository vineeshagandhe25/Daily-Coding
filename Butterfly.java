// Butterfly Pattern

public class Butterfly {
    public static void main(String[] args) {
        int n=4;
        butterflyPattern(n);
    }

    public static void butterflyPattern(int n)
    {
        System.out.println("Butterfly Pattern ");

        // upper half
        for(int i=1;i<=n;i++)
        {
            // 1st part
            for(int j=1;j<=i;j++)
            {
              System.out.print("*");
            }

            // spaces
            int spaces=2*(n-i);
            for(int j=1;j<=spaces;j++)
            {
                System.out.print(" ");
            }
            
            // 2nd part
            for(int j=1;j<=i;j++)
            {
              System.out.print("*");
            }
            System.out.println();
        }

        // lowwer half
        for(int i=n;i>=1;i--)
        {
            // 1st part
            for(int j=1;j<=i;j++)
            {
              System.out.print("*");
            }

            // spaces
            int spaces=2*(n-i);
            for(int j=1;j<=spaces;j++)
            {
                System.out.print(" ");
            }
            
            // 2nd part
            for(int j=1;j<=i;j++)
            {
              System.out.print("*");
            }
            System.out.println();
        }
    }
}

// Time Complexity --- O(N^2)
// Space Complexity ---O(1)
