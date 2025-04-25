"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# Solution
# Nested loop, O(n^2)
def add_up_to_k(numbers_list, k):

    for i in range(len(numbers_list) - 1):
        a = numbers_list[i]
        for j in range(i + 1, len(numbers_list)):
            b = numbers_list[j]
            if a + b == k:
                return True
    
    return False

# Bonus problem
# My attempt: not exactly a one pass since the 'in' operation takes O(n)
def bonus_add_up_to_k(numbers_list, k):
    
    for i in range(len(numbers_list) - 1):
        a = numbers_list[i]
        b = k - a
        if b in numbers_list[i + 1:]:
            return True
        
    return False

# Correct solution: true one-pass using a set
# List searches are linear time O(n) as it needs iteration
# Set searches are constant time O(1) as it uses hash-based lookup
def bonus2_add_up_to_k(numbers_list, k):
    
    seen = set()
    
    for number in numbers_list:
        if k - number in seen:
            return True
        seen.add(number)
    
    return False

# Tests
numbers = [10, 15, 3, 7]
k = 17
print(add_up_to_k(numbers, k)) # True
print(bonus_add_up_to_k(numbers, k)) # True

numbers = [129, -122, 90, 322]
k = 200
print(add_up_to_k(numbers, k)) # True
print(bonus_add_up_to_k(numbers, k)) # True

numbers = [0, 0, 0, 0]
k = 4
print(add_up_to_k(numbers, k)) # False
print(bonus_add_up_to_k(numbers, k)) # False

numbers = [10, 9, 5, 7]
k = 10
print(add_up_to_k(numbers, k)) # False
print(bonus_add_up_to_k(numbers, k)) # False