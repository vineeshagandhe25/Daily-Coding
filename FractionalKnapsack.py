def fractional_knapsack(items, capacity):
   
    for item in items:
        item.append(item[0] / item[1])  
    
   
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0
    
    for item in items:
        if capacity >= item[1]:  
            total_value += item[0] 
            capacity -= item[1]  
        else:  
            fraction = capacity / item[1] 
            total_value += item[0] * fraction  
            break
    
    return total_value


items = [[60, 10], [100, 20], [120, 30]]  
capacity = 50
max_value = fractional_knapsack(items, capacity)
print("Maximum value in knapsack:",max_value)
