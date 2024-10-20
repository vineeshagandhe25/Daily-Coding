/* Write a menu driven program (using switch case) to do following operation on two 
dimensional array of size m x n. You should use methods which accept 2-D array 
and its size m and n as arguments. The options are:

i. To input elements into matrix of size m x n
ii. To display elements of matrix of size m x n
iii. Sum of all elements of matrix of size m x n
iv. To display row-wise sum of matrix of size m x n
v. To display column-wise sum of matrix of size m x n
vi. To create transpose of matrix B of size n x m */

import java.util.*;

public class Matrix {

    // method to input elements into matrix
    static void input(int[][] matrix,int m,int n) {
        
        Scanner sc = new Scanner(System.in);
        for(int i=0;i<m;i++) {  // Time Complexity --- O(m*n)   Space Complexity --- O(1) 
            for(int j=0;j<n;j++) {
                System.out.println("enter ele :");
                matrix[i][j]=sc.nextInt();
            }
        }
    }

    // method to display elements of matrix
    static void display(int[][] matrix,int m,int n) {

        for(int i=0;i<m;i++) {  // Time Complexity --- O(m*n)    Space Complexity --- O(1)
            for(int j=0;j<n;j++) {
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
    }

    // method to perform sum of all elements of matrix 
    static void sumOfEles(int[][] matrix,int m,int n) {
        
        int sum=0;
        for(int i=0;i<m;i++) {  // Time Complexity --- O(m*n)    Space Complexity --- O(1)
            for(int j=0;j<n;j++) {
                sum += matrix[i][j];
            }
        }
        System.out.println("Sum of all eles :"+sum);
    }

    // method to display row-wise sum of matrix 
    static void sumOfRowWise(int[][] matrix,int m,int n) {
        int sum=0;
        for(int i=0;i<m;i++) {  // Time Complexity --- O(m*n)    Space Complexity --- O(1)
            for(int j=0;j<n;j++) {
                sum += matrix[i][j];
            }
            System.out.println(i+" th row-wise sum : "+sum);
            sum=0;
        }
    }

    // method to display col-wise sum of matrix 
    static void sumOfColWise(int[][] matrix,int m,int n) {
        int sum=0;
        for(int i=0;i<n;i++) {  // Time Complexity --- O(m*n)   Space Complexity --- O(1) 
            for(int j=0;j<m;j++) {
                sum += matrix[j][i];
            }
            System.out.println(i+" th col-wise sum : "+sum);
            sum=0;
        }
    }

    // method to create transpose of matrix 
    static void transpose(int[][] matrix,int m,int n) {

        int[][] transpose_matrix = new int[n][m];

        for(int i=0;i<m;i++) {  // Time Complexity --- O(m*n)    Space Complexity --- O(n*m)
            for(int j=0;j<n;j++) {
                transpose_matrix[j][i]=matrix[i][j];
            }
        }

        // Display the transposed matrix
        System.out.println("Transpose of the matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(transpose_matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        
        int[][] matrix;
        Scanner sc = new Scanner(System.in);
        int m,n;
        System.out.println("enter no of rows :");
        m=sc.nextInt();
        System.out.println("enter no of cols :");
        n=sc.nextInt();
        matrix=new int[m][n];

        // to handle 0 or negative sizes 
        if (m <= 0 || n <= 0) {
            System.out.println("Invalid Inputs");
            System.exit(0);
        }
        while (true) {
            // User menu
            System.out.println("Menu:");
            System.out.println("1. Input elements into matrix");
            System.out.println("2. Display matrix");
            System.out.println("3. Sum of all elements");
            System.out.println("4. Row-wise sum");
            System.out.println("5. Column-wise sum");
            System.out.println("6. Transpose of matrix");
            System.out.println("\n enter your option ");
            
            int option = sc.nextInt();

            switch (option) {
                case 1:
                    input(matrix, m, n);
                    break;
                case 2:
                    display(matrix, m, n);
                    break;
                case 3:
                    sumOfEles(matrix, m, n);
                    break;
                case 4:
                    sumOfRowWise(matrix, m, n);
                    break;
                case 5:
                    sumOfColWise(matrix, m, n);
                    break;
                case 6:
                    transpose(matrix, m, n);
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
            System.out.println("If you want to continue enter any number or else enter 0 to exit");
            int choice = sc.nextInt();
            if(choice == 0) {
                break;
            }
        }
        sc.close();
    }
}

// Time Complexity --- O(m*n) where m is no of rows and n is no of cols.
// Space Complexity --- O(m*n) where m is no of rows and n is no of cols.