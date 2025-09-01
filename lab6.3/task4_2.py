def sum_to_n(n):
    if n <= 0:
        return "Please enter a positive integer."
    return n * (n + 1) // 2   # formula for sum of first n natural numbers

# User input
num = int(input("Enter a positive integer: "))
result = sum_to_n(num)
print(f"Sum of first {num} natural numbers is {result}")
