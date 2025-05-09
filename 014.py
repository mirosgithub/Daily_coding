"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

# Solution
import random

def estimate(n):
    total = n
    count = 0

    for i in range(total):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            count += 1
    
    ratio = count / total
    pi = 4 * ratio

    return pi

# Tests
print(estimate(100))
print(estimate(1000))
print(estimate(10000))
print(estimate(100000))
print(estimate(1000000))
print(estimate(10000000))
print(estimate(100000000))
print(estimate(1000000000))