# Given an integer  print all of its permutations 

def permutations(a,f,h):  
    if f==h:
        print(str(a))
    else :
        for i in range(f,h):
            a[f],a[i]=a[i],a[f]
            permutations(a,f+1,h)
            a[i],a[f]=a[f],a[i]

num=temp=153
res=[]
while temp != 0:
    x=temp%10
    res.append(x)
    temp //= 10
        
permutations(res,0,len(res))
