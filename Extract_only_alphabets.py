# Given a string, return only alphabetical string. 

def extract_string(string): # Function to return only alphabetical string
    res_str='' # Varible used to store resultant string
    for ch in string: # Time Complexity is O(N) where N is length of string.
      if  (ord(ch) >= 65 and ord(ch)<=90) or (ord(ch) >= 97 and ord(ch)<=122):  # Checking if ch is alphabet
         res_str+=ch
    
    return res_str   
           
                                                        #  Test Cases     
print(extract_string(" hello, how are you ? "))         # General Input
print(extract_string("cousins coding assignment :)"))   # Lower case letters
print(extract_string("HAPPY REPUBLIC DAY "))            # Upper case letters
print(extract_string("VineeshaGandhe"))                 # string with no spaces
print(extract_string("~!@#$%^&*"))                      # string with no alphabets
print(extract_string("100---police"))                   # string with integers   
print(extract_string(""))                               # empty string

# * Time Complexity ---  O(N) where N is length of string.
# * Space Complexity --- O(M) where M is lenght of res_str.          
