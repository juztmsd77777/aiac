def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
even_total, odd_total = sum_even_odd(nums)
print("Sum of even numbers:", even_total)
print("Sum of odd numbers:", odd_total)
