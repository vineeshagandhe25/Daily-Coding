# Optimal Binary Search Tree
def obst(keys,freq):
    n = len(keys)
    res = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    
    for i in range(n+1):
        for j in range(n+1):
            if i == j or j < i :
                res[i][j]=0
            elif i+1 == j :
                res[i][j]=freq[j-1]
    print(res)            
    for i in range(2,n+1):
        for j in range(i,n+1):
            if i == j or j < i :
                res[i][j]=0
            elif i+1 == j :
                res[i][j]=freq[j-1]
            else :
                sum=0
                for k in range(i+1,j+1):
                    sum+=freq[k-1]
                cost = float('inf')
                for k in range(i+1,j+1):
                    temp=(res[i][k-1]+res[k][j])
                    #print(k,temp)
                    if temp < cost :
                        cost= temp
                res[i][j]=cost+sum 
                #print(cost,sum)                   
    return res

a = [1, 2, 3, 4]
freq = [4, 2, 6, 3]
print(obst(a,freq))