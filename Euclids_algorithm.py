# Q: Given two positive integer a & b ,return no of common factors of a and b.
# Using Euclidean_algorithm
'''Euclidean_algorithm --- This algorithm helps us to find greatest common divisor(GCD) of 2 numbers .If we divide the small number the 
algorithm stops when the remainder is 0'''
def gcd(a,b): # Time Complexity is O(log(min(a,b)))
    if b==0:
        return a
    return gcd(b,a % b)

def factors(n1,n2): # Function to find no of common factors 
    gcd_val=gcd(n1,n2) # gcd_var is used to store the returned value from gcd() which implies highest common factor of both n1 &n2
    count=0  # count variable is used for counting no of common factors of n1 &n2
    for i in range(1,gcd_val+1):
        # As loop iterates upto gcd_val where Time complexity of gcd is O(log(min(n1,n2))).So here the time complexity is O(log(min(n1,n2)))
        if n1 % i == n2 % i == 0: 
            count+=1
    return count        

                     #Test  Cases
print(factors(6,12)) # General case
print(factors(25,30)) # General case         
print(factors(4,4))   # Both integers are same
print(factors(11,17))  # prime numbers
print(factors(32,4)) # one number is multiple of another 

# * Time Complexity ---  O(log(min(a,b))) + O(log(min(n1,n2))) = O(log(min(n1,n2)))
# * Space Complexity --- O(1) as only constant no of variables used.          