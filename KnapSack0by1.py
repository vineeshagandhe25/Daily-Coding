# 0/1 knapsack problem solution
def knapscak(W,wt,val,n): # parameters are total weight , weight array , coresponding profits and total no of items

    k=[[0 for i in range(W+1)]for i in range(n+1)]  

    for i in range(n+1): # Time Complexity --- O(N) where N is the length of weight array

        for j in range(W+1):  # Time Complexity --- O(M) where M is W+1 

            if i == 0 or j == 0:
                k[i][j]=0
            elif wt[i-1] <= j :
                k[i][j]=max(val[i-1]+k[i-1][j-wt[i-1]],k[i-1][j])
            else:
                k[i][j]=k[i-1][j]

    return k[n][W]

print(knapscak(8,[2,3,4,5],[1,2,5,6],4))

# Time Complexity --- O(N*M) where N is the length of weight array and M is capacity of knapsack.

