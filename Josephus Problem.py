# JOSEPHUS PROBLEM 

def josephus(arr,k,index):

    # Base Condition --- when single person is left we stop here
    if len(arr) == 1 :
        print("The ele is",arr[0])
        return
    # finding the person to be eliminated
    index=(index+k) % len(arr)
    arr.pop(index)
    josephus(arr,k,index)
   
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
k=2
index=0
josephus(arr,k-1,index)    

# * Time Complexity --- O(n) where n is length of arr
# * Space Complexity --- O(1)