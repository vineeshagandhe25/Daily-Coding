# The input is given in array format add 1 to that num and res must be array

arr=[1,2,3]
num=0
for i in arr:
    num=num*10+i
res=num+1
res_arr=[]
while res>0:
    r=res%10
    res_arr.insert(0,r)
    res=res//10
print(res_arr)