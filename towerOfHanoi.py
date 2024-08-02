# Tower of Hanoi problem
import math

def towerOfHanoi(n):
    # Calculate the total number of steps required
    steps = int(math.pow(2, n) - 1)

    # Iterate over each step
    for i in range(steps + 1):
        # Calculate the source
        start = (i & i + 1) % 3
        # Calculate the destination 
        end = ((i | i + 1) + 1) % 3
        print("Disk is moved from ", start, " to ", end)

# Test the function with 3 disks
towerOfHanoi(3)

# Time Complexity --- O(2^n)
# Space Complexity --- O(1)