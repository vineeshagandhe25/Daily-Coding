''' Given a sorted array A of size n and a number k, return the number of unique pairs which have a difference of k.
|arr[i] - arr[j]| = k where i < j
A: [1, 3, 5, 7, 10]
k: 2
Answer: 3'''

'''Answer: This problem is solved using hashing concept.
Sets are often used in situations where you need to quickly test for membership or eliminate duplicates from a collection.
In Python, the underlying data structure of a set is a hash table (also known as a hash map). 
This data structure is optimized for fast lookup, insertion, and deletion of elements. 
Each element in the set is hashed, and the hash value is used to determine the location in memory where the element is stored.'''

def findPairs(arr,k):

    n=len(arr)  # Time Complexity of len() is O(1)
    hashset=set(arr)  # Time Complexity of set() is O(n) (as we are passing n iterable eles)
    res=0
    if k == 0:
        return 
    
    # The time complexity of 'in' operation with sets in python is O(1) . 
    for i in range(n):  # Time Complexity --- O(n) where n is len(arr)
        if arr[i] + k  in hashset:
            res += 1

    return res 

arr=[1,2,3,4,5]         # test cases:
k=-1                    # negative k
print(findPairs(arr,k)) 
k=0                     # zero input
print(findPairs(arr,k))
k=1                     # general input 
print(findPairs(arr,k))
arr=[1,3,5,7,10]        # given input
k=2
print(findPairs(arr,k))
arr=[1,2,3,4,5]         
k=6                    # non exists k value
print(findPairs(arr,k)) 
arr=[]                 # empty array 
k=-1                   
print(findPairs(arr,k)) 
arr=[1]                 # single valued array 
k=-1                   
print(findPairs(arr,k))

# * Time Complexity --- O(n) where n is length of input arr.
# * Space  Complexity --- O(n) where n is length of input arr.