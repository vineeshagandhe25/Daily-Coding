# Q : The input is given in array format (which is a number) add 1 to that num and res must be in array format

# Function which add 1 to num (array) and returns result
def sum_arr(arr):
    num=0  # to store num , which is obtained from array

    # code to obtain num from array
    for i in arr:  # Time Complexity --- O(N)  where N is the length of arr
        num = num * 10 + i
    sum=num+1
    res_arr=[]  # to store res  

    # to convert number (sum) into array format
    while sum > 0:   # Time Complexity --- O(N)  where N is the length of arr
        rem=sum%10
        res_arr.insert(0,rem)
        sum //= 10

    return res_arr  # returning res_arr


arr=[1,2,3]  # input array
print(sum_arr(arr))  # calling function  and printing resultant array

#  * Time Complexity --- O(N)+O(N)=O(N)  where N is the length of arr
#  * Space Complexity --- O(N)  where N is the length of arr