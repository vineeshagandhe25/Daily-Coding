# Max-Heap 

# Time Complexity --- O(log n) where n is height of heap
def heapify(arr, n, i): # constructing max heap using heapify operations.
    largest = i   # setting current ele as largest ele
    l = 2 * i + 1 # left child
    r = 2 * i + 2 # right child
    
    # max heap property --- parent root must be greater then its child roots
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    # finding if child nodes is larger and setting it as parent node
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest) # heapifying next sub tree

# inserting eles into heap.
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)


    
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max Heap : ",arr)

# inserting n elements into heap is O(nlogn).

# * Time Complexity --- O(nlogn) 
# * Space Complexity --- O(n) where n is no of eles. (for inserting operation)