res=[]
x=int(input("enter a number "))
i=1
for i in range(1,x+1):
    if(x%i==0):
        res.append(i)

print("The factors of  :",x)
print(res)