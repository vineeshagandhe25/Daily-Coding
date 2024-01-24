# Given an integer  print all of its permutations 

def permutations(arr,first,last):  #  function to generate  permutations
    # This code generates all the permutations of a number and no of permutations are N! where N is no of digits in input integer
    # Time Complexity --- O(N!)
    if first==last:
        print(arr) # base condition (printing permutations)

    else :
        for i in range(first,last):
                if arr[first:i].count(arr[i])==0:          
                       arr[first],arr[i]=arr[i],arr[first]     # swapping eles to get permutations
                       permutations(arr,first+1,last)  # recursively calling 
                       arr[i],arr[first]=arr[first],arr[i]    # back tracking    


num=temp=333
res=[] # List to store digits of input integer
if num<0:
     print("Given integer is a negative num plz provide a positive num")
elif num==0:
     print(num)     
else:     
    while temp != 0: # Converting given integer  into list
       x=temp%10
       res.append(x)
       temp //= 10

        
    permutations(res,0,len(res))

# * Time Complexity --- O(N!) where N is no of digits in input integer 
# * Space Complexity --- O(N) where N is no of digits in input integer (Due to the space used to store the digits in res[])
