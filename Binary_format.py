#Q:Given an integer n, find its binary format and store it in an array.
num=1234567890
arr=[]
while num>0:
    r=num%2
    arr.append(r)
    num=num//2
#In arr the binary digits are stored in reverse order so to get correct order we using res_arr
res_arr=[0]*len(arr) 
j=0
for i in range(len(arr)-1,-1,-1):
    res_arr[i]=arr[j]
    j+=1
print(res_arr)