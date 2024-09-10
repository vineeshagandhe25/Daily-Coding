/*
Input:
N: integer- number of dices
M: integer- number of faces on each dice
X: integer- The target sum.
Output: 
An integer that represents number of ways to achieve the sum X when all N dice are rolled
 */
public class Salesforceq1 {
    
}

/*We can solve this problem using dynamic programming. The idea is to use a 2D array dp where dp[i][j] represents the number of ways to get a sum of j using i dice.

Steps:
Initialize the base case: dp[0][0] = 1, meaning there is one way to get sum 0 with 0 dice (by not rolling any dice).
For each dice, iterate over possible sums and calculate the number of ways to achieve each sum using the number of dice rolled.
The result will be stored in dp[N][X].
 */