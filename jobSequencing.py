# Jod sequencing with deadline by greedy algorithm. 
def jobSequencing(data,deadline):
    n=len(data) # length of data
    
    # arranging the data as per there profits in descending order
    for i in range(n):
        for j in range(n-i-1):
            if data[j][2]<data[j+1][2]:
                data[j][2],data[j+1][2]=data[j+1][2],data[j][2]
    
    solts=[0]*deadline
    jobs=[0]*deadline

    for i in range(n):
        for j in range(min(deadline-1,data[i][1]-1),-1,-1) :
            if solts[j] == 0:
                solts[j]=1
                jobs[j]=data[i][0]
                break

    return jobs

data=[['j1',2,20],['j2',1,15],['j3',1,10],['j4',3,5],['j5',3,1]]
deadline=3
print(jobSequencing(data,deadline))        