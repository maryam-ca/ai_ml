# generators.py

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def custom_range(start, end, step):
    while start < end:
        yield start
        start += step


if __name__ == "__main__":
    print("Fibonacci Series:")
    for num in fibonacci(5):
        print(num)

    print("\nCustom Range:")
    for num in custom_range(1, 10, 2):
        print(num)
