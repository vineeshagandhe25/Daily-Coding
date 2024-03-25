'''Write a function in Python that takes a string as input and returns True if the string is a palindrome, and False otherwise.
 Remember, a palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward 
 (ignoring spaces, punctuation, and capitalization).'''

# function to check the given string is palindrome or not
def isPalindrome(string):
    ignoring_symbols={' ','!'," ' ",' " ','.','?',',',';',':','-'} # to ignore spaces,punctuation 
    # in operator with ignoring_symbols is constant time 

    temp1='' # used for storing input string without ignoring symbols 
    temp2='' # used for storing input string without ignoring symbols  in reverse order

    lower_string=string.lower() # to ignore capitalization we make string into lower case
    # Time Complexity of lower() is O(N) where N is the len of string 
    # Space Complexity of lower() is O(N) where N is the len of string 
    
    # Time Complexity of len() is O(1)
    # Space Complexity of len() is O(1)
    for i in range(len(lower_string)-1,-1,-1):# Time Complexity --- O(N) where N is the len of string
        if lower_string[i] in ignoring_symbols: # ignoring spaces, punctuation
            continue
        temp2 += lower_string[i]

    for i in lower_string:  # Time Complexity --- O(N) where N is the len of string
        if i in ignoring_symbols:
            continue
        temp1 += i   
  
    return temp1 == temp2 

print(isPalindrome('Mom!'))   

# * Time Complexity --- O(N) where N is the len of string
# * Space Complexity --- O(N) where N is the len of string


    