# Given an array, an integer k, find any two different indexed elements whose sum is equal to k. 

def findEles(arr, k):
    num_index = {}  #  to store indices of elements
    for i, num in enumerate(arr): # Time Compkexity --- O(N)
        if k - num in num_index:
            print(arr[num_index[k - num]], num)
            return
        num_index[num] = i

# Test Cases
arr = [1, 2, 3, 4]
k = 5
findEles(arr,k)
arr = [1, 2, 3, 4]
k = -1
findEles(arr,k)
arr = [1, -2, 3, 4]
k = -1
findEles(arr,k)
arr = [1, 2, 3, 4]
k = 2
findEles(arr,k)
arr = []
k = 5
findEles(arr,k)
# Time Compkexity --- O(N) where N is length of arr
# Space  Compkexity --- O(N) where N is length of arr

