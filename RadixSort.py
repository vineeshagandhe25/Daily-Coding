# Radix Sort 
arr=[646,749,56,8,846,74] # input array
bkts=[[],[],[],[],[],[],[],[],[],[]]  # bucktes(0-9)
maxValue=max(arr)  # maximum value in array
r=1 
while maxValue // r > 0:
    while len(arr) > 0:
        val=arr.pop()
        radixIndex = (val // r) % 10
        bkts[radixIndex].append(val)
    for bucket in bkts:
        while len(bucket) > 0:
            val = bucket.pop()
            arr.append(val)
    r*=10

print("Sorted Array ",arr)

 # Time Complexity --- O(N*d) where N is length of input array and d is number of digits in largest number of array.
 # Space Complexity --- O(N)  where N is length of input array      
