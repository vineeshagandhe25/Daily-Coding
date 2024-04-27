# Optimal Binary Search Tree
def obst(keys, freq):
    n = len(keys)
    res = [[0 for _ in range(n)] for _ in range(n)]
    keys=[]

    for i in range(n):
        res[i][i] = freq[i]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            res[i][j] = float('inf')
            freq_sum = sum(freq[i:j+1])
            r=0
            for r in range(i, j + 1):
                cost = freq_sum + (res[i][r - 1] if r > i else 0) + (res[r + 1][j] if r < j else 0)
                if cost < res[i][j]:
                    res[i][j] = cost
            keys.append(r)


    return res,keys

a = [1, 2, 3, 4]
freq = [4, 2, 6, 3]
print(obst(a, freq))
