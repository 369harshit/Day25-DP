def longestCommonSubsequence(str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return 0

    if str1[i] == str2[j]:
        return 1 + longestCommonSubsequence(str1, str2, i + 1, j + 1)
    
    return max(longestCommonSubsequence(str1, str2, i + 1, j), longestCommonSubsequence(str1, str2, i, j + 1))

# Example usage
str1 = "AGGTAB"
str2 = "GXTXAYB"
print(longestCommonSubsequence(str1, str2, 0, 0))  # Output should be 4 (LCS: "GTAB")
