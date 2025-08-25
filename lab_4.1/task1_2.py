def is_valid_indian_mobile(number: str) -> bool:
    """
    Returns True if the given string is a valid Indian mobile number.
    A valid Indian mobile number:
      - Has exactly 10 digits
      - Starts with 6, 7, 8, or 9
    """
    if not isinstance(number, str):
        return False
    if len(number) != 10:
        return False
    if not number.isdigit():
        return False
    if number[0] not in {'6', '7', '8', '9'}:
        return False
    return True

user_input = input("Enter a mobile number: ")
if is_valid_indian_mobile(user_input):
    print("Valid Indian mobile number")
else:
    print("Invalid Indian mobile number")

