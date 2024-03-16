# python to find min and max elements from given array.

# function to find min and max eles
def Min_Max(a,i,j,min,max):
    if i == j: # code for single ele of array
        max=min=a[i]
        return max,min
    elif i == (j-1): # code for comparing two eles
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
        # finding mid and recursively calling functions to get min and max by comparing with exsiting min and max
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

# * Time COmplexity --- O(N) # N is length of input array
# * Space COmplexity --- O(N) # N is length of input array
