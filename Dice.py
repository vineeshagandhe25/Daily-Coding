'''
Input:
N: integer- number of dices
M: integer- number of faces on each dice
X: integer- The target sum.
Output: 
An integer that represents number of ways to achieve the sum X when all N dice are rolled '''

def num_ways(N, M, X):
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, X + 1):
            for k in range(1, min(j, M) + 1):
                dp[i][j] += dp[i - 1][j - k]

    return dp[N][X]

N = 3  
M = 6  
X = 7  
result = num_ways(N, M, X)
print(result)