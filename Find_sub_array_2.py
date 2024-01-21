#Given an array [15,-1,2,5,8], find subarray(any size) with sum=15
arr = [-1, -2, -3, 8]
key = 5
res = False
i = 0

while i < len(arr):
    sum = 0
    if arr[i] == key:
        res = True
        break
    else:
        j = i
        while j < len(arr):
            sum += arr[j]
            if sum == key:
                res = True
                break
            j += 1
    i +=1

print(res)