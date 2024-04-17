'''Given a string of lower case alphabets count all possible substrings ( not necessarily distinct) that has exactly k distinct characters.
Example:
Input : abc , k=2
Output: 2
Possible substrings are {'ab','bc'} '''

# substring function
def substring(string,k):
    count = 0
    while string:   # Time Complexity --- O(n) where n is length of string
        st=''   # used for substrings 
        s=set() # used to find distinct characters in st

        for i in string:   # Time Complexity --- O(n) where n is length of string
           st += i
           s.add(i)
           if len(s) == k :
               count += 1

        string=string[1:]        
    print("possible substrings that has exactly ",k , "distinct characters---",count)
  
inputString='aba'
k=2   # k distinct characters.
substring(inputString,k)

# Test Cases :
'''inputString='abc'
k=2 #k distinct characters.
substring(inputString,k)
inputString='ababacc'
k=2 #k distinct characters.
substring(inputString,k)
inputString='aba'
k=1 #k distinct characters.
substring(inputString,k)
inputString='aba'
k=3 #k distinct characters.
substring(inputString,k)'''


# * Time Complexity --- O(N^2) where n is length of input string.
# * Space Complexity --- O(N) where n is length of input string.
