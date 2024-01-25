# Q: Given two positive integer a & b ,return no of common factors of a and b.

def factors(n1,n2):  # Function to find no of common factors of n1(a) and n2(b)
    iterations=0            # iterations variable used to store the no of for loop iterations
    count=0          # count varible used to count the no of common factors
    if n1==n2: # if n1 & n2 equal then iterations is any of them
        iterations=n1
    elif n1 < n2: # the number which is the small in given 2 numbers will be the iterations 's value
        iterations=n1
    else:
        iterations=n2
    if n1 % n2==0 : # if one integer is multiple of another then iterations be multiple //2
        iterations=n2//2
        count+=1
    elif n2%n1 ==0:
        iterations=n1//2
        count+=1        
    for i in range(1,iterations+1):  # Time Complexity --- O(N) where N = iterations
        if n1 % i==0 and n2 % i==0: # if i divides both n1 & n2 then count increases
            count+=1
    return count 
                     #Test  Cases
print(factors(6,12)) # General case
print(factors(25,30)) # General case         
print(factors(4,4))   # Both integers are same
print(factors(11,17))  # prime numbers
print(factors(32,4)) # one number is multiple of another 

# * Time Complexity --- O(N) where N = iterations
# * Space Complexity --- O(1) as only constant no of variables used.
