"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

# Solution
def largest_sum(integers):
    
    if not integers:
        return None
    
    best_sum = []
    
    for i in range(len(integers)):
        if i == 0: # if no previous sum, append current number as best sum
            best_sum.append(integers[i])
        elif i == 1: # elif no pre-previous sum, append max(current, previous sum) as best sum
            best_sum.append(max(integers[i], best_sum[i - 1]))
        else: # else, append max(current + pre-previous sum, previous sum) as best sum
            best_sum.append(max(integers[i], integers[i] + best_sum[i - 2], best_sum[i - 1]))
        
    return best_sum[-1]

# Follow-up solution
def followup_largest_sum(integers):
    if not integers:
        return None
    
    # Initialize with the first element to handle negative-only arrays
    best_1_before = integers[0]
    best_2_before = 0  # This represents "nothing" (empty selection)
    current_best = integers[0]
    
    for i in range(1, len(integers)):
        if i == 1:
            current_best = max(integers[i], best_1_before)
        else:
            current_best = max(integers[i], integers[i] + best_2_before, best_1_before)
        
        # Update trackers
        best_2_before = best_1_before
        best_1_before = current_best
    
    return current_best

# Tests
integers = [2, 4, 6, 2, 5]
print(largest_sum(integers))
print(followup_largest_sum(integers))

integers = [5, 1, 1, 5]
print(largest_sum(integers))
print(followup_largest_sum(integers))

integers = [-2, -4, -1]
print(largest_sum(integers))
print(followup_largest_sum(integers))

integers = []
print(largest_sum(integers))
print(followup_largest_sum(integers))