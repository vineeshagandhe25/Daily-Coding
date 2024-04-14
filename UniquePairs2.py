''' Given a sorted array A of size n and a number k, return the number of unique pairs which have a difference of k.
|arr[i] - arr[j]| = k where i < j
A: [1, 3, 5, 7, 10]
k: 2
Answer: 3'''

def findPairs(arr,k):

    n=len(arr)  # Time Complexity of len() is O(1)
    i=0
    j=i+1
    res=0
    
    if k == 0:
        return
    while i < j  and j < n : 
        if (arr[i] - arr[j]) == k:
            res += 1
            i += 1
            j += 1

        elif  (arr[i] - arr[j]) > k:
            i += 1
            j += 1

        else:
            j += 1      

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
