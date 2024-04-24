# Optimal Binary Search Tree
def obst(keys,freq):
    n = len(keys)
    res = [[0 for _ in range(n)] for _ in range(n)]

    for gap in range(n):
        for i in range(n - gap):
            j = i + gap
            if gap == 0:
                res[i][j] = freq[i]
            else:
                res[i][j] = float('inf')
                sum_freq = sum(freq[i:j+1])
                for k in range(i, j+1):
                    cost = (res[i][k-1] if k > i else 0) + (res[k+1][j] if k < j else 0) + sum_freq
                    if cost < res[i][j]:
                        res[i][j] = cost
    return res

a = [1, 2, 3, 4]
freq = [4, 2, 6, 3]
print(obst(a,freq))