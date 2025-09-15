def is_prime(n: int) -> bool:
    """
    Determine if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n % 2 == 0 and n != 2:  # exclude even numbers > 2
        return False

    # Only check odd divisors up to √n
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")
    except ValueError:
        print("Invalid input, please enter an integer.")

