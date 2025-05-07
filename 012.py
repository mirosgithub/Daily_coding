"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

# Solution
# My attempt: correct logic, except for the base case of N = 0
def ways_to_climb(N):

    def climb(s, N):
        if N < s:
            return 0
        elif N == s:
            return 1
        
        N -= s
        return climb(1, N) + climb(2, N)
    
    return climb(1, N) + climb(2, N)

# Correct solution: memoization for better efficiency
def ways_to_climb_correct(N):
    memo = {}
    
    def climb(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        memo[n] = climb(n-1) + climb(n-2)
        return memo[n]
    
    return climb(N)

# Bonus problem
# My attempt: correct logic, except for the base case of N = 0
def custom_ways_to_climb(N, X):

    def custom_climb(s, X, N):
        if N < s:
            return 0
        elif N == s:
            return 1
        
        N -= s
        ways = 0
        for x in X:
            ways += custom_climb(x, X, N)
        return ways
    
    ways = 0
    for x in X:
            ways += custom_climb(x, X, N)
    return ways

# Correct solution: memoization for better efficiency
def custom_ways_to_climb_correct(N, X):
    memo = {}
    
    def climb(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        memo[n] = sum(climb(n - x) for x in X)
        return memo[n]
    
    return climb(N)

# Test cases:
# Basic problem
print("Testing basic staircase problem:")
print("N | Original | Memoized")
print("-" * 25)
for i in range(10):
    print(f"{i} | {ways_to_climb(i):8d} | {ways_to_climb_correct(i):8d}")

# Bonus problem
print("\nTesting bonus problem with different step sizes:")
test_cases = [
    (5, [1, 2]),    
    (5, [1, 3, 5]),  
    (6, [1, 2, 3]),  
    (4, [2, 3]),     
]

print("\nN | Step Sizes | Original | Memoized")
print("-" * 45)
for N, X in test_cases:
    print(f"{N} | {X} | {custom_ways_to_climb(N, X):8d} | {custom_ways_to_climb_correct(N, X):8d}")

# Time efficiency test
print("\nDemonstrating memoization impact:")
import time

def time_function(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

N = 30
result1, time1 = time_function(ways_to_climb, N)
result2, time2 = time_function(ways_to_climb_correct, N)

print(f"\nCalculating ways_to_climb({N}):")
print(f"Original (no memoization): {time1:.4f} seconds")
print(f"With memoization: {time2:.4f} seconds")
print(f"Speedup factor: {time1/time2:.1f}x")