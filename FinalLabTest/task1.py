# ===========================================================
#                   UNIT TESTS WITH OUTPUT
# ===========================================================

import unittest


"""
task1.py

Contains an iterative binary search implementation and a suite of unit tests.

The binary_search function expects a list sorted in ascending order and returns
the index of the target element if found, otherwise -1.

The bottom section uses unittest to verify correctness across multiple cases.
"""

def binary_search(sorted_list, target):
    """
    Perform an iterative binary search on a sorted list in ascending order.

    Parameters:
    - sorted_list: list of comparable items sorted in ascending order.
    - target: the item to search for.

    Returns:
    - int: index of target if found, otherwise -1.

    Implementation notes:
    - Uses two pointers (left, right) to maintain the current search window.
    - Computes mid as left + (right - left) // 2 to avoid potential overflow
      in languages where integer overflow is a concern (keeps intent clear here).
    """
    left = 0
    right = len(sorted_list) - 1

    # Continue while there is a valid search interval.
    while left <= right:
        # Midpoint of current interval
        mid = left + (right - left) // 2
        mid_value = sorted_list[mid]

        # If the middle element matches, return the index.
        if mid_value == target:
            return mid
        # If target is greater than middle, search the right half.
        elif mid_value < target:
            left = mid + 1
        # Otherwise, search the left half.
        else:
            right = mid - 1

    # Target not found.
    return -1





class TestBinarySearch(unittest.TestCase):
    # Unit tests for binary_search: each test constructs a list and a target,
    # invokes binary_search and asserts the returned index matches the expected result.

    def show(self, lst, target, result, expected):
        """
        Helper for printing test inputs and outputs in a readable way.

        This is not required for the assertions, but helps if tests are run
        from a console so the failure context is visible.
        """
        print("\nList:", lst)
        print("Target:", target)
        print("Output:", result)
        print("Expected:", expected)

    def test_empty_list(self):
        """Search in an empty list should return -1."""
        lst = []
        target = 10
        expected = -1
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_single_present(self):
        """Single-element list where the element is present should return 0."""
        lst = [5]
        target = 5
        expected = 0
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_single_absent(self):
        """Single-element list where the element is absent should return -1."""
        lst = [5]
        target = 2
        expected = -1
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_beginning(self):
        """Target at the beginning of the list should return index 0."""
        lst = [1, 2, 3, 4, 5]
        target = 1
        expected = 0
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_middle(self):
        """Target positioned in the middle of the list should return correct index."""
        lst = [10, 20, 30, 40, 50]
        target = 30
        expected = 2
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_end(self):
        """Target at the end of the list should return the last index."""
        lst = [1, 2, 3, 4, 5]
        target = 5
        expected = 4
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_not_found(self):
        """When the target is not in the list, return -1."""
        lst = [2, 4, 6, 8, 10]
        target = 7
        expected = -1
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_even_length(self):
        """Validate behavior on even-length lists."""
        lst = [1, 3, 5, 7]
        target = 5
        expected = 2
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)

    def test_duplicates(self):
        """
        When the list contains duplicates, any valid index of the target is acceptable.

        The test asserts that the returned index is one of the valid positions.
        """
        lst = [1, 2, 2, 2, 3]
        target = 2
        # Any of these indices are valid because they all contain the target.
        expected = [1, 2, 3]
        result = binary_search(lst, target)
        print("\nList:", lst)
        print("Target:", target)
        print("Output:", result)
        print("Expected (any):", expected)
        self.assertIn(result, expected)

    def test_large_list(self):
        """Test correctness and performance on a larger list."""
        lst = list(range(100))
        target = 99
        expected = 99
        result = binary_search(lst, target)
        self.show(lst, target, result, expected)
        self.assertEqual(result, expected)



# Run all tests when executed as a script.
if __name__ == "__main__":
    unittest.main()
