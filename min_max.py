def Min_Max(a,i,j,min,max):
    if i == j:
        max=min=a[i]
        return max,min
    elif i == (j-1):
        if a[i] < a[j]:
            max=a[j]
            min=a[i]
            return max,min
        else:
            max=a[i]
            min=a[j]
            return max,min
    else:
        mid=(i+j)//2
        max1,min1=Min_Max(a,i,mid,min,max)
        max2,min2=Min_Max(a,mid+1,j,min,max)
        if min1<min2:
            min=min1
        else:
            min=min2
        if max1>max2:
            max=max1
        else:
            max=max2
        return max,min 
        
a=[34,56,2,90,3]
print(Min_Max(a,0,4,a[0],a[0]))