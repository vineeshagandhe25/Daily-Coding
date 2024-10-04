# Quick sort 

def quickSort(arr) :

    if len(arr) <= 1 : # Base Condition
        return arr
    
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot ]  # putting values lesser then pivot ele in left 
    Pivot = [x for x in arr if x == pivot ] # putting values equal to pivot ele in Pivot 
    right = [x for x in arr if x > pivot ] # putting values greater then pivot ele in right

    return quickSort(left) + Pivot + quickSort(right)

arr=[8,7,6,5,4,3,2,1,1]
print(quickSort(arr))

# Time Complexity --- O(nlogn) 
# Space Complexity --- O(n) 