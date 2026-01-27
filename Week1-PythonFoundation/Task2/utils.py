# utils.py
# Reusable utility functions

def calculate_sum(*args):
    """
    Accepts multiple numbers and returns their sum
    """
    total = 0
    for num in args:
        total += num
    return total


def calculate_average(*args):
    """
    Returns average of given numbers
    """
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


def print_details(**kwargs):
    """
    Prints key-value pairs nicely
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")
