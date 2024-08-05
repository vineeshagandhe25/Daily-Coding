# Tower of Hanoi problem
'''Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. 
Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. 
The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules: 
Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. 
a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.'''

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