def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Invalid input: {e}")


