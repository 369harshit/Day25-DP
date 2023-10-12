def knapsack(values, weights, capacity, n):
    # Base case: If no more items are left or no capacity left, return 0 (no value can be obtained)
    if n == 0 or capacity == 0:
        return 0
    
    # Exclude the last item and find the maximum value that can be obtained
    without_last_item = knapsack(values, weights, capacity, n - 1)
    
    # Include the last item if its weight fits within the remaining capacity
    if weights[n - 1] <= capacity:
        # Calculate the value obtained by including the last item and subtracting its weight from capacity
        with_last_item = values[n - 1] + knapsack(values, weights, capacity - weights[n - 1], n - 1)
    else:
        with_last_item = 0  # Cannot include the last item due to weight constraint
    
    # Return the maximum value of including or excluding the last item
    return max(without_last_item, with_last_item)

# Example items
values = [5, 4, 8, 6]       # Value of items
weights = [1, 2, 4, 5]      # Weight of items
capacity = 5             # Capacity of the knapsack
num_items = len(values)  # Number of items ie.3


# Calculate the maximum value using the brute-force approach
result = knapsack(values, weights, capacity, num_items)

# Print the result
print("Maximum value:", result)
