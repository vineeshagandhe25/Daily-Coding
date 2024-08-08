/* Problem Statement -:

In an airport, the Airport authority decides to charge a minimum amount to the passengers who are carrying luggage with them. 
They set a threshold weight value, say, T, if the luggage exceeds the weight threshold you should pay double the base amount. 
If it is less than or equal to threshold then you have to pay $1.   */

import java.util.*;

public class Luggage {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int weights[] = new int[n];
        for (int i = 0; i < n; i++)
            weights[i] = sc.nextInt();
        int t = sc.nextInt();
        System.out.println(weightMachine(n, weights, t));
        sc.close();
    }

    static int weightMachine(int N, int weights[], int T) {
        int amount = 0, i;
        for (i = 0; i < N; i++) { // Time Complexity --- O(N)
            amount++;
            if (weights[i] > T) {
                amount++;
            }
        }
        return amount;
    }
}

// Time Complexity --- O(N) where N is the length of weights array.
// Space Complexity --- O(1)