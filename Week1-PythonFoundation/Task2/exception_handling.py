# exception_handling.py
# Exception-safe calculator

def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Operation (+ - * /): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        else:
            print("Invalid operation")
            return

    except ValueError:
        print("Error: Invalid number input")
    except ZeroDivisionError:
        print("Error: Division by zero")
    else:
        print("Result:", result)
    finally:
        print("Calculator finished")


if __name__ == "__main__":
    calculator()
