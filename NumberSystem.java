
/*Problem Statement  :

Suppose you are in a number system, where if the number doesn’t contain 2 in the unit digit then the number is not valid. So the first number of the number system is 2, the second number is 12, and the third is 22.
for a given integer n, you have to print the nth element of the number system.

Input Format:
First line, containing n denoting the number of test cases.
then n number of lines for the query.

Output Format:
Print the consecutive number in the number system for each query.

Sample Input:
3

Sample Output:
22

Explanation:
1st number will be 2 , 2nd number will be 12 and third number will be 32 */
import java.util.*;

public class NumberSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println((n - 1) * 10 + 2);
        scanner.close();
    }
}

// Time Complexity --- O(1)
// Space Complexity --- O(1)