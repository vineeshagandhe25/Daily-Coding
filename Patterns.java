public class Patterns 
{
 public static void main(String[] args) 
 {
    int n=4;
    int m=5;
    solidRect(n, m);
    hollowRect(n,m);
    halfPyramid(n);
    invertedHalfPyramid(n);
    invertedHalfPyramid2(n);
    floydsTriangle(n);
    zeroOneTriangle(n);
 }   

 public static void solidRect(int n,int m)
 {
    System.out.println("Solid rectangle");
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            System.out.print("*");
        }
        System.out.println();
    }
 }


 public static void hollowRect(int n,int m)
 {
    System.out.println("Hollow rectangle");
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(i==1 || j==1 || i==n || j==m )
            {
                System.out.print("*");
            }
            else
            {
                System.out.print(" ");
            }
        }
        System.out.println();
    }
 }
 public static void halfPyramid(int n)
 {
    System.out.println("Half Pyramid");
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            System.out.print("*");
        }
        System.out.println();
    }
 }
 public static void invertedHalfPyramid(int n)
 {
    System.out.println("Inverted Half Pyramid");
    for(int i=n;i>=1;i--)
    {
        for(int j=1;j<=i;j++)
        {
            System.out.print("*");
        }
        System.out.println();
    }
 }
 public static void invertedHalfPyramid2(int n)
 {
    System.out.println("Inverted Half Pyramid");
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n-i;j++)
        {
            System.out.print(" ");
        }
        for(int j=1;j<=i;j++)
        {
            System.out.print("*");
        }
        System.out.println();
    }

 }
 public static void floydsTriangle(int n)
 {
    System.out.println("Floyd's Triangle");
    int num=1;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            System.out.print(num+" ");
            num++;
        }
        System.out.println();
    }
 }
 public static void zeroOneTriangle(int n)
 {
    System.out.println("Zero One Triangle");
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            int sum=i+j;
            if(sum % 2 == 0)
            {
                System.out.print("1 ");
            }
            else
            {
                System.out.print("0 "); 
            }
        }
        System.out.println();
    }
 }
}
