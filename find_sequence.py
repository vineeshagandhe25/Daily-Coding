# qsn :Given an array, return true if the array contains i,j,k such that arr[i] > arr[j] > arr[k] and j > i , k > j; 
arr=[1,2,3,4]
length=len(arr)
res=False
if length < 3:
    print("length is less than 3")
else:
    for i in range(0,length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if arr[i]>arr[j] and arr[j]>arr[k]:
                    res=True  
                    break
print(res)                  
