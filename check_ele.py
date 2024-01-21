words=['vinni','vinnu','vineesha','shanvi']
key='v'
res_arr=[]
for i in words:
    if key in i:
        res_arr.append(words.index(i))
print(res_arr)