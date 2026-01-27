# data_op.py
# Data manipulation

numbers = [10, 20, 20, 30, 40, 10]

# Remove duplicates
unique = list(set(numbers))

# Sort
sorted_nums = sorted(unique)

# List comprehension
squares = [n * n for n in sorted_nums]

# Dictionary comprehension
stats = {n: n * n for n in sorted_nums}

print("Unique:", unique)
print("Sorted:", sorted_nums)
print("Squares:", squares)
print("Max:", max(sorted_nums))
print("Min:", min(sorted_nums))
print("Average:", sum(sorted_nums) / len(sorted_nums))
print("Dict:", stats)
