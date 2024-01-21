string='Vishal is a Good BOY !@#$%^&* () 1234567890'
count=0          

for i in string: 
    ch = i.upper() 
    if  not  (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or  ch == 'U') and ord(ch) >= 65 and ord(ch)<=90:
       count+=1  
       
print(count)