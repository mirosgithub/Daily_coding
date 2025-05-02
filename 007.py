"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# Solution
def count_ways(message):
    if not message:
        return 0
        
    n = len(message)
    
    ways = [0] * (n + 1)
    ways[0] = 1 
    
    for i in range(1, n + 1):
        if message[i - 1] != '0':
            ways[i] += ways[i - 1]
            
        if i > 1:
            two_digit = int(message[i - 2:i])
            if 10 <= two_digit <= 26:
                ways[i] += ways[i - 2]
    
    return ways[n]
        
# Tests
print(count_ways("111")) 
print(count_ways("11111")) 
print(count_ways("210814")) 
print(count_ways(""))
print(count_ways("1010"))