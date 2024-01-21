def rotate(arr,k):
    if k>0:
        x=k%len(arr)
        result=arr[-x:]+arr[:-x]
        print(result)  
    elif k<0:
        print("The no of rotations must be positive num" )
    else:
        print(arr)
arr=[1,2,3,4,5]
rotate(arr,0)
rotate(arr,1)
rotate(arr,8)
rotate(arr,-1)