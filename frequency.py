# Finding freq of a ele

Arr=['a','b','c','a','b']
Freq={}
for i in Arr:
     if i in Freq:
        Freq[i]=Freq[i]+1
     else:
         Freq[i]=1
for i in Freq:
    print("Freq of ",i," ",Freq[i])