#Program to print all prime numbers <=n using Sieve of Eratosthenes

def sieveOfEratosthenes(n):
    prime_nums=[True for i in range(n+1)] #array with all True values
    x=2
    
    while(x*x<=n):
        if prime_nums[x]==True:
            for i in range(x*x,n+1,x):
                prime_nums[i]=False #updating multiples of x to false
        x+=1    
        
    for x in range(2,n+1):
        if prime_nums[x]:
            print(x)
            
        
sieveOfEratosthenes(200)