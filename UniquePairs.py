''' Given a sorted array A of size n and a number k, return the number of unique pairs which have a difference of k.
|arr[i] - arr[j]| = k where i < j
A: [1, 3, 5, 7, 10]
k: 2
Answer: 3'''

def findPairs(arr,k):
    n=len(arr)
    hashset=set(arr)
    res=0
    if k == 0:
        return 
    for i in range(n):
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