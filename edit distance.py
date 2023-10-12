def minDistance(word1, word2):
    def helper(i, j):
        # If one of the words is empty, return the remaining length of the other word
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        # If the characters match, move both pointers
        if word1[i] == word2[j]:
            return helper(i + 1, j + 1)
        
        # Try all three operations: insert, delete, and replace
        insert = 1 + helper(i, j + 1)
        delete = 1 + helper(i + 1, j)
        replace = 1 + helper(i + 1, j + 1)
        
        # Return the minimum of the three options
        return min(insert, delete, replace)
    
    return helper(0, 0)

# Example usage
word1 = "abc"
word2 = "acc"
print(minDistance(word1, word2))  # Output: 1
