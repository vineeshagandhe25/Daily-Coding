#Q:Convert a given integer to word
num=-123
words={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
#words dictionary
if num==0:
    print(words[0])
else:
 if num<0:
    num=num*(-1)
 output_string=''
 f=1
 while num>0:
    r=num%10
    if f!=1:
        output_string=words[r]+'-'+output_string
    else :
       output_string=words[r]
       f=0
    num=num//10
 print(output_string)