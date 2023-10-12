def max_sum_increasing_subsequence(arr):
    n = len(arr)
    max_sum = [0] * n
    
    for i in range(n):
        max_sum[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                max_sum[i] = max(max_sum[i], max_sum[j] + arr[i])

    return max(max_sum)

# Example usage
arr = [1, 101, 2, 3, 100]
print(max_sum_increasing_subsequence(arr))  # Output: 106
