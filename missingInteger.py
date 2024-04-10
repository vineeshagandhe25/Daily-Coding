# Find the missing number in an array of integers ?

def find(arr):
    n=len(arr) + 1
    total_sum=(n*(n+1))//2
    array_sum=sum(arr)
    missing_num=total_sum - array_sum 
    return missing_num

arr=[1,2,4,5,6]
print("The missing num is ",find(arr))

