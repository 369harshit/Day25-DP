def matrix_chain_order(arr):
    # Create a table to store results of subproblems
    n = 5  # Assuming N = 5 for this example
    dp = []
    for _ in range(n):
      row = []
      for _ in range(n):
        row.append(0)
      dp.append(row)

# Now dp is a 2D list with dimensions n x n, and all elements are initialized to 0.


    # dp[i, j] will store the minimum cost of multiplying matrices from i to j

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]

# Example usage
N = 5
arr = [40, 20, 30, 10, 30]
result = matrix_chain_order(arr)
print(f"Minimum cost of matrix multiplication: {result}")
