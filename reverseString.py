# Write a function in Python that takes a string as input and returns the reverse of the string. For example, if the input is "hello", the function should return "olleh".

# function which reverse the string
def reverseString(string):
    
    # len() : Time Complexity --- O(N) where N is length of string
    last_index=len(string)-1
    res_str=''
    
    # starting from last index and assigning letters from last to res_str 
    for i in range(last_index,-1,-1):  # Time Complexity --- O(N) where N is length of string
        res_str += string[i]

    return res_str

string='Coding'
print(reverseString(string)) # general input
print(reverseString('')) # empty string
print(reverseString('a')) # single character


# * Time Complexity --- O(N) where N is length of string
# * Space Complexity --- O(N) where N is length of string
