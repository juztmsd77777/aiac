def factorial(n):
    if not isinstance(n, int):
        return "Input must be an integer."
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    user_input = int(input("Enter a number to calculate its factorial: "))
    output = factorial(user_input)
    print(f"Factorial of {user_input} is {output}" if isinstance(output, int) else output)
except ValueError:
    print("Please enter a valid integer.")


