"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Solution
# This was my first time learning about functional programming and closure
# Functional Programming: Functions can be used as inputs/outputs and data can be 
# represented as behavior rather than structure.
# Closures: Functions remember variables from their creation environment. 
# 'pair' captures and remembers 'a' and 'b' values even after cons() finishes.
def car(pair):
    def first(a, b):
        return a
    
    return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    
    return pair(last)

# Test
print(car(cons(3, 4)))
print(cdr(cons(3, 4)))