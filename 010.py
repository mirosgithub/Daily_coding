"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

# Solution
import threading

def job_scheduler(f, n):
    delay = n / 1000
    
    timer = threading.Timer(delay, f)
        
    timer.start()
    
# Tests
def greet():
    print("Hi Miro!")

job_scheduler(greet, 2000)

print("Job 'greet()' is scheduled in 2s...")