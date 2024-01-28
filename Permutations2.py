# Total number of permutations with duplication allowed. 
count=0  #  varible to count no of permutations

def permutations(arr,length,string=''):  #  function to generate  permutations
    # This code generates all the permutations of a number and no of permutations are N^N where N is no of digits in input integer
    # Time Complexity --- O(N^N)
    global count
    if length==0:
        print(string) # base condition (printing permutations)
        string=''
        count+=1 
        
    else :
        for i in  range(len(arr)):
            if arr[0:i].count(arr[i])==0:     # To skip duplicate permutations  
                permutations(arr,length-1,string+str(arr[i])) # Recursive calling

num=temp=111
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
    print(count)
    

# * Time Complexity --- O(N^N) where N is no of digits in input integer 
# * Space Complexity --- O(N) where N is no of digits in input integer (Due to the space used to store the digits in res[])
