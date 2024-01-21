#Given an integer, you have a chance to swap any of its digits. Return the maximum number that can be formed by atmost one swap. 

num=9993678
if num>11:
 length=0
 temp=num 
 while temp>0:
    temp=temp//10
    length+=1
 arr=[0]*length 
 temp=num
 for i in range(length-1,-1,-1):
    n=temp%10
    temp=temp//10 
    arr[i]=n  # storing  digits in reverse order in an array
 x=t=0
 while True:
  for i in range(t+1, length):
    if arr[x]<arr[i]:
        x=i   #finding out the max ele in an array 
  if x==t:
      x=t=t+1
      continue
  else :
      break
 if x!=t:
    arr[t],arr[x]=arr[x],arr[t] #swapping that max ele with first ele
 n=0
 for i in arr:
    n=n*10+i  #conversion of arr into num
 print(n)
else:
 print(num)
#time complexity is O(log(num))
