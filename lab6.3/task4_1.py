def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

num = int(input("Enter a positive integer: "))
result = sum_to_n(num)
print(f"Sum of first {num} natural numbers is {result}")
    
    
    
    