def obst(keys, freq):
    n = len(keys)
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        res[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            res[i][j] = float('inf')
            freq_sum = sum(freq[i:j + 1])
            for r in range(i, j + 1):
                cost = ((res[i][r - 1] if r > i else 0) +
                        (res[r + 1][j] if r < j else 0) + freq_sum)
                if cost < res[i][j]:
                    res[i][j] = cost

    return res

keys = [1, 2, 3, 4]
freq = [4, 2, 6, 3]
print(obst(keys, freq))
