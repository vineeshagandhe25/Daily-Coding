# Merge  two sorted arrays, without using extra space, sort them . 

# Merge function
def merge(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
                k=j
                while k < len(arr2)-1 and arr2[k]>arr2[k+1]:  # resorting arr2
                    arr2[k],arr2[k+1]=arr2[k+1],arr2[k]
                    k += 1
            
    print("array 1:", arr1)
    print("array 2:", arr2)

arr1 = [8,9,10,11]
arr2 = [2, 4, 6]
merge(arr1,arr2)
                           # Test Cases
arr1=[1,3,5]                # arrs of same size
arr2=[2,4,6]
merge(arr1,arr2)
arr1=[1,3,5]                # arrs of different sizes
arr2=[2,4,6,7,8]
merge(arr1,arr2)
arr1=[]                     # empty arrs 
arr2=[]
merge(arr1,arr2)
arr1=[1,2,3]                #  same arrs 
arr2=[1,2,3]
merge(arr1,arr2)   
arr1=[1]                    # arrs of same size
arr2=[2]
merge(arr1,arr2)  
arr1=[1]                    # same arrs with sinlge ele
arr2=[1]
merge(arr1,arr2)
                
# * Time Complexity --- O(N*M) where N is length of arr1 and M is length of arr2
# * Space Complexity --- O(1)     
