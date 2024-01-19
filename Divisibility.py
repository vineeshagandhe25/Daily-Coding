# Given an array of natural numbers, find the number of elements individually divisible by 2, divisible by 3, by 5 and by 7. 

arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,121]
divby2=divby3=divby5=divby7=0    # initialising variables to store no of eles divisible by 2,3,5,7 respectively

for i in arr: # Time Complexity is O(n)
    # incrementing the variables if i  is divisible with any of 2,3,5&7
    if i % 2 == 0:  
        divby2 +=1
    if i % 3 == 0:
        divby3 +=1    
    if i % 5 == 0:
        divby5 +=1  
    if i % 7 == 0:
        divby7 +=1      

print("Total no of eles in given arr which are divisible by 2 = ",divby2)
print("Total no of eles in given arr which are divisible by 3 = ",divby3)
print("Total no of eles in given arr which are divisible by 5 = ",divby5)
print("Total no of eles in given arr which are divisible by 7 = ",divby7)

# * Time Complexity ---> O(n)
# * Space Complexity ---> O(1) as only constant no of variables used