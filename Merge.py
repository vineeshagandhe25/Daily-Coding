# Qns Merge two sorted arrays into a single sorted array. 

# Merge function
def merge(arr1,arr2):
    i=j=k=0  # indeies for arr1 arr2 res_arr respectively
    length1=len(arr1)  # length of arr1
    length2=len(arr2)  # length of arr2
    res_arr=[0]*(length1+length2)  # resultant array

    while i < length1 and j < length2 :
        if arr1[i] < arr2[j]:
            res_arr[k]=arr1[i]
            i += 1
        else:
            res_arr[k]=arr2[j]
            j += 1   
        k += 1

    while i < length1 :
        res_arr[k]=arr1[i]
        i += 1
        k += 1    

    while j < length2 :
        res_arr[k]=arr2[j]
        j += 1
        k += 1     

    return res_arr
                            # Test Cases
arr1=[1,3,5]                # arrs of same size
arr2=[2,4,6]
print(merge(arr1,arr2))
arr1=[1,3,5]                # arrs of different sizes
arr2=[2,4,6,7,8]
print(merge(arr1,arr2))
arr1=[]                     # empty arrs 
arr2=[]
print(merge(arr1,arr2))
arr1=[1,2,3]                #  same arrs 
arr2=[1,2,3]
print(merge(arr1,arr2))   
arr1=[1]                    # arrs of same size
arr2=[2]
print(merge(arr1,arr2))  
arr1=[1]                    # same arrs with sinlge ele
arr2=[1]
print(merge(arr1,arr2))

# * Time Complexity --- O(N) where N is length of max(len(arr1,arr2))
# * Space Complexity --- O(M) where M is length of res_arr(that is len(arr1)+len(arr2))

