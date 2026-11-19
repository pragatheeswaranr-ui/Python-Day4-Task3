
# Employee Data Analysis

print("Hello Jupyter")

# Introduction
# Practising Python basics and execution time comparison.

numbers = list(range(1000))

# List comprehension
list_result = [x * 2 for x in numbers]

# For loop
def double_numbers():
    result = []
    for x in numbers:
        result.append(x * 2)
    return result

loop_result = double_numbers()

print("List comprehension result:", list_result[:5])
print("For loop result:", loop_result[:5])

# Execution Time Comparison
# List comprehension: 45.4 microseconds
# For loop: 43.5 microseconds
# For loop was slightly faster in this test.

# When to use Notebook and Python file
# 1. Jupyter Notebook is useful for learning and testing code.
# 2. It is useful for data analysis and visualisation.
# 3. Python files are useful for complete programs.
# 4. Python files are useful for reusable code.
