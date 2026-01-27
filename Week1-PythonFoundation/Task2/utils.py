# utils.py
# Reusable utility functions

def calculate_sum(*args):
    # Time Complexity: O(n)
    return sum(args)


def calculate_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Lambda function
square = lambda x: x * x


# Tuple example
dimensions = (10, 20)


if __name__ == "__main__":
    print("Sum:", calculate_sum(1, 2, 3))
    print("Average:", calculate_average(10, 20, 30))
    print("Square:", square(5))
    print("Dimensions:", dimensions)
    print_details(name="Ali", role="Student")
