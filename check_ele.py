# check whether given character present in given words array or not .If yes then store that index in resultant array.

# function to check the given  character k  in words
def check(words,key):
    res_arr=[]
    for i in words:  # Time Complexity --- O(N) where N is Length of Words 
      
      # as 'in' operator takes O(M) where M is the length of the i , The Time Complexity is O(M)
      # so the overall time complexity --- N * M ( In worst case M is the size of largest len of i) 

      if key in i:  
           
          # append function takes O(1) 
          res_arr.append(words.index(i))

    return res_arr

words=['vinni','vinnu','vineesha','shanvi']  # given input
key='v'
print(check(words,key))

# * Time Complexity --- O(N*M) where N is len of words and M is the len max(words[i] where i is in range of 0-len(words)-1)
# * Space Complexity --- O(N) where N is the length of words 