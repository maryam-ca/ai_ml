# data_op.py
# Data manipulation practice

numbers = [10, 20, 20, 30, 40, 10, 50]

# Remove duplicates
unique_numbers = list(set(numbers))
print("Unique:", unique_numbers)

# Sort numbers
sorted_numbers = sorted(unique_numbers)
print("Sorted:", sorted_numbers)

# Max, Min, Average
print("Max:", max(sorted_numbers))
print("Min:", min(sorted_numbers))
print("Average:", sum(sorted_numbers) / len(sorted_numbers))
