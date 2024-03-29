# Fractional Knapsack 
def fractional_knapsack(items, capacity):
   
    for item in items:  # Time Complexity --- O(N) where N is the length of items
        item.append(item[0] / item[1])  # profit/weight ratio
    
   
    items.sort(key=lambda x: x[2], reverse=True) # arranging items in decsending order as per their  profit/weight ratio
    
    total_value = 0  # total profit 
    
    for item in items:  # Time Complexity --- O(N) where N is the length of items
        # if capacity >= item weight then we add it to sack
        if capacity >= item[1]:  
            total_value += item[0] 
            capacity -= item[1]  
        # else we make fractions    
        else:  
            fraction = capacity / item[1] 
            total_value += item[0] * fraction  
            # after fractions there is no capacity in sack . So, we break here
            break
    
    return total_value  # returning total profit 


items = [[60, 10], [100, 20], [120, 30]]  # input   
capacity = 50  # knap sack capacity
max_value = fractional_knapsack(items, capacity)
print("Maximum value in knapsack:",max_value)

# Time Complexity --- O(N) where N is the length of items
# Space Complexity --- O(1)
