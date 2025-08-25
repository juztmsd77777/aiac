import re

def is_valid_indian_mobile(number):
    """
    Validates if the given number is a valid Indian mobile number.
    It must start with 6, 7, 8, or 9 and have exactly 10 digits.
    """
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, str(number)))

# Example usage
mobile = input("Enter a mobile number: ")
if is_valid_indian_mobile(mobile):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")
