#Q:Given an integer n, find its binary format and store it in an array.

# code to find binary format
def binaryFormat(num): 
    res_arr=[]  # resultant binary format array

    while num>0:   # Time Complexity --- O(N)  where N is the no.of digits in num
       
       # code to get binary format
       rem=num%2
       res_arr.insert(0,rem)  # inserting from left to right 
       num=num//2

    return res_arr

num=12
print(binaryFormat(num))  # printing result by calling function

 # Time Complexity --- O(N)  where N is the no.of digits in num
 # Space Complexity --- O(logM) where M is the input num