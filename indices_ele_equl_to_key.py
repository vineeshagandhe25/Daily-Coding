# printing indices whose eles sum is equal to given key
arr=[-6,1,2,3,4,5,6,12]
k=6
resarr=[]
for i in arr:
   x=k-i
   if x in arr:
       if x not in resarr and i not in resarr:
              resarr.append(i)
              resarr.append(x)
              if x!=i:
                print(arr.index(i)," ",arr.index(x))