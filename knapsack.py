def fractional_knapsack(capacity, weights, values):
    n = len(weights)
    value_weight_ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    value_weight_ratio.sort(reverse=True)

    total_value = 0
    knapsack = []

    for ratio, weight, value in value_weight_ratio:
        if capacity >= weight:
            knapsack.append((weight, value))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((capacity, fraction * value))
            total_value += fraction * value
            break

    return total_value, knapsack

capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]

max_value, items_taken = fractional_knapsack(capacity, weights, values)
print("Maximum value:", max_value)
print("Items taken:", items_taken)
