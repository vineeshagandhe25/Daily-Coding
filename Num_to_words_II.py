#Q:Convert a given integer into words
num=21324132
ones=['one','two','three','four','five','six','seven','eight','nine']
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = [ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty","ninety"]
if num==0:
    print("zero")
else:
 if num<0:
    print("invalid")
 output_string=''
 if num>=10000000:
    r=num//10000000
    if r>=10 and r<20:
        output_string+=teens[r-10]+" "+"crore"+" "
    elif r>=20:
         output_string+=tens[r//10-2]
         r=r%10
    if r>0 and r<10:
        output_string+=ones[r-1]+" "+"crore"+" " 
    elif r==0:
        output_string+=" "+"crore"+" "       
    num=num%10000000  
 if num>=100000:
    r=num//100000
    if r>=10 and r<20:
        output_string+=teens[r-10]+" "+"lakh"+" " 
    elif r>=20:
         output_string+=tens[r//10-2]
         r=r%10
    if r>0 and r<10:
        output_string+=ones[r-1]+" "+"lakh"+" " 
    elif r==0:
        output_string+=" "+"lakh"+" "    
    num=num%100000
 if num>=1000:
    r=num//1000
    if r>=10 and r<20:
        output_string+=teens[r-10]+" "+"thousand"+" " 
        r=0
    elif r>=20:
         output_string+=tens[r//10-2]
         r=r%10
    if r>0 and r<10:
        output_string+=ones[r-1]+" "+"thousand"+" "
    elif r==0:
        output_string+=" "+"thousand"+" "
    num=num%1000

 if num>=100:
        output_string+=ones[r//100-1]+"hundred"+" "
        r=r%100
        if 10 <= r < 20:
            output_string+= teens[r - 10]+" "
            r = 0
        elif r >= 20:
            output_string += tens[(r//10)-2]+" "
            r %= 10
        if r > 0:
            output_string += ones[r-1]

    
 print(output_string)
