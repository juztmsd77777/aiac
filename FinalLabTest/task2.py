import re
import unittest

def validate_password(password):
    """
    Validate a password based on required security rules.

    Requirements
    ------------
    - At least 8 characters long
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one special character from: ! @ # $

    Parameters
    ----------
    password : str
        The password string to validate.

    Returns
    -------
    bool
        True if the password meets all security requirements, otherwise False.
    """

    # Check 1: Minimum length requirement
    if len(password) < 8:
        return False

    # Check 2: Contains at least one digit (AI-generated regex)
    if not re.search(r"\d", password):
        return False

    # Check 3: Contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check 4: Contains at least one special character from ! @ # $
    if not re.search(r"[!@#$]", password):
        return False

    # If all checks passed, return True
    return True



# ===========================================================
#                   UNIT TESTS WITH OUTPUT
# ===========================================================

import unittest

class TestPasswordValidation(unittest.TestCase):
    """Unit tests for the validate_password function.

    Each test verifies one rule or an edge-case combination of the password
    validation logic implemented in validate_password.
    """

    def show(self, password, result, expected):
        """Helper to display test inputs and results for easier debugging.

        Prints the password under test, the actual result, and the expected
        result. This does not affect assertions and is intended to make test
        output more readable when running the test suite.
        """
        print("\nPassword:", password)
        print("Output:", result)
        print("Expected:", expected)

    def test_valid_password(self):
        # Valid password: meets length, digit, uppercase, and special-char rules.
        password = "Hello@123"
        expected = True
        result = validate_password(password)
        self.show(password, result, expected)
        self.assertEqual(result, expected)

    def test_short_password(self):
        # Too short: should fail because length < 8.
        password = "Hi@1"
        expected = False
        result = validate_password(password)
        self.show(password, result, expected)
        self.assertEqual(result, expected)

    def test_missing_digit(self):
        # Missing digit: should fail even if other rules are satisfied.
        password = "Hello@AA"
        expected = False
        result = validate_password(password)
        self.show(password, result, expected)
        self.assertEqual(result, expected)

    def test_missing_uppercase(self):
        # Missing uppercase: all-lowercase with digit and special should fail.
        password = "hello@123"
        expected = False
        result = validate_password(password)
        self.show(password, result, expected)
        self.assertEqual(result, expected)

    def test_missing_special_char(self):
        # Missing special character: should fail despite having digits and uppercase.
        password = "Hello1234"
        expected = False
        result = validate_password(password)
        self.show(password, result, expected)
        self.assertEqual(result, expected)

    def test_multiple_special_chars(self):
        # Multiple special characters allowed: still valid if other rules met.
        password = "Hello!!123"
        expected = True
        result = validate_password(password)
        self.show(password, result, expected)
        self.assertEqual(result, expected)

    def test_edge_case_only_special(self):
        # Only special characters: should fail because missing digit and uppercase.
        password = "@#$!@#$!"
        expected = False  # no digit, no uppercase
        result = validate_password(password)
        self.show(password, result, expected)
        self.assertEqual(result, expected)


# Run the tests
if __name__ == "__main__":
    unittest.main()
