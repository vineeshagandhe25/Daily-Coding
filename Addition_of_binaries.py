# Add two binaries
arr1=[1,0,1]
arr2=[1,0,0]
# making both arrays of equal size
while len(arr1)< len(arr2):   
    arr1.insert(0,0)
while len(arr2)<len(arr1):
    arr2.insert(0,0)
carry=0   # To store carry bit 
res_arr=[] 

for i in range(len(arr1)-1,-1,-1):  # Time Complexity is O(n)
    sum=arr1[i]+arr2[i]+carry
    res_arr.insert(0,sum%2)  # to obtain binary digit we use sum%2
    carry=sum//2

if carry:
    res_arr.insert(0, carry)  # assigning last carry bit

print(res_arr)

# * Time Complexity --- O(n) where n is len of an input array whose len is greater
# * Space Complexity --- O(n)  where n is the len of res_arr



    
            
