def longestIncreasingSubsequence(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    # Initialize an array to store the length of the longest increasing subsequence ending at each index
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The maximum value in the dp array will be the length of the longest increasing subsequence
    return max(dp)

# Example usage
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longestIncreasingSubsequence(nums))  # Output should be 6 (subsequence: [10, 22, 33, 50, 60, 80])

