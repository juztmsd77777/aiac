def factr(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factr(n - 1)

print("Factorial of 5 is:", factr(5))