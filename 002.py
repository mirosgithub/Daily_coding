"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

import math

# Solution
# My attempt: did not account for the division by zero case
def products(integer_array):
    new_array = []
    product = math.prod(integer_array)
    
    for i in range(len(integer_array)):
        new_array.append(product // integer_array[i])
        
    return new_array

# Bonus problem
# My attempt: time complexity of O(n^2), not the most effective
def bonus_products(integer_array):
    new_array = []
    
    for i in range(len(integer_array)):
        new_array.append(math.prod(integer_array[:i] + integer_array[i + 1:]))
        
    return new_array

# Correct solution: time & space complexity of O(n)
def bonus2_products(integer_array):
    n = len(integer_array)
    left = [1] * n
    right = [1] * n
    new_array = []
    
    for i in range(1, n):
        left[i] = left[i - 1] * integer_array[i - 1]
        
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * integer_array[i + 1]
        
    for i in range(n):
        new_array.append(left[i] * right[i])
                         
    return new_array

# Tests
integers = [1, 2, 3, 4, 5]
print(bonus2_products(integers))

integers = [3, 2, 1]
print(bonus2_products(integers))

integers = [20, 3, 0, 10]
print(bonus2_products(integers))