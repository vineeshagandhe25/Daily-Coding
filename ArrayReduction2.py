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
import heapq

def arrayReduction(arr):
    n=len(arr)  # Time Complexity of len() -- O(1)
    operations=1
    cost=0
    min_heap=[] 
    max_heap=[]
    for num in arr:
        heapq.heappush(min_heap,num) # creating min heap 
        heapq.heappush(max_heap,-num) # creating max heap 
        #print(min_heap," ",max_heap)

    while operations < n:  # Time Complexity -- O(N) where N is length of arr
        max_ele=-heapq.heappop(max_heap)
        min_ele=heapq.heappop(min_heap)
        newEle=max_ele+min_ele  
        heapq.heappush(min_heap,newEle)
        heapq.heappush(max_heap,-newEle)
        cost += math.ceil( (min_ele + max_ele) /  (max_ele - min_ele + 1) )  # cost of an operation
        operations += 1
    
    return cost

# input
arr=[1,2,3,4,5,6,80]
print(arrayReduction(arr))
# * Time Complexity --- O(N^2) where N is length of arr
# * Space Complexity---O(1) 