# Add two Binaries

arr1=[1,1]
arr2=[1]
a=b=0
for i in arr1:  # converting arr1 into number   * Time Complexity---O(l) l=len of arr1
    a=a*10+i
for i in arr2:  # converting arr2 into number   * Time Complexity --- O(k) k=len if arr2
    b=b*10+i
# converting numbers into strings    
a=str(a)
b=str(b)
# converting above binary strings into integers
a=int(a,2)
b=int(b,2)
res=bin(a+b) # result in binary using bin()
res=str(res) # converting above binary num into string 
res_arr=[]
for x in range(2,len(res)): # as res='0bbin_num' we avoid 0b by starting from index 2  * Time Complexity --- O(n) where n is len of res
    res_arr.append(int(res[x]))
print(res_arr)

# * Time Complexity --- O(l)+O(k)+O(n)=O(n)  (because n is always >= of l or k)
# * Space Complexity --- O(n)  where n is the len of res


