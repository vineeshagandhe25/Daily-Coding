# check whether given character present in given words array or not .If yes then store that index in resultant array.

# function to check the ele in words
def check(words,key):
    res_arr=[]
    for i in words:
      if key in i:
          res_arr.append(words.index(i))
    return res_arr

words=['vinni','vinnu','vineesha','shanvi'] 
key='v'
