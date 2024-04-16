def fractional_knapsack(value, weight, capacity):
   
    ratios = [(v/w, w) for v, w in zip(value, weight)]
    
    ratios.sort(reverse=True)
    
    total_value = 0
    fractions = [0]*len(value)
    
    for ratio, w in ratios:
        if capacity == 0:
            break
        if w <= capacity:
           
            fractions[value.index(ratio*w)] = 1
            total_value += ratio*w
            capacity -= w
        else:
            
            fractions[value.index(ratio*w)] = capacity/w
            total_value += ratio*capacity
            capacity = 0
    
    return total_value, fractions

# Example usage
value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

max_value, fractions = fractional_knapsack(value, weight, capacity)
print("Maximum value:", max_value)
print("Fractions of items:",fractions)
