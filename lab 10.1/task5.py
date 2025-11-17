import time
"""
This script calculates the squares of numbers from 1 to 999,999 using list comprehension,
prints the total number of squares computed, and measures the execution time.
Steps:
1. Records the start time.
2. Generates a list of squares for numbers in the specified range.
3. Prints the length of the generated list.
4. Records the end time and calculates the execution duration.
5. Prints the execution time in seconds.
Intended to demonstrate efficient list creation and basic performance measurement in Python.
"""

start_time = time.time()

# Using list comprehension for faster execution
squares = [number ** 2 for number in range(1, 1_000_000)]
print(len(squares))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
