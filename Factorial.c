#include <stdio.h>

// Function to calculate factorial using recursion
int factorialRecursive(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorialRecursive(n - 1);
}

// Function to calculate factorial using iteration
int factorialIterative(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    
    int number;

    printf("Enter a positive integer: ");
    scanf("%d", &number);

    // Validate the input
    if (number < 0) {
        printf("Factorial is not defined for negative numbers.\n");
        return 1;
    }

    // Calculate factorial using iteration and recursion
    int resultIterative = factorialIterative(number);
    int resultRecursive = factorialRecursive(number);

    // Display the results
    printf("Factorial using iteration: %d\n", resultIterative);
    printf("Factorial using recursion: %d\n", resultRecursive);

    return 0;
}
