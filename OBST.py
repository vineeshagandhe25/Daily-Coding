def obst(keys, freq):
    n = len(keys)
    res = [[0 for _ in range(n + 1)] for _ in range(n + 2)]

    for i in range(n + 1):
        for j in range(n + 1):
            if i == j - 1:
                res[i][j] = freq[j - 1]

    for l in range(2, n + 2):
        for i in range(1, n - l ):
            j = i + l - 1
            res[i][j] = float('inf')
            cum_freq = sum(freq[i - 1:j])
            for r in range(i, j + 1):
                t = res[i][r - 1] + res[r + 1][j]
                if t < res[i][j]:
                    res[i][j] = t
            res[i][j] += cum_freq

    return res

a = [1, 2, 3, 4]
freq = [4, 2, 6, 3]
print(obst(a, freq))
