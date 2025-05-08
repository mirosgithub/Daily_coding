"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

# Solution
def longest_substring(s, k):
    if not s or k == 0:
        return 0
        
    char_count = {}
    start = 0
    max_length = 0
    
    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        
        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Tests
s = "abcba"
k = 2
print(longest_substring(s, k))