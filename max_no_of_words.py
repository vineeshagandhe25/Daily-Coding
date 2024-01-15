''' qns: You are given array of strings sentences, where each sentences[i] repersents a single sentence.
Return the max no of words that appear in a single sentence'''

sentences=["Happy pongal","happy pongal to you","happy pongal to you and for your family"]
max=0

def my_split(sen): # split function
    res=''
    res_lst=[]
    for i in sen: #  Time Complexity -- O(m) where m is length of sentence
        if i != ' ':    # based on the ' ' char we are separating  words in string
            res=res+i
        else:
            res_lst.append(res)  #appending each word to res_lst
            res=''
    res_lst.append(res)   # appending last word to res_lst     
    return res_lst       

for sentence in sentences: # Time Complexity -- O(n)  where n is length of sentences
    temp=0    
    sen=my_split(sentence)  # splitting the string into words using my_slipt() 
    for word in sen:   # Time Complexity -- O(l)   where  l is length of sen
        temp+=1
    if max<temp:
        max=temp   

print(max)    

# As we are calling n times my_split so Time Complexity is o(n*m)

# Time Complexity ---> O(n)+O(m*n)+O(l)--->O(m*n)
