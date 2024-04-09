'''  1. Array Reduction 3
Given an array arr of n integers, a sequence of n-1 operations must be performed on the array.
In each operation,
• Remove the minimum and maximum elements from the current array and add their sum back to the array.
• The cost of an operation, cost = ceil((minimum_element +
maximum_element)/
(maximum_element-minimum_element
+ 1)).
Find the total cost to reduce the array to
a single element. '''
import math
def arrayReduction(arr):
    n=len(arr)  # Time Complexity of len() -- O(1)
    operations=1
    cost=0
    while operations < n :  # Time Complexity -- O(N) where N is length of arr
        max_ele=max(arr)    # Time Complexity of max() -- O(N) * N
        min_ele=min(arr)    # Time Complexity of min() -- O(N) * N
        arr.remove(max_ele) # Time Complexity of remove() -- O(N) * N
        arr.remove(min_ele) # Time Complexity of remove() -- O(N) * N
        arr.append(max_ele+min_ele)  # Time Complexity of append() -- O(1) 
        cost += math.ceil( (min_ele + max_ele) /  (max_ele - min_ele) )  # cost of an operation
        operations += 1
    print(arr)
    return cost

# input
arr=[1,2,3,4,5,6,7]
print(arrayReduction(arr))
# * Time Complexity --- O(N^2) where N is length of arr
# * Space Complexity---O(1) 