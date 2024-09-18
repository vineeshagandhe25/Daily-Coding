# Code to count the number of consonants in given string .

string='Vishal is a Good BOY !@#$%^&* () 1234567890'
count=0          

for i in string: 
    ch = i.upper() # to ignore upper and lower case by making all letters as upper case.

    # checking for whether i is alphabet or not and checking for consonants.
  
    if  not  (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or  ch == 'U') and ord(ch) >= 65 and ord(ch)<=90:
       # incrementing count for every consonant.
       count+=1  
       
print(count)

# Time Complexity --- O(N) where N is length of given string .
# Space Complexity --- O(1).