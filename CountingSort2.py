# Counting Sort  
def countingSort(array):
    if not array:
        return  
    
    max_val = max(array)
    exp = 1  # We start from the least significant digit
    
    while max_val // exp > 0:
        # Initialize count array for digits 0 to 9
        count = [0] * 10
        output = [0] * len(array)

        # Store count of occurrences of digits
        for num in array:
            countIndex = (num // exp) % 10
            count[countIndex] += 1

        # Change count[i] so that it contains the actual position of the digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array by placing elements in the correct position
        for num in reversed(array):
            countIndex = (num // exp) % 10
            output[count[countIndex] - 1] = num
            count[countIndex] -= 1

        # Copy the sorted elements from output array to the original array
        for i in range(len(array)):
            array[i] = output[i]

        # Move to the next significant digit
        exp *= 10


data = [40, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array : ")
print(data)


# Time Complexity: O(nlogM), where M is the maximum element in the array.
# Space Complexity: O(n).