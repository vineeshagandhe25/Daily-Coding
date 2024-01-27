# Total number of permutations with duplication allowed. 


def permutations(arr,length,string=''):  #  function to generate  permutations
    # This code generates all the permutations of a number and no of permutations are N! where N is no of digits in input integer
    # Time Complexity --- O(N!)
    
    if length==0:
        print(string) # base condition (printing permutations)
        string=''
        

    else :
        for i in  range(len(arr)):
            if arr[0:i].count(arr[i])==0:       
                permutations(arr,length-1,string+str(arr[i]))

num=temp=121
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

        
    permutations(res,len(res))
    

# * Time Complexity --- O(N^N) where N is no of digits in input integer 
# * Space Complexity --- O(N) where N is no of digits in input integer (Due to the space used to store the digits in res[])
