# Roman to Int
string='VIII'
Roman_nums={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  # Roman nums dict
res=temp=0   
length=len(string)

for i in range(length-1):
    if  Roman_nums[string[i]]< Roman_nums[string[i+1]]  : 
        temp=Roman_nums[string[i]]
        continue
    res=res+Roman_nums[string[i]]-temp
    temp=0
    
res=res+Roman_nums[string[length-1]]-temp   # Adding last roman num to res
print(res) 
