def maxProductSubarrayBruteForce(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    max_product = float('-inf')
    
    for i in range(n):
        product = 1
        for j in range(i, n):
            product = product * nums[j]
            max_product = max(max_product, product)
    
    return max_product

# Example usage
nums = [2, 3, -2, 4]
print(maxProductSubarrayBruteForce(nums))  # Output should be 6 (subarray [2, 3])
