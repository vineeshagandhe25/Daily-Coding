'''
Input:
N: integer- number of dices
M: integer- number of faces on each dice
X: integer- The target sum.
Output: 
An integer that represents number of ways to achieve the sum X when all N dice are rolled '''

def num_ways(N, M, X):
    dp = [[0] * (X + 1) for _ in range(M + 1)]
    dp[0][0] = 1
    if M == 0 or X == 0:
        return 0

    for i in range(1, M + 1): # Time Complexity --- O(M)
        for j in range(1, X + 1):# Time Complexity ---O(X*M)
            for k in range(1, min(j, N) + 1):
                dp[i][j] += dp[i - 1][j - k]

    return dp[M][X]

N = 6
M = 3
X = 12 
result = num_ways(N, M, X)
print(result)

# Time Complexity ---O(X*M)
# Space Complexity ---O(X*M)