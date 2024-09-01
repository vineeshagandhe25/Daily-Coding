# Counting Sort  
def countingSort(array):
    if not array:
        return  
    
    max_val = max(array)
    
    count = [0] * (10)
    output = [0] * len(array)
    exp=1
    while max_val // exp >0 :
        for num in array:
            countIndex=(num//exp)%10
            count[countIndex] += 1
            
        for i in range(1, len(count)):
             count[i] += count[i - 1]

        for num in reversed(array):
             output[count[num] - 1] = num
             count[num] -= 1
    
        for i in range(len(array)):
              array[i] = output[i]
        exp *= 10      
        
        
    

data = [40, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array : ")
print(data)


# Code with error 