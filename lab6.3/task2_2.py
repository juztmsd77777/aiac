def multiple(n, limit=10):
    print(f"\nMultiplication Table of {n}")
    print("-" * 25)
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n * i}")
    print("-" * 25)

# User input
num = int(input("Enter a number: "))
limit = int(input("Enter the limit (default 10): ") or 10)  # user can choose limit
multiple(num, limit)
