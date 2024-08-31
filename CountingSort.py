# Counting Sort 
def countingSort(array):
    if not array:  # condition for empty array
        return  
    
    max_val = max(array) # max value in array
    
    count = [0] * (max_val + 1) # count array to count frequencies of num in input array
    output = [0] * len(array)   # output array 
    
    for num in array:  # Time Complexity -- O(N) where N is length of array
        # finding frequency of every num in array
        count[num] += 1
    
    for i in range(1, len(count)):  # Time Complexity -- O(M) where M is largest num in array
        # for cummulative count
        count[i] += count[i - 1]
    
    for num in reversed(array):   # Time Complexity -- O(N) where N is length of array
        # arraneging nums in output array based on count array
        output[count[num] - 1] = num
        count[num] -= 1
    
    for i in range(len(array)):  # Time Complexity -- O(N) where N is length of array 
        # asigning output array to original array
        array[i] = output[i]

data = [40, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array : ")
print(data)

# Time Complexity --- O(N+M) where  N is length of array  and M is largest num in array
# Space  Complexity --- O(M) where M is largest num in array



'''Minor Suggestion:
If the input array contains negative numbers, the current implementation won't work since counting sort is generally used for non-negative integers. 
To handle negative numbers, additional modifications are required.'''