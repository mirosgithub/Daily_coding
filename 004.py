"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

# Solution 
# My attempt: correct logic but not in linear time
def missing_int(integers_list):
    integers_list.sort()
    prev = 0
    
    for i in integers_list:
        if i > prev + 1:
            return prev + 1
        elif i < 1:
            continue
        else:
            prev = i
            
    return prev + 1

# Correct solution:
def missing_int_2(integers_list):
    n = len(integers_list)

    for i in range(n):
        while 1 <= integers_list[i] <= n and integers_list[integers_list[i]-1] != integers_list[i]:
            temp = integers_list[integers_list[i]-1]
            integers_list[integers_list[i]-1] = integers_list[i]
            integers_list[i] = temp
    
    for i in range(n):
        if integers_list[i] != i + 1:
            return i + 1
    
    return n + 1

# Test
integers = [3, 4, -1, 1]
print(missing_int(integers))
print(missing_int_2(integers))

integers = [1, 2, 0]
print(missing_int(integers))
print(missing_int_2(integers))

integers = [-1, -2, 0]
print(missing_int(integers))
print(missing_int_2(integers))