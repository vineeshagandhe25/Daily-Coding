# Given an integer  print all of its permutations 
dup=0 # variable used to avoid duplicate permutations

def permutations(arr,first,last):  #  function to generate  permutations
    # This code generates all the permutations of a number and no of permutations are N! where N is no of digits in input integer
    # Time Complexity --- O(N!)
    global dup
    if first==last and arr != dup:
        print(arr) # base condition (printing permutations)
        dup=arr.copy() # copying current permutation into dup var
    else :
        for i in range(first,last):
                arr[first],arr[i]=arr[i],arr[first]     # swapping eles to get permutations
                permutations(arr,first+1,last)  # recursively calling 
                arr[i],arr[first]=arr[first],arr[i]    # back tracking    


num=temp=-1234
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
