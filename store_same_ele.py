# Store same eles in both arrays in res array
A=[4,3,2,1]
B=[2,5,6,7,8,4]
sortedarrA=sorted(A)
sortedarrB=sorted(B)
size=0
if len(A)<len(B):
    size=len(A)
else:
    size=len(B)
res=[0]*size
i=j=k=0
while i<len(A) and j<len(B) :
    if sortedarrA[i]==sortedarrB[j]:
        res[k]=sortedarrA[i]
        k=k+1
        i=i+1
        j=j+1
    elif sortedarrA[i] <sortedarrB[j] :
        i=i+1
    else:
        j=j+1
print(res[:k])