def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a number: "))
    fact = factorial(num)
    if fact is not None:
        print(f"Factorial of {num} is {fact}")
except ValueError:
    print("Please enter a valid integer.")