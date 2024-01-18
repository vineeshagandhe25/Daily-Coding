'''Qsn)Given an array A, sort it using insertion sort, and find if an element x is present in it or not. Search for x using binary search. 
Write your own insertion sort function and your own binary search function. If x is present, return true, otherwise return false.'''

def insertion_sort(arr):   # insertion sort to sort the array

    for i in range(1,len(arr)):  # Time complexity is O(N^2)  and Space Complexity is O(1)
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key   

def binary_search(arr,first,last,x): # Binary search to search ele x 
    # first indicates first index and last indicates last index of an array
    while first<=last: # Time complexity is O(logN) and space complexity is O(1)
        mid=(first+last)//2
        if arr[mid]==x:   # checking if mid is == x or not
            return True  # returning true if get ele
        elif arr[mid]<x:  # if x > arr[mid] then further search in right sub arr eles from mid 
            first=mid+1
        else:       # if x < arr[mid] then further search in left sub arr eles upto mid 
            last=mid-1

    return False      #returning false if didn't  get ele  

A=[12,8,4,0,-1,3]
length=len(A)-1
find_ele=8
insertion_sort(A)
print(binary_search(A,0,length,find_ele))
find_ele=10
print(binary_search(A,0,length,find_ele))

# Time Complexity --- O(N^2)+O(logN)=O(N^2)
# Space complexity --- O(1)+O(1)=O(1)

