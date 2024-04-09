# How would you swap two numbers without using a third variable?

a=10
b=5
def swap():
    global a,b
    b = b + a;  # now b is sum of both the numbers
    a = b - a;  # b - a = (b + a) - a = b (a is swapped)
    b = b - a;   # (b + a) - b = a (b is swapped)
    return a,b

print("Before swapping  a:",a," b:",b)
swap()
print("After swapping  a:",a," b:",b)
